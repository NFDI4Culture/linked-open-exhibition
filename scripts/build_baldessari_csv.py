"""Build the Wikibase load CSVs from data-models/import/baldessari-artwork.csv.

Reads  : baldessari-artwork.csv (artwork_id, title, creator, date, object_type, materials, height_cm, width_cm)
         term.csv / person.csv (existing curated rows are kept as they are)
Writes : artwork.csv, term.csv, person.csv, exhibition-item.csv, catalogue.csv in the same folder.

Free-text object types and materials are normalised to shared terms (see OBJECT_TYPES and MATERIAL_ALIASES).
Film/video details are kept: specific film types are object types, colour / black-and-white / sound / 16 mm
are material terms. Dates such as 1972-73 and 1970s are loaded as they are (see the notebook).
"""
import csv
import re
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "data-models" / "import"
SOURCE = TEMPLATES / "baldessari-artwork.csv"
EXHIBITION_ID = "EXH001"
VENUE_ID = "PLC001"

# canonical object types: key -> (label_en, label_de, wikidata_qid)
OBJECT_TYPES = {
    "painting": ("painting", "Gemälde", "Q3305213"),
    "photograph": ("photograph", "Fotografie", "Q125191"),
    "super-8 film loop (originally 16 mm)": ("Super-8 film loop (originally 16 mm)", "Super-8-Filmloop (ursprünglich 16 mm)", ""),
    "super-8 film loop": ("Super-8 film loop", "Super-8-Filmloop", ""),
    "super-8 film": ("Super-8 film", "Super-8-Film", ""),
    "16 mm film": ("16 mm film", "16-mm-Film", ""),
    "film loop": ("film loop", "Filmloop", ""),
    "video loop": ("video loop", "Videoloop", ""),
    "wallpaper": ("wallpaper", "Tapete", "Q191529"),
    "illustration": ("illustration", "Illustration", "Q178659"),
}

# material atom -> (label_en, label_de, wikidata_qid); None = not a material (film attribute)
MATERIALS = {
    "inkjet": ("inkjet", "Tintenstrahldruck", "Q130443678"),
    "canvas": ("canvas", "Leinwand", "Q4259259"),
    "acrylic paint": ("acrylic paint", "Acrylfarbe", "Q207849"),
    "photoemulsion": ("photoemulsion", "Fotoemulsion", ""),
    "hand lettering": ("hand lettering", "Handbeschriftung", ""),
    "digital printing": ("digital printing", "Digitaldruck", ""),
    "black-and-white photograph": ("black-and-white photograph", "Schwarzweißfotografie", ""),
    "color photograph": ("color photograph", "Farbfotografie", ""),
    "gelatin silver print": ("gelatin silver print", "Silbergelatineabzug", "Q64029133"),
    "oil stain": ("oil stain", "Ölfleck", ""),
    "oil stick": ("oil stick", "Ölstift", "Q7081466"),
    "oil pastel": ("oil pastel", "Ölpastell", ""),
    "oil tint": ("oil tint", "Öltönung", ""),
    "oil enamel": ("oil enamel", "Ölemail", ""),
    "vinyl paint": ("vinyl paint", "Vinylfarbe", "Q2135874"),
    "vinyl": ("vinyl", "Vinyl", ""),
    "pencil": ("pencil", "Bleistift", ""),
    "crayon": ("crayon", "Kreide", ""),
    "paper": ("paper", "Papier", ""),
    "metallic paper": ("metallic paper", "Metallpapier", ""),
    "Gandhi Ashram paper": ("Gandhi Ashram paper", "Gandhi-Ashram-Papier", ""),
    "paper stickers": ("paper stickers", "Papieraufkleber", ""),
    "photocopy": ("photocopy", "Fotokopie", ""),
    "Masonite": ("Masonite", "Masonit", ""),
    "aluminium": ("aluminium", "Aluminium", ""),
    "rubber": ("rubber", "Gummi", ""),
    "formica": ("Formica", "Formica", ""),
    "Folio D process": ("Folio D process", "Folio-D-Verfahren", ""),
    "wallpaper": ("wallpaper", "Tapete", "Q191529"),
    "color": ("color", "Farbe", ""),
    "black-and-white": ("black-and-white", "Schwarzweiß", ""),
    "sound": ("sound", "Ton", ""),
    "16 mm": ("16 mm", "16 mm", ""),
}
# term.csv rows that were curated by hand; every other row is regenerated
BASE_TERM_IDS = {"MAT001", "MAT002", "MAT003", "TYP001", "TYP002", "PLC001"}

