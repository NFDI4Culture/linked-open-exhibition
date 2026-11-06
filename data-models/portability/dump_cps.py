#!/usr/bin/env python
"""
dump_cps.py
-----------
Dumps the content of the CPS Wikibase (https://cps.tibwiki.io/) into a SQLite database,
a DDL file and a full SQL dump. Only the public MediaWiki/Wikibase API is used; no
database access or credentials are needed. A native MariaDB dump of the wiki
(mysqldump) can only be made on the server itself.

Outputs (written next to this script)
    cps-schema.sql      DDL only (CREATE TABLE / INDEX)
    cps-dump.sql        DDL + all INSERT statements (restore: sqlite3 new.db < cps-dump.sql)
    cps.sqlite          the database

Tables: entity, label, description, alias, statement, qualifier, reference_snak.
Every entity also keeps its full Wikibase JSON in entity.json, so nothing is lost.

Usage
    python data-models/portability/dump_cps.py
    python data-models/portability/dump_cps.py --url https://cps.tibwiki.io
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
DB_PATH = HERE / "cps.sqlite"
SCHEMA_PATH = HERE / "cps-schema.sql"
DUMP_PATH = HERE / "cps-dump.sql"

NAMESPACES = {"item": 120, "property": 122}
BATCH = 50

SCHEMA = """
CREATE TABLE meta (
  key   TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE entity (
  entity_id   TEXT PRIMARY KEY,                    -- Q1, P7, ...
  entity_type TEXT NOT NULL CHECK (entity_type IN ('item', 'property')),
  datatype    TEXT,                                -- properties only
  lastrevid   INTEGER,
  modified    TEXT,
  json        TEXT NOT NULL                        -- full Wikibase entity JSON
);

CREATE TABLE label (
  entity_id TEXT NOT NULL REFERENCES entity (entity_id) ON DELETE CASCADE,
  lang      TEXT NOT NULL,
  value     TEXT NOT NULL,
  PRIMARY KEY (entity_id, lang)
);

CREATE TABLE description (
  entity_id TEXT NOT NULL REFERENCES entity (entity_id) ON DELETE CASCADE,
  lang      TEXT NOT NULL,
  value     TEXT NOT NULL,
  PRIMARY KEY (entity_id, lang)
);

CREATE TABLE alias (
  entity_id TEXT NOT NULL REFERENCES entity (entity_id) ON DELETE CASCADE,
  lang      TEXT NOT NULL,
  position  INTEGER NOT NULL,
  value     TEXT NOT NULL,
  PRIMARY KEY (entity_id, lang, position)
);

CREATE TABLE statement (
  statement_id    TEXT PRIMARY KEY,                -- Wikibase statement GUID
  entity_id       TEXT NOT NULL REFERENCES entity (entity_id) ON DELETE CASCADE,
  property_id     TEXT NOT NULL,
  rank            TEXT NOT NULL CHECK (rank IN ('preferred', 'normal', 'deprecated')),
  position        INTEGER NOT NULL,                -- order among all statements of the entity
  snaktype        TEXT NOT NULL CHECK (snaktype IN ('value', 'somevalue', 'novalue')),
  datatype        TEXT,
  value_text      TEXT,                            -- string, url, external-id, time, quantity amount, coordinates, text
  value_entity_id TEXT,                            -- wikibase-item / wikibase-property values
  lang            TEXT,                            -- monolingualtext
  unit            TEXT,                            -- quantity unit (entity ID, or NULL for unitless)
  value_json      TEXT                             -- raw datavalue.value
);
CREATE INDEX statement_entity   ON statement (entity_id, property_id);
CREATE INDEX statement_property ON statement (property_id);
CREATE INDEX statement_value    ON statement (value_entity_id);

CREATE TABLE qualifier (
  qualifier_id    INTEGER PRIMARY KEY,
  statement_id    TEXT NOT NULL REFERENCES statement (statement_id) ON DELETE CASCADE,
  property_id     TEXT NOT NULL,
  snaktype        TEXT NOT NULL,
  datatype        TEXT,
  value_text      TEXT,
  value_entity_id TEXT,
  lang            TEXT,
  unit            TEXT,
  value_json      TEXT
);
CREATE INDEX qualifier_statement ON qualifier (statement_id);

CREATE TABLE reference_snak (
  reference_snak_id INTEGER PRIMARY KEY,
  statement_id      TEXT NOT NULL REFERENCES statement (statement_id) ON DELETE CASCADE,
  reference_hash    TEXT NOT NULL,
  property_id       TEXT NOT NULL,
  snaktype          TEXT NOT NULL,
  datatype          TEXT,
  value_text        TEXT,
  value_entity_id   TEXT,
  lang              TEXT,
  unit              TEXT,
  value_json        TEXT
);
CREATE INDEX reference_statement ON reference_snak (statement_id);
"""


def get(session: requests.Session, api: str, **params) -> dict:
    params.setdefault("format", "json")
    params.setdefault("formatversion", "2")
    for attempt in range(4):
        response = session.get(api, params=params, timeout=60)
        if response.status_code == 429 or response.status_code >= 500:
            time.sleep(2 * (attempt + 1))
            continue
        response.raise_for_status()
        data = response.json()
        if "error" in data:
            raise RuntimeError(f"API error: {data['error']}")
        return data
    response.raise_for_status()
    raise RuntimeError("unreachable")


def list_entity_ids(session: requests.Session, api: str, namespace: int) -> list[str]:
    ids: list[str] = []
    params = {"action": "query", "list": "allpages", "apnamespace": namespace, "aplimit": "max"}
    while True:
        data = get(session, api, **params)
        # titles look like "Item:Q1" / "Property:P7"
        ids.extend(page["title"].split(":", 1)[1] for page in data["query"]["allpages"])
        if "continue" not in data:
            return ids
        params.update(data["continue"])


def fetch_entities(session: requests.Session, api: str, ids: list[str]) -> list[dict]:
    entities: list[dict] = []
    for i in range(0, len(ids), BATCH):
        data = get(session, api, action="wbgetentities", ids="|".join(ids[i:i + BATCH]))
        entities.extend(data["entities"].values())
    return entities


def flatten_snak(snak: dict) -> dict:
    """Reduce a Wikibase snak to the columns shared by statement, qualifier and reference_snak."""
    row = {
        "property_id": snak["property"],
        "snaktype": snak["snaktype"],
        "datatype": snak.get("datatype"),
        "value_text": None,
        "value_entity_id": None,
        "lang": None,
        "unit": None,
        "value_json": None,
    }
    datavalue = snak.get("datavalue")
    if not datavalue:
        return row
    value = datavalue["value"]
    row["value_json"] = json.dumps(value, ensure_ascii=False)
    kind = datavalue["type"]
    if kind == "string":
        row["value_text"] = value
    elif kind == "wikibase-entityid":
        row["value_entity_id"] = value["id"]
    elif kind == "monolingualtext":
        row["value_text"], row["lang"] = value["text"], value["language"]
    elif kind == "time":
        row["value_text"] = value["time"]
    elif kind == "quantity":
        row["value_text"] = value["amount"]
        unit = value.get("unit", "1")
        row["unit"] = None if unit == "1" else unit.rsplit("/", 1)[-1]
    elif kind == "globecoordinate":
        row["value_text"] = f"{value['latitude']},{value['longitude']}"
    else:
        row["value_text"] = json.dumps(value, ensure_ascii=False)
    return row


def insert(db: sqlite3.Connection, table: str, row: dict) -> int:
    cursor = db.execute(
        f"INSERT INTO {table} ({', '.join(row)}) VALUES ({', '.join('?' * len(row))})",
        list(row.values()),
    )
    return cursor.lastrowid


def store_entity(db: sqlite3.Connection, entity: dict) -> int:
    entity_id = entity["id"]
    db.execute(
        "INSERT INTO entity (entity_id, entity_type, datatype, lastrevid, modified, json)"
        " VALUES (?, ?, ?, ?, ?, ?)",
        (entity_id, entity["type"], entity.get("datatype"), entity.get("lastrevid"),
         entity.get("modified"), json.dumps(entity, ensure_ascii=False)),
    )
    for table, key in (("label", "labels"), ("description", "descriptions")):
        for lang, item in entity.get(key, {}).items():
            db.execute(f"INSERT INTO {table} (entity_id, lang, value) VALUES (?, ?, ?)",
                       (entity_id, lang, item["value"]))
    for lang, items in entity.get("aliases", {}).items():
        for position, item in enumerate(items, 1):
            db.execute("INSERT INTO alias (entity_id, lang, position, value) VALUES (?, ?, ?, ?)",
                       (entity_id, lang, position, item["value"]))

    count = 0
    for claims in entity.get("claims", {}).values():
        for claim in claims:
            count += 1
            statement_id = claim["id"]
            insert(db, "statement", {
                "statement_id": statement_id, "entity_id": entity_id, "rank": claim["rank"],
                "position": count, **flatten_snak(claim["mainsnak"]),
            })
            for snaks in claim.get("qualifiers", {}).values():
                for snak in snaks:
                    insert(db, "qualifier", {"statement_id": statement_id, **flatten_snak(snak)})
            for reference in claim.get("references", []):
                for snaks in reference.get("snaks", {}).values():
                    for snak in snaks:
                        insert(db, "reference_snak", {
                            "statement_id": statement_id,
                            "reference_hash": reference.get("hash", ""), **flatten_snak(snak),
                        })
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--url", default="https://cps.tibwiki.io", help="Wikibase base URL")
    args = parser.parse_args()
    base = args.url.rstrip("/")
    api = f"{base}/w/api.php"

    session = requests.Session()
    session.headers["User-Agent"] = "linked-open-exhibition-dump/1.0 (NFDI4Culture)"

    if DB_PATH.exists():
        DB_PATH.unlink()
    db = sqlite3.connect(DB_PATH)
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript(SCHEMA)

    totals = {}
    statements = 0
    for kind, namespace in NAMESPACES.items():
        ids = list_entity_ids(session, api, namespace)
        entities = fetch_entities(session, api, ids)
        for entity in entities:
            statements += store_entity(db, entity)
        totals[kind] = len(entities)
        print(f"{kind}: {len(entities)}")

    meta = {
        "source": base,
        "dumped_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "items": str(totals["item"]),
        "properties": str(totals["property"]),
        "statements": str(statements),
    }
    db.executemany("INSERT INTO meta (key, value) VALUES (?, ?)", meta.items())
    db.commit()

    SCHEMA_PATH.write_text(
        f"-- DDL of the CPS Wikibase dump ({base}), generated by dump_cps.py\n"
        "-- Enable foreign keys on every connection: PRAGMA foreign_keys = ON;\n" + SCHEMA,
        encoding="utf-8",
    )
    with DUMP_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        for line in db.iterdump():
            handle.write(line + "\n")
    db.close()
    print(f"statements: {statements}")
    print(f"wrote {DB_PATH.name}, {SCHEMA_PATH.name}, {DUMP_PATH.name}")


if __name__ == "__main__":
    main()
