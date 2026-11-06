#!/usr/bin/env python
"""
build.py
--------
Builds a private, reviewable copy of the CSV data from the Wikibase model.

Inputs
    data-models/wikibase-model.json      classes, properties, datatypes, equivalents
    data-models/import/*.csv          the data (same files the Wikibase loader reads)
    data-models/wikibase-ids.json        optional: local ID -> Wikibase item ID

Outputs (written next to this script)
    linked-open-exhibition.dtd           DTD generated from the model JSON
    linked-open-exhibition.xml           all CSV data as XML, validated against the DTD
    schema.sql                           SQLite schema (Entity-Attribute-Value)
    linked-open-exhibition.sqlite        the schema filled with the same data
    er-model.qmd                         Mermaid ER diagrams (conceptual, EAV, pipeline)

Usage
    python data-models/portability/build.py            build everything
    python data-models/portability/build.py --validate check the XML file against the DTD only

Two things are NOT in wikibase-model.json and are defined below (SPECS, ASSOCS):
which CSV column feeds which property, and which class an item-valued property may point to.
Statement mapping follows the Wikibase loader notebook (catalogues/wikibase-artwork-load.ipynb).
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
import sys
from dataclasses import dataclass, field
from pathlib import Path

from lxml import etree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MODEL_PATH = ROOT / "data-models" / "wikibase-model.json"
TEMPLATES = ROOT / "data-models" / "import"
IDS_PATH = ROOT / "data-models" / "wikibase-ids.json"

DTD_PATH = HERE / "linked-open-exhibition.dtd"
XML_PATH = HERE / "linked-open-exhibition.xml"
SCHEMA_PATH = HERE / "schema.sql"
DB_PATH = HERE / "linked-open-exhibition.sqlite"
ER_PATH = HERE / "er-model.qmd"

XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"

# --------------------------------------------------------------------------------------
# Model
# --------------------------------------------------------------------------------------
model = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
CLASSES = {c["key"]: c for c in model["classes"]}
PROPS = {p["key"]: p for p in model["properties"]}
PROP_ORDER = {p["key"]: i for i, p in enumerate(model["properties"])}
LABEL_LANGS = model["language_defaults"]["label_languages"]
TITLE_LANG = model["language_defaults"]["title_language"]

# Model properties that are not statements on an item: the local ID becomes the id attribute,
# equivalent_property describes properties and classes themselves.
EXCLUDED = {"equivalent_property", "local_id"}

# Properties that may occur at most once on an item. Everything else may repeat.
# 'title' is required at least once on every class that uses it.
SINGLE = {
    "inception", "date_text", "object_type_text", "materials_text", "height", "width", "depth",
    "inventory_number", "location", "image_url", "wikidata_qid", "gnd_id", "aat_id", "start_date",
    "end_date", "subtitle", "publisher", "publication_date", "isbn13", "dnb_edition_id",
    "described_at_url", "commons_category",
}
REQUIRED = {"title"}

# --------------------------------------------------------------------------------------
# CSV -> statements. Column tuples are (csv column, property key[, options]).
# options: range = class the target item must have, multi = ';'-separated list
# --------------------------------------------------------------------------------------
SPECS = [
    {"file": "person.csv", "id": "person_id", "class": "person", "label": "name",
     "cols": [("wikidata_qid", "wikidata_qid"), ("gnd_id", "gnd_id")]},
    {"file": "term.csv", "id": "term_id", "class_col": "term_type",
     "label_en": "label_en", "label_de": "label_de",
     "cols": [("wikidata_qid", "wikidata_qid"), ("aat_id", "aat_id")]},
    {"file": "exhibition.csv", "id": "exhibition_id", "class": "exhibition",
     "cols": [("title", "title"), ("start_date", "start_date"), ("end_date", "end_date"),
              ("venue_id", "location", {"range": "place"}), ("wikidata_qid", "wikidata_qid")]},
    {"file": "catalogue.csv", "id": "catalogue_id", "class": "catalogue",
     "cols": [("title", "title"), ("subtitle", "subtitle"),
              ("author_ids", "author", {"range": "person", "multi": True}),
              ("publisher_id", "publisher", {"range": "organization"}),
              ("publication_date", "publication_date"), ("isbn13", "isbn13"),
              ("dnb_edition_id", "dnb_edition_id"), ("described_at_url", "described_at_url"),
              ("image_url", "image_url"),
              ("exhibition_id", "catalogue_of", {"range": "exhibition", "multi": True}),
              ("wikidata_qid", "wikidata_qid")]},
    {"file": "artwork.csv", "id": "artwork_id", "class": "artwork",
     "cols": [("title", "title"),
              ("object_type_id", "instance_of", {"range": "object_type"}),
              ("creator_id", "creator", {"range": "person"}),
              ("date_created", "inception"),
              ("material_ids", "made_from_material", {"range": "material", "multi": True}),
              ("height_cm", "height"), ("width_cm", "width"), ("depth_cm", "depth"),
              ("inventory_number", "inventory_number"),
              ("current_location_id", "location", {"range": "place"}),
              ("image_url", "image_url"),
              ("iconclass_notations", "iconclass", {"multi": True}),
              ("date_text", "date_text"), ("object_type_text", "object_type_text"),
              ("materials_text", "materials_text"), ("wikidata_qid", "wikidata_qid")]},
]

# Statements with qualifiers, one CSV row per statement.
ASSOCS = [
    {"file": "exhibition-item.csv", "name": "exhibition_item", "entity": "artwork_id",
     "target": "exhibition_id", "prop": "exhibited_at", "range": "exhibition",
     "quals": [("catalogue_number", "catalogue_number"), ("catalogue_page", "catalogue_page"),
               ("title_as_exhibited", "title_as_exhibited"), ("notes", "note")]},
    {"file": "scan-location.csv", "name": "scan_location", "entity": "artwork_id",
     "target": "catalogue_id", "prop": "appears_in_catalogue", "range": "catalogue",
     "quals": [("scan_page", "scan_page"), ("scan_region", "scan_region"),
               ("extraction_method", "extraction_method"), ("review_status", "review_status"),
               ("notes", "note")]},
]

# Item-valued properties and the class they point to.
RANGES: dict[str, set[str]] = {"exhibition_catalogue": {"catalogue"}}  # inverse of catalogue_of
for _spec in SPECS:
    for _col in _spec["cols"]:
        _opts = _col[2] if len(_col) > 2 else {}
        if "range" in _opts:
            RANGES.setdefault(_col[1], set()).add(_opts["range"])
for _a in ASSOCS:
    RANGES.setdefault(_a["prop"], set()).add(_a["range"])

# Qualifier property -> statement properties it may be attached to.
QUALIFIER_OF: dict[str, list[str]] = {}
for _a in ASSOCS:
    for _, _q in _a["quals"]:
        QUALIFIER_OF.setdefault(_a["prop"], [])
        if _q not in QUALIFIER_OF[_a["prop"]]:
            QUALIFIER_OF[_a["prop"]].append(_q)
for _k in QUALIFIER_OF:
    QUALIFIER_OF[_k].sort(key=PROP_ORDER.get)

QUALIFIER_KEYS = [p["key"] for p in model["properties"] if "qualifier" in p["used_on"]]


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def xml_name(key: str) -> str:
    """XML element name of a property. DTD element names are global, so a property that
    shares its key with a class (object_type) is named after its English label instead."""
    return slug(PROPS[key]["label_en"]) if key in CLASSES else key


def self_check_model() -> None:
    assert "label" not in PROPS and "loe" not in PROPS, "reserved element name used as property key"
    in_map = {q for quals in QUALIFIER_OF.values() for q in quals}
    missing = [k for k in QUALIFIER_KEYS if k not in in_map]
    assert not missing, f"qualifier properties not assigned to a statement property: {missing}"
    names = [xml_name(k) for k in PROPS if k not in EXCLUDED]
    assert len(names) == len(set(names)), "XML element name collision"
    assert not set(names) & set(CLASSES), "XML element name collides with a class name"


# --------------------------------------------------------------------------------------
# Read the CSV files into entities
# --------------------------------------------------------------------------------------
@dataclass
class Stmt:
    prop: str
    value: str
    is_ref: bool = False
    lang: str | None = None
    unit: str | None = None
    quals: list[tuple[str, str]] = field(default_factory=list)


@dataclass
class Entity:
    id: str
    cls: str
    labels: dict[str, str]
    source: str
    stmts: list[Stmt] = field(default_factory=list)


def read_csv(name: str) -> list[dict[str, str]]:
    with open(TEMPLATES / name, newline="", encoding="utf-8-sig") as fh:
        return [{k: (v or "").strip() for k, v in row.items()} for row in csv.DictReader(fh)]


def split_multi(value: str) -> list[str]:
    return [x.strip() for x in value.split(";") if x.strip()]


def load_entities(errors: list[str]) -> dict[str, Entity]:
    ents: dict[str, Entity] = {}
    for spec in SPECS:
        for n, row in enumerate(read_csv(spec["file"]), start=2):
            where = f"{spec['file']} row {n}"
            eid = row[spec["id"]]
            cls = spec.get("class") or row[spec["class_col"]]
            if cls not in CLASSES:
                errors.append(f"{where}: class '{cls}' is not in the model")
                continue
            if eid in ents:
                errors.append(f"{where}: duplicate ID '{eid}' (also {ents[eid].source})")
                continue
            if "label" in spec:
                labels = {lang: row[spec["label"]] for lang in LABEL_LANGS}
            elif "label_en" in spec:
                labels = {"en": row[spec["label_en"]], "de": row[spec["label_de"]] or row[spec["label_en"]]}
            else:
                labels = {}
            ent = Entity(eid, cls, labels, f"{spec['file']}:{n}")
            for col, prop, *rest in spec["cols"]:
                opts = rest[0] if rest else {}
                raw = row[col]
                if not raw:
                    continue
                datatype = PROPS[prop]["datatype"]
                for value in (split_multi(raw) if opts.get("multi") else [raw]):
                    if datatype == "wikibase-item":
                        ent.stmts.append(Stmt(prop, value, is_ref=True))
                    elif datatype == "monolingualtext":
                        ent.stmts.append(Stmt(prop, value, lang=TITLE_LANG))
                    elif datatype == "quantity":
                        ent.stmts.append(Stmt(prop, value.replace(",", "."), unit="cm"))
                    else:
                        ent.stmts.append(Stmt(prop, value))
            ents[eid] = ent

    for a in ASSOCS:
        for n, row in enumerate(read_csv(a["file"]), start=2):
            ent = ents.get(row[a["entity"]])
            if ent is None:
                errors.append(f"{a['file']} row {n}: {a['entity']} '{row[a['entity']]}' not found")
                continue
            quals = [(q, row[col]) for col, q in a["quals"] if row[col]]
            ent.stmts.append(Stmt(a["prop"], row[a["target"]], is_ref=True, quals=quals))

    # inverse link, as the Wikibase loader does: catalogue_of on the catalogue gives
    # exhibition_catalogue on the exhibition
    for ent in list(ents.values()):
        for s in ent.stmts:
            if s.prop == "catalogue_of" and s.value in ents:
                ents[s.value].stmts.append(Stmt("exhibition_catalogue", ent.id, is_ref=True))

    for ent in ents.values():
        ent.stmts.sort(key=lambda s: PROP_ORDER[s.prop])  # stable: keeps CSV order within a property
    return ents


def check_entities(ents: dict[str, Entity], errors: list[str]) -> None:
    for ent in ents.values():
        for s in ent.stmts:
            where = f"{ent.id} ({ent.source})"
            if ent.cls not in PROPS[s.prop]["used_on"]:
                errors.append(f"{where}: property '{s.prop}' is not allowed on class '{ent.cls}'")
            if s.is_ref:
                target = ents.get(s.value)
                if target is None:
                    errors.append(f"{where}: {s.prop} points to '{s.value}', which does not exist")
                elif s.prop in RANGES and target.cls not in RANGES[s.prop]:
                    errors.append(f"{where}: {s.prop} points to {target.id} ({target.cls}), "
                                  f"expected {sorted(RANGES[s.prop])}")


# --------------------------------------------------------------------------------------
# DTD
# --------------------------------------------------------------------------------------
def comment(text: str) -> str:
    return "<!-- " + text.replace("--", "- -") + " -->"


def class_props(cls: str) -> list[dict]:
    return [p for p in model["properties"] if cls in p["used_on"] and p["key"] not in EXCLUDED]


def equivalents_text(p: dict) -> str:
    eq = p.get("equivalents", {})
    return "; ".join(f"{k}: {v}" for k, v in eq.items())


def build_dtd() -> str:
    out = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        comment(f"{model['model']}, version {model['version']}. Generated from "
                "data-models/wikibase-model.json by build.py. Do not edit by hand."),
        comment("Every item is an element named after its class. The ID attribute is the local ID of the "
                "CSV files. Item-valued properties are empty elements with a ref attribute (IDREF), so a "
                "reference to a missing ID is a validation error. Other values are element text."),
        comment("A DTD cannot say which class a ref must point to; the SQLite triggers check that."),
        "",
        f'<!ENTITY % entities "{" | ".join(CLASSES)}">',
        "<!ELEMENT loe (%entities;)*>",
        "<!ATTLIST loe",
        "  model   CDATA #REQUIRED",
        "  version CDATA #REQUIRED>",
        "",
        comment("Label of an item in one language (people and terms)."),
        "<!ELEMENT label (#PCDATA)>",
        "<!ATTLIST label xml:lang NMTOKEN #REQUIRED>",
        "",
    ]

    for ck, c in CLASSES.items():
        props = class_props(ck)
        parts = ["label*" if any(p["key"] in REQUIRED for p in props) else "label+"]
        for p in props:
            suffix = "+" if p["key"] in REQUIRED else ("?" if p["key"] in SINGLE else "*")
            parts.append(xml_name(p["key"]) + suffix)
        out.append(comment(f"{c['label_en']} / {c['label_de']}: {c['description_en']} ({equivalents_text(c)})"))
        out.append(f"<!ELEMENT {ck} (" + ",\n    ".join(parts) + ")>")
        out.append(f"<!ATTLIST {ck}")
        out.append("  id       ID       #REQUIRED")
        out.append("  wikibase NMTOKEN  #IMPLIED")
        out.append("  source   CDATA    #IMPLIED>")
        out.append("")

    declared = []
    for p in model["properties"]:
        key = p["key"]
        if key in EXCLUDED:
            continue
        if not any(c in CLASSES for c in p["used_on"]) and "qualifier" not in p["used_on"]:
            continue
        declared.append(p)

    out.append(comment("Properties. Qualifiers are child elements of the statement they qualify."))
    out.append("")
    for p in declared:
        key, name, dt = p["key"], xml_name(p["key"]), p["datatype"]
        used = ", ".join(p["used_on"])
        out.append(comment(f"{p['label_en']} / {p['label_de']} [{dt}] key={key}, used on: {used}. "
                           f"{p['description_en']} ({equivalents_text(p)})"))
        if dt == "wikibase-item":
            quals = QUALIFIER_OF.get(key)
            content = "(" + ", ".join(f"{xml_name(q)}?" for q in quals) + ")" if quals else "EMPTY"
            out.append(f"<!ELEMENT {name} {content}>")
            out.append(f"<!ATTLIST {name} ref IDREF #REQUIRED>")
        else:
            out.append(f"<!ELEMENT {name} (#PCDATA)>")
            if dt == "monolingualtext":
                out.append(f'<!ATTLIST {name} xml:lang NMTOKEN "{TITLE_LANG}">')
            elif dt == "quantity":
                out.append(f'<!ATTLIST {name} unit (cm) "cm">')
        out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------------------
# XML
# --------------------------------------------------------------------------------------
def build_xml(ents: dict[str, Entity], wikibase_ids: dict[str, str]) -> bytes:
    root = etree.Element("loe", model=model["model"], version=model["version"])
    for ck in CLASSES:
        for ent in (e for e in ents.values() if e.cls == ck):
            el = etree.SubElement(root, ck, id=ent.id)
            if ent.id in wikibase_ids:
                el.set("wikibase", wikibase_ids[ent.id])
            el.set("source", ent.source)
            for lang, text in ent.labels.items():
                lab = etree.SubElement(el, "label")
                lab.set(XML_LANG, lang)
                lab.text = text
            for s in ent.stmts:
                se = etree.SubElement(el, xml_name(s.prop))
                if s.is_ref:
                    se.set("ref", s.value)
                else:
                    se.text = s.value
                if s.lang:
                    se.set(XML_LANG, s.lang)
                if s.unit:
                    se.set("unit", s.unit)
                for qprop, qvalue in sorted(s.quals, key=lambda q: PROP_ORDER[q[0]]):
                    etree.SubElement(se, xml_name(qprop)).text = qvalue
    return etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8",
                          doctype=f'<!DOCTYPE loe SYSTEM "{DTD_PATH.name}">')


def validate_xml(xml_path: Path, dtd_path: Path) -> list[str]:
    dtd = etree.DTD(file=str(dtd_path))
    doc = etree.parse(str(xml_path))
    if dtd.validate(doc):
        return []
    return [f"line {e.line}: {e.message}" for e in dtd.error_log.filter_from_errors()]


# --------------------------------------------------------------------------------------
# SQLite: Entity-Attribute-Value
# --------------------------------------------------------------------------------------
def _statement_trigger(event: str) -> str:
    return f"""