MATERIAL_ALIASES = {
    "acrylic": "acrylic paint", "acrylic paint": "acrylic paint", "acrylic wash": "acrylic paint",
    "inkjet": "inkjet", "inkjet print": "inkjet",
    "canvas": "canvas", "photoemulsion": "photoemulsion", "hand lettering": "hand lettering",
    "digital printing": "digital printing",
    "black-and-white photograph": "black-and-white photograph",
    "black-and-white photographs": "black-and-white photograph",
    "color photograph": "color photograph", "color photographs": "color photograph",
    "gelatin silver photographs": "gelatin silver print",
    "oil stain": "oil stain", "oil stick": "oil stick", "oil pastel": "oil pastel",
    "oil tint": "oil tint", "oil enamel": "oil enamel",
    "vinyl paint": "vinyl paint", "vinyl": "vinyl", "pencil": "pencil", "crayon": "crayon",
    "paper": "paper", "metallic paper": "metallic paper", "gandhi ashram paper": "Gandhi Ashram paper",
    "paper stickers": "paper stickers", "photocopy": "photocopy", "masonite": "Masonite",
    "aluminium": "aluminium", "rubber": "rubber", "formica": "formica",
    "folio d process": "Folio D process", "wallpaper": "wallpaper",
    "color": "color", "black-and-white": "black-and-white", "sound": "sound", "16 mm": "16 mm",
}

PERSONS = {
    "John Baldessari": ("Q683378", "118506153"),
    "Laurence Sterne": ("Q218960", "11861794X"),
    # authors of the texts in the catalogue (GND from the DNB record 957409494)
    "Meg Cranston": ("", "119555522"),
    "Diedrich Diederichsen": ("", "130448001"),
    "Thomas Weski": ("", "119093022"),
}

# the exhibition catalogue (DNB record 957409494) and its publisher
ORGANIZATIONS = [("ORG001", "König", "König")]
CATALOGUE_HEADER = ["catalogue_id", "title", "subtitle", "author_ids", "publisher_id", "publication_date",
                    "isbn13", "dnb_edition_id", "described_at_url", "image_url", "exhibition_id", "wikidata_qid"]
CATALOGUE_ROWS = [[
    "CAT001", "Baldessari",
    "while something is happening here, something else is happening there ; works 1988 - 1999 ; "
    "Spectrum - Internationaler Preis für Fotografie der Stiftung Niedersachsen ; "
    "[Sprengel-Museum Hannover, 26.9.1999 - 2.1.2000 und Staatliche Kunstsammlungen Dresden, "
    "Gemäldegalerie Neue Meister, 15.1. - 2.4.2000]",
    "PER003; PER004; PER005", "ORG001", "1999", "978-3-88375-396-6", "957409494",
    "https://d-nb.info/957409494", "", EXHIBITION_ID, "",
]]

# catalogue pages already recorded in the earlier 3-row sample, keyed by (title, date)
KNOWN_PAGES = {
    ("Goya Series: Strange", "1997"): "14",
    ("Goya Series: These Too", "1997"): "14; 51",
    ("Tetrad Series. All Getting On Together", "1999"): "17",
}


def object_type(raw):
    s = raw.lower()
    if not s:
        return ""
    if s == "painting" or "canvas" in s:
        return "painting"
    if "photograph" in s:
        return "photograph"
    if s in OBJECT_TYPES:
        return s
    if s in ("black-and-white film loop", "color film loop"):
        return "film loop"
    if s == "black-and-white":  # colour descriptor in the type column (ART068): no usable type
        return ""
    raise ValueError(f"unmapped object type: {raw!r}")


def type_attributes(raw):
    """Colour descriptor hidden in the object type, e.g. 'color film loop'."""
    s = raw.lower()
    if s.startswith("color "):
        return ["color"]
    if s.startswith("black-and-white "):
        return ["black-and-white"]
    return []


def material_atoms(raw):
    s = raw.lower().replace("ink-jet", "inkjet").replace("ink jet", "inkjet")
    s = s.replace("color and black and white photographs", "color photographs, black and white photographs")
    s = s.replace("black and white", "black-and-white")
    s = re.sub(r"\bmounted on\b", ",", s)
    atoms = []
    for part in re.split(r"\s*[;,]\s*|\s+on\s+|\s+and\s+", s):
        part = part.strip()
        if part:
            atoms.append(part)
    out = []
    for a in atoms:
        if a not in MATERIAL_ALIASES:
            raise ValueError(f"unmapped material {a!r} in {raw!r}")
        key = MATERIAL_ALIASES[a]
        if key not in out:
            out.append(key)
    return out