CREATE TRIGGER statement_check_{event.lower()} BEFORE {event} ON statement
BEGIN
  SELECT RAISE(ABORT, 'statement property must not be a qualifier property')
   WHERE (SELECT is_qualifier FROM property WHERE property_key = NEW.property_key) = 1;
  SELECT RAISE(ABORT, 'property is not allowed on the class of this entity (property_class)')
   WHERE NOT EXISTS (SELECT 1 FROM property_class pc JOIN entity e ON e.class_key = pc.class_key
                      WHERE pc.property_key = NEW.property_key AND e.entity_id = NEW.entity_id);
  SELECT RAISE(ABORT, 'item property needs value_entity_id and no value_text')
   WHERE (SELECT datatype FROM property WHERE property_key = NEW.property_key) = 'wikibase-item'
     AND (NEW.value_entity_id IS NULL OR NEW.value_text IS NOT NULL);
  SELECT RAISE(ABORT, 'non-item property needs value_text and no value_entity_id')
   WHERE (SELECT datatype FROM property WHERE property_key = NEW.property_key) <> 'wikibase-item'
     AND (NEW.value_text IS NULL OR NEW.value_entity_id IS NOT NULL);
  SELECT RAISE(ABORT, 'target entity has a class that this property may not point to (property_range)')
   WHERE NEW.value_entity_id IS NOT NULL
     AND EXISTS (SELECT 1 FROM property_range WHERE property_key = NEW.property_key)
     AND NOT EXISTS (SELECT 1 FROM property_range pr JOIN entity t ON t.class_key = pr.class_key
                      WHERE pr.property_key = NEW.property_key AND t.entity_id = NEW.value_entity_id);
END;
"""


def _qualifier_trigger(event: str) -> str:
    return f"""
CREATE TRIGGER qualifier_check_{event.lower()} BEFORE {event} ON qualifier
BEGIN
  SELECT RAISE(ABORT, 'qualifier property expected (property.is_qualifier = 1)')
   WHERE (SELECT is_qualifier FROM property WHERE property_key = NEW.property_key) <> 1;
  SELECT RAISE(ABORT, 'qualifier may not be used on this statement property (qualifier_of)')
   WHERE NOT EXISTS (SELECT 1 FROM qualifier_of q JOIN statement s ON s.property_key = q.property_key
                      WHERE q.qualifier_key = NEW.property_key AND s.statement_id = NEW.statement_id);
END;
"""


SCHEMA_SQL = """\
-- Entity-Attribute-Value schema for the linked-open-exhibition model.
-- Generated by build.py. Enable foreign keys on every connection: PRAGMA foreign_keys = ON;
--
--   entity     one row per item (artwork, person, exhibition, ...)       E
--   property   the attribute catalogue, loaded from wikibase-model.json  A
--   statement  one row per value of a property on an entity              V
--   qualifier  extra values on a statement (catalogue page, scan page)
--
-- Model tables (loaded from wikibase-model.json and build.py)
CREATE TABLE meta (
  key   TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE entity_class (
  class_key      TEXT PRIMARY KEY,
  label_en       TEXT NOT NULL,
  label_de       TEXT,
  description_en TEXT,
  wikidata       TEXT,
  cidoc          TEXT,
  linked_art     TEXT,
  lido           TEXT
);

CREATE TABLE property (
  property_key   TEXT PRIMARY KEY,
  label_en       TEXT NOT NULL,
  label_de       TEXT,
  description_en TEXT,
  datatype       TEXT NOT NULL CHECK (datatype IN
                   ('string','external-id','url','time','quantity','monolingualtext','wikibase-item')),
  is_qualifier   INTEGER NOT NULL DEFAULT 0 CHECK (is_qualifier IN (0, 1)),
  wikidata       TEXT,
  cidoc          TEXT,
  linked_art     TEXT,
  lido           TEXT
);

-- which classes a property may be used on (used_on in the model)
CREATE TABLE property_class (
  property_key TEXT NOT NULL REFERENCES property (property_key),
  class_key    TEXT NOT NULL REFERENCES entity_class (class_key),
  PRIMARY KEY (property_key, class_key)
);

-- which classes an item-valued property may point to (not in the model JSON, defined in build.py)
CREATE TABLE property_range (
  property_key TEXT NOT NULL REFERENCES property (property_key),
  class_key    TEXT NOT NULL REFERENCES entity_class (class_key),
  PRIMARY KEY (property_key, class_key)
);

-- which statement properties a qualifier may be attached to
CREATE TABLE qualifier_of (
  qualifier_key TEXT NOT NULL REFERENCES property (property_key),
  property_key  TEXT NOT NULL REFERENCES property (property_key),
  PRIMARY KEY (qualifier_key, property_key)
);

-- Data tables
CREATE TABLE entity (
  entity_id   TEXT PRIMARY KEY,                               -- local ID, e.g. ART001
  class_key   TEXT NOT NULL REFERENCES entity_class (class_key),
  wikibase_id TEXT,                                           -- item ID in the local Wikibase, e.g. Q50
  source      TEXT                                            -- CSV file and row
);

CREATE TABLE label (
  entity_id TEXT NOT NULL REFERENCES entity (entity_id) ON DELETE CASCADE,
  lang      TEXT NOT NULL,
  label     TEXT NOT NULL,
  PRIMARY KEY (entity_id, lang)
);

CREATE TABLE statement (
  statement_id    INTEGER PRIMARY KEY,
  entity_id       TEXT NOT NULL REFERENCES entity (entity_id) ON DELETE CASCADE,
  property_key    TEXT NOT NULL REFERENCES property (property_key),
  value_text      TEXT,                                       -- string, url, time, quantity, ...
  value_entity_id TEXT REFERENCES entity (entity_id),         -- item-valued properties
  lang            TEXT,                                       -- monolingual text
  unit            TEXT,                                       -- quantities
  position        INTEGER NOT NULL DEFAULT 1,                 -- order among values of one property
  CHECK ((value_text IS NULL) <> (value_entity_id IS NULL))
);
CREATE INDEX statement_entity   ON statement (entity_id, property_key);
CREATE INDEX statement_value    ON statement (value_entity_id);

CREATE TABLE qualifier (
  qualifier_id INTEGER PRIMARY KEY,
  statement_id INTEGER NOT NULL REFERENCES statement (statement_id) ON DELETE CASCADE,
  property_key TEXT NOT NULL REFERENCES property (property_key),
  value_text   TEXT NOT NULL
);
CREATE INDEX qualifier_statement ON qualifier (statement_id);

-- Validation: the same rules the DTD and build.py check, kept in the database
""" + _statement_trigger("INSERT") + _statement_trigger("UPDATE") \
    + _qualifier_trigger("INSERT") + _qualifier_trigger("UPDATE") + """
-- Views for reviewing the data
CREATE VIEW v_entity AS
SELECT e.entity_id, e.class_key,
       COALESCE(l.label,
                (SELECT s.value_text FROM statement s
                  WHERE s.entity_id = e.entity_id AND s.property_key = 'title'
                  ORDER BY s.position LIMIT 1),
                e.entity_id) AS display_label,
       e.wikibase_id, e.source
FROM entity e
LEFT JOIN label l ON l.entity_id = e.entity_id AND l.lang = 'en';

CREATE VIEW v_statement AS
SELECT s.statement_id, s.entity_id, ent.class_key, ent.display_label AS entity_label,
       s.property_key, p.label_en AS property_label, p.datatype,
       COALESCE(s.value_text, tgt.display_label) AS value,
       s.value_entity_id, s.lang, s.unit, s.position
FROM statement s
JOIN v_entity ent ON ent.entity_id = s.entity_id
JOIN property p   ON p.property_key = s.property_key
LEFT JOIN v_entity tgt ON tgt.entity_id = s.value_entity_id;

CREATE VIEW v_artwork AS
SELECT entity_id AS artwork_id,
       MAX(CASE WHEN property_key = 'title'     THEN value END) AS title,
       MAX(CASE WHEN property_key = 'creator'   THEN value END) AS creator,
       MAX(CASE WHEN property_key = 'inception' THEN value END) AS date_created,
       MAX(CASE WHEN property_key = 'instance_of' THEN value END) AS object_type,
       group_concat(CASE WHEN property_key = 'made_from_material' THEN value END, '; ') AS materials,
       MAX(CASE WHEN property_key = 'height'    THEN value END) AS height_cm,
       MAX(CASE WHEN property_key = 'width'     THEN value END) AS width_cm,
       MAX(CASE WHEN property_key = 'depth'     THEN value END) AS depth_cm,
       MAX(CASE WHEN property_key = 'inventory_number' THEN value END) AS inventory_number,
       MAX(CASE WHEN property_key = 'location'  THEN value END) AS location,
       group_concat(CASE WHEN property_key = 'exhibited_at' THEN value END, '; ') AS exhibited_at,
       group_concat(CASE WHEN property_key = 'appears_in_catalogue' THEN value END, '; ') AS appears_in_catalogue
FROM v_statement
WHERE class_key = 'artwork'
GROUP BY entity_id;

CREATE VIEW v_item_in_exhibition AS
SELECT s.entity_id AS artwork_id, a.display_label AS artwork,
       s.value_entity_id AS exhibition_id, x.display_label AS exhibition,
       (SELECT value_text FROM qualifier q WHERE q.statement_id = s.statement_id AND q.property_key = 'catalogue_number') AS catalogue_number,
       (SELECT value_text FROM qualifier q WHERE q.statement_id = s.statement_id AND q.property_key = 'catalogue_page') AS catalogue_page,
       (SELECT value_text FROM qualifier q WHERE q.statement_id = s.statement_id AND q.property_key = 'title_as_exhibited') AS title_as_exhibited,
       (SELECT value_text FROM qualifier q WHERE q.statement_id = s.statement_id AND q.property_key = 'note') AS note
FROM statement s
JOIN v_entity a ON a.entity_id = s.entity_id
JOIN v_entity x ON x.entity_id = s.value_entity_id
WHERE s.property_key = 'exhibited_at';

CREATE VIEW v_scan_location AS
SELECT s.entity_id AS artwork_id, a.display_label AS artwork,
       s.value_entity_id AS catalogue_id, c.display_label AS catalogue,
       (SELECT value_text FROM qualifier q WHERE q.statement_id = s.statement_id AND q.property_key = 'scan_page') AS scan_page,
       (SELECT value_text FROM qualifier q WHERE q.statement_id = s.statement_id AND q.property_key = 'scan_region') AS scan_region,
       (SELECT value_text FROM qualifier q WHERE q.statement_id = s.statement_id AND q.property_key = 'extraction_method') AS extraction_method,
       (SELECT value_text FROM qualifier q WHERE q.statement_id = s.statement_id AND q.property_key = 'review_status') AS review_status,
       (SELECT value_text FROM qualifier q WHERE q.statement_id = s.statement_id AND q.property_key = 'note') AS note
FROM statement s
JOIN v_entity a ON a.entity_id = s.entity_id
JOIN v_entity c ON c.entity_id = s.value_entity_id
WHERE s.property_key = 'appears_in_catalogue';
"""


def build_db(ents: dict[str, Entity], wikibase_ids: dict[str, str]) -> None:
    SCHEMA_PATH.write_text(SCHEMA_SQL, encoding="utf-8", newline="\n")
    if DB_PATH.exists():
        DB_PATH.unlink()
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript(SCHEMA_SQL)

    def eq(spec: dict) -> tuple:
        e = spec.get("equivalents", {})
        return e.get("wikidata"), e.get("cidoc"), e.get("linked_art"), e.get("lido")

    con.executemany("INSERT INTO meta VALUES (?, ?)",
                    [("model", model["model"]), ("model_version", model["version"]),
                     ("source", "data-models/wikibase-model.json and data-models/import/*.csv")])
    con.executemany("INSERT INTO entity_class VALUES (?,?,?,?,?,?,?,?)",
                    [(c["key"], c["label_en"], c["label_de"], c["description_en"], *eq(c))
                     for c in model["classes"]])
    con.executemany("INSERT INTO property VALUES (?,?,?,?,?,?,?,?,?,?)",
                    [(p["key"], p["label_en"], p["label_de"], p["description_en"], p["datatype"],
                      int("qualifier" in p["used_on"]), *eq(p)) for p in model["properties"]])
    con.executemany("INSERT INTO property_class VALUES (?, ?)",
                    [(p["key"], c) for p in model["properties"] for c in p["used_on"] if c in CLASSES])
    con.executemany("INSERT INTO property_range VALUES (?, ?)",
                    [(k, c) for k, classes in RANGES.items() for c in sorted(classes)])
    con.executemany("INSERT INTO qualifier_of VALUES (?, ?)",
                    [(q, k) for k, quals in QUALIFIER_OF.items() for q in quals])

    # all entities first, so that item-valued statements can point to any of them
    con.executemany("INSERT INTO entity VALUES (?, ?, ?, ?)",
                    [(e.id, e.cls, wikibase_ids.get(e.id), e.source) for e in ents.values()])
    con.executemany("INSERT INTO label VALUES (?, ?, ?)",
                    [(e.id, lang, text) for e in ents.values() for lang, text in e.labels.items()])
    for e in ents.values():
        position: dict[str, int] = {}
        for s in e.stmts:
            position[s.prop] = position.get(s.prop, 0) + 1
            cur = con.execute(
                "INSERT INTO statement (entity_id, property_key, value_text, value_entity_id, lang, unit, position) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (e.id, s.prop, None if s.is_ref else s.value, s.value if s.is_ref else None,
                 s.lang, s.unit, position[s.prop]))
            con.executemany("INSERT INTO qualifier (statement_id, property_key, value_text) VALUES (?, ?, ?)",
                            [(cur.lastrowid, q, v) for q, v in s.quals])
    con.commit()
    con.close()


def check_db() -> list[str]:
    problems = []
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA foreign_keys = ON")
    if con.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
        problems.append("SQLite integrity_check failed")
    for row in con.execute("PRAGMA foreign_key_check"):
        problems.append(f"foreign key violation: {row}")
    con.close()
    return problems


# --------------------------------------------------------------------------------------
# Mermaid
# --------------------------------------------------------------------------------------
def mm_type(datatype: str) -> str:
    return "decimal" if datatype == "quantity" else "string"


def conceptual_er(ents: dict[str, Entity]) -> str:
    term_classes = [c for c in CLASSES if any(e.cls == c and e.source.startswith("term.csv") for e in ents.values())]
    attrs: dict[str, list[tuple]] = {c: [] for c in CLASSES}
    rels: list[tuple] = []
    for spec in SPECS:
        for cls in ([spec["class"]] if "class" in spec else term_classes):
            attrs[cls].append(("string", "id", "PK", "local ID"))
            if "label" in spec or "label_en" in spec:
                attrs[cls].append(("string", "label", "", "en and de"))
            for col, prop, *rest in spec["cols"]:
                if cls not in PROPS[prop]["used_on"]:
                    continue
                if PROPS[prop]["datatype"] == "wikibase-item":
                    rel = (cls, rest[0]["range"], prop, "o{" if rest[0].get("multi") else "o|")
                    if rel not in rels:
                        rels.append(rel)
                else:
                    note = "" if PROPS[prop]["datatype"] == "string" else PROPS[prop]["datatype"]
                    attrs[cls].append((mm_type(PROPS[prop]["datatype"]), prop, "", note))
    lines = ["erDiagram"]
    for rel_from, rel_to, prop, card in rels:
        lines.append(f'    {rel_from.upper()} }}o--{card} {rel_to.upper()} : "{prop}"')
    for a in ASSOCS:
        name = a["name"].upper()
        lines.append(f'    ARTWORK ||--o{{ {name} : "{a["prop"]}"')
        lines.append(f'    {a["range"].upper()} ||--o{{ {name} : "{a["prop"]}"')
    lines.append("")
    for cls in CLASSES:
        if not attrs[cls]:
            continue
        lines.append(f"    {cls.upper()} {{")
        for t, n, key, note in attrs[cls]:
            lines.append(f'        {t} {n}' + (f" {key}" if key else "") + (f' "{note}"' if note else ""))
        lines.append("    }")
    for a in ASSOCS:
        lines.append(f'    {a["name"].upper()} {{')
        lines.append(f'        string {a["entity"]} FK')
        lines.append(f'        string {a["target"]} FK')
        for _, q in a["quals"]:
            lines.append(f'        string {q} "qualifier"')
        lines.append("    }")
    return "\n".join(lines)


def eav_er() -> str:
    con = sqlite3.connect(DB_PATH)
    tables = [r[0] for r in con.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY rowid")]
    lines = ["erDiagram"]
    bodies = []
    for t in tables:
        cols = con.execute(f"PRAGMA table_info({t})").fetchall()
        fks = {r[3] for r in con.execute(f"PRAGMA foreign_key_list({t})")}
        body = [f"    {t} {{"]
        for _cid, name, ctype, _notnull, _default, pk in cols:
            keys = ", ".join(k for k, on in (("PK", pk), ("FK", name in fks)) if on)
            body.append(f"        {ctype or 'TEXT'} {name}" + (f" {keys}" if keys else ""))
        body.append("    }")
        bodies.append("\n".join(body))
        notnull = {c[1]: c[3] for c in cols}
        pk_count = sum(1 for c in cols if c[5])
        for r in con.execute(f"PRAGMA foreign_key_list({t})"):
            parent, col = r[2], r[3]
            parent_card = "||" if notnull[col] else "o|"
            child_card = "o|" if pk_count == 1 and any(c[1] == col and c[5] for c in cols) else "o{"
            lines.append(f'    {parent} {parent_card}--{child_card} {t} : "{col}"')
    con.close()
    return "\n".join(lines + [""] + bodies)


PIPELINE = """flowchart LR
    CSV[/"CSV templates<br/>data-models/import"/]
    MODEL[/"wikibase-model.json"/]
    subgraph PRIVATE["Private review copy (portability/)"]
        DTD["DTD"]
        XML["XML<br/>validated against DTD"]
        SQL[("SQLite EAV<br/>+ triggers + views")]
    end
    LOADER["Loader notebook<br/>wikibase-artwork-load.ipynb"]
    WB[("Local Wikibase<br/>localhost:8090")]
    WD[("Wikidata")]
    MODEL -->|generates| DTD
    MODEL -->|generates properties| LOADER
    MODEL -->|seeds schema| SQL
    CSV -->|build.py| XML
    CSV -->|build.py| SQL
    DTD -. validates .-> XML
    CSV --> LOADER
    LOADER --> WB
    WB -. "later, via QuickStatements or API" .-> WD
    SRC{{"Source of truth: not decided yet"}}
    SRC -.-> CSV
    SRC -.-> WB
    SRC -.-> WD
    style PRIVATE fill:transparent,stroke:#888,stroke-dasharray:5 5,color:#333
"""

EXAMPLE_SQL = """-- artworks with their creator, date, materials and catalogue
SELECT * FROM v_artwork LIMIT 10;

-- every statement about one artwork
SELECT property_label, value, lang, unit FROM v_statement WHERE entity_id = 'ART001';

-- artworks that are not linked to a catalogue
SELECT entity_id, entity_label FROM v_entity e
 WHERE class_key = 'artwork'
   AND NOT EXISTS (SELECT 1 FROM statement s WHERE s.entity_id = e.entity_id
                    AND s.property_key = 'appears_in_catalogue');

-- how much of each property is filled in
SELECT p.label_en, COUNT(*) AS statements
  FROM statement s JOIN property p USING (property_key)
 GROUP BY p.label_en ORDER BY statements DESC;"""


def build_er_qmd(ents: dict[str, Entity]) -> str:
    return f"""---
title: "Entity-relationship model"
subtitle: "Conceptual model, SQLite EAV schema and data pipeline"
---

Generated by `data-models/portability/build.py` from `wikibase-model.json` and the CSV templates. Do not edit by hand.

## Conceptual model

The classes of the Wikibase model and how the CSV files connect them. `EXHIBITION_ITEM` and `SCAN_LOCATION` are CSV files that become statements with qualifiers in Wikibase (`Exhibited at` and `Appears in catalogue`). The inverse link `Exhibition catalogue` is created from `catalogue_of` and is not drawn.

```{{mermaid}}
{conceptual_er(ents)}
```

## SQLite schema (Entity-Attribute-Value)

Read directly from `linked-open-exhibition.sqlite`. The model tables describe the attributes. The data tables hold every fact as one row in `statement`. Triggers reject statements whose property is not allowed on the entity's class, whose value has the wrong kind, or whose target has the wrong class.

```{{mermaid}}
{eav_er()}
```

## Setup

```{{mermaid}}
{PIPELINE}```

## Example queries

```sql
{EXAMPLE_SQL}
```
"""


# --------------------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--validate", action="store_true", help="only validate the XML file against the DTD")
    args = ap.parse_args()

    self_check_model()

    if args.validate:
        problems = validate_xml(XML_PATH, DTD_PATH)
        print("XML is valid against the DTD." if not problems else "\n".join(problems))
        return 1 if problems else 0

    errors: list[str] = []
    ents = load_entities(errors)
    check_entities(ents, errors)
    if errors:
        print(f"{len(errors)} problem(s) in the CSV data, nothing written:")
        for e in errors:
            print("  " + e)
        return 1

    wikibase_ids = {}
    if IDS_PATH.exists():
        wikibase_ids = json.loads(IDS_PATH.read_text(encoding="utf-8")).get("items", {})

    DTD_PATH.write_text(build_dtd(), encoding="utf-8", newline="\n")
    XML_PATH.write_bytes(build_xml(ents, wikibase_ids))
    problems = validate_xml(XML_PATH, DTD_PATH)
    build_db(ents, wikibase_ids)
    problems += check_db()

    con = sqlite3.connect(DB_PATH)
    n_stmt = con.execute("SELECT COUNT(*) FROM statement").fetchone()[0]
    n_qual = con.execute("SELECT COUNT(*) FROM qualifier").fetchone()[0]
    n_lab = con.execute("SELECT COUNT(*) FROM label").fetchone()[0]
    con.close()
    root = etree.parse(str(XML_PATH)).getroot()
    xml_stmts = sum(1 for ent in root for ch in ent if ch.tag != "label")
    if xml_stmts != n_stmt:
        problems.append(f"XML has {xml_stmts} statements, SQLite has {n_stmt}")

    ER_PATH.write_text(build_er_qmd(ents), encoding="utf-8", newline="\n")

    print(f"{len(ents)} items, {n_stmt} statements, {n_qual} qualifiers, {n_lab} labels")
    for name in (DTD_PATH, XML_PATH, SCHEMA_PATH, DB_PATH, ER_PATH):
        print(f"  wrote {name.relative_to(ROOT)}")
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print("  " + p)
        return 1
    print("XML valid against DTD; SQLite integrity and foreign keys ok.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