def read(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write(path, header, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def main():
    src = read(SOURCE)

    # --- terms: keep existing curated rows, then add what is missing
    existing = [{k: v.strip() for k, v in r.items()} for r in read(TEMPLATES / "term.csv")]
    terms = [t for t in existing if t["term_id"] in BASE_TERM_IDS]
    by_key = {(t["term_type"], t["label_en"].lower()): t["term_id"] for t in terms}
    counters = {"material": 0, "object_type": 0, "place": 0}
    prefix = {"material": "MAT", "object_type": "TYP", "place": "PLC"}
    for t in terms:
        counters[t["term_type"]] = max(counters[t["term_type"]], int(t["term_id"][3:]))

    def term_id(term_type, label_en, label_de, qid):
        key = (term_type, label_en.lower())
        if key not in by_key:
            counters[term_type] += 1
            tid = f"{prefix[term_type]}{counters[term_type]:03d}"
            terms.append({"term_id": tid, "term_type": term_type, "label_en": label_en,
                          "label_de": label_de, "aat_id": "", "wikidata_qid": qid})
            by_key[key] = tid
        return by_key[key]

    artworks, items, problems = [], [], []
    for r in src:
        aid = r["artwork_id"]
        title = r["title"].strip()
        try:
            ot = object_type(r["object_type"])
            atoms = material_atoms(r["materials"])
        except ValueError as e:
            problems.append(f"{aid}: {e}")
            continue
        colour = {"color", "black-and-white"}
        for extra in type_attributes(r["object_type"]):
            if not colour & set(atoms):
                atoms.append(extra)
            elif extra not in atoms:
                problems.append(f"{aid}: object type '{r['object_type']}' conflicts with materials '{r['materials']}', kept materials")
        if r["object_type"].lower() == "black-and-white":
            problems.append(f"{aid}: object type 'black-and-white' is a colour value, object type left empty")
        ot_id = term_id("object_type", *OBJECT_TYPES[ot]) if ot else ""
        mat_ids = [term_id("material", *MATERIALS[a]) for a in atoms]
        date = r["date"].strip()
        person = "PER001" if r["creator"] == "John Baldessari" else "PER002"
        artworks.append([aid, title, ot_id, person, date, "; ".join(mat_ids),
                         r["height_cm"], r["width_cm"], "", "", "", "", "", "",
                         r["date"].strip(), r["object_type"].strip(), r["materials"].strip()])
        items.append([aid, EXHIBITION_ID, "", KNOWN_PAGES.get((title, date), ""), "", ""])

    write(TEMPLATES / "artwork.csv",
          ["artwork_id", "title", "object_type_id", "creator_id", "date_created", "material_ids",
           "height_cm", "width_cm", "depth_cm", "inventory_number", "current_location_id",
           "image_url", "iconclass_notations", "wikidata_qid",
           "date_text", "object_type_text", "materials_text"], artworks)
    write(TEMPLATES / "exhibition-item.csv",
          ["artwork_id", "exhibition_id", "catalogue_number", "catalogue_page",
           "title_as_exhibited", "notes"], items)
    write(TEMPLATES / "term.csv", ["term_id", "term_type", "label_en", "label_de", "aat_id", "wikidata_qid"],
          [[t["term_id"], t["term_type"], t["label_en"], t["label_de"], t["aat_id"], t["wikidata_qid"]] for t in terms]
          + [[oid, "organization", en, de, "", ""] for oid, en, de in ORGANIZATIONS])
    write(TEMPLATES / "person.csv", ["person_id", "name", "wikidata_qid", "gnd_id"],
          [[f"PER{i:03d}", n, q, g] for i, (n, (q, g)) in enumerate(PERSONS.items(), 1)])
    write(TEMPLATES / "catalogue.csv", CATALOGUE_HEADER, CATALOGUE_ROWS)

    print(f"{len(artworks)} artworks, {len(items)} exhibition items, {len(terms)} terms, {len(PERSONS)} persons")
    for p in problems:
        print("NOTE:", p)
    return 1 if any("unmapped" in p for p in problems) else 0


if __name__ == "__main__":
    sys.exit(main())
