"""
extract_artworks.py
-------------------
Stage 2 of the catalogue OCR pipeline.

Reads the full OCR text produced by ocr_catalogue.py and attempts to parse
individual catalogue entries into structured rows, saving the result as a CSV.

Data-model columns follow the three Linked Open Exhibition data models:
  - Item in Exhibition  (data-models/item-in-exhibition.csv)
  - Artist              (data-models/artists-data-model.csv)
  - Exhibition          (data-models/exhibition.csv)

Output CSV: output/baldessari-sprengel-artworks.csv

Usage:
    python scripts/extract_artworks.py [OCR_TEXT_FILE] [--output CSV_PATH]
                                       [--exhibition "Title"] [--location "Place"]
                                       [--start YYYY-MM-DD] [--end YYYY-MM-DD]

Parsing strategy
----------------
Exhibition catalogue entries for printed catalogues typically follow a
repeating block pattern such as:

    [ARTIST NAME]
    [Artwork title], [year]
    [Medium / materials]
    [Height] x [Width] [unit]  (or Width x Height, varies by museum)
    [Collection / lender]
    [Catalogue number]

Because OCR output from scanned books is noisy, the parser applies a
sequence of heuristic rules rather than strict templates. Every extracted
field that is uncertain is flagged with a trailing " [?]" to aid manual review.

After running this script you should:
  1. Open output/baldessari-sprengel-artworks.csv in a spreadsheet.
  2. Correct any OCR artefacts, fill in missing fields, remove [?] flags.
  3. Proceed to Stage 3 (XML generation) only when the data looks clean.
"""

import argparse
import csv
import re
import sys
from pathlib import Path
from dataclasses import dataclass, fields, asdict


# ---------------------------------------------------------------------------
# Data model – mirrors the three Linked Open Exhibition CSV schemas
# ---------------------------------------------------------------------------

@dataclass
class ArtworkRecord:
    """One row in the output CSV."""
    # Artwork fields (item-in-exhibition data model)
    catalogue_no: str = ""          # P528  catalogue code
    artwork_title: str = ""         # P1476 title
    artwork_title_lang: str = ""    # language of title (iso 639-1)
    artwork_type: str = ""          # P31   instance of (painting, print, …)
    artwork_inception: str = ""     # P571  year/date created
    medium_material: str = ""       # P186  made from material / technique
    height_cm: str = ""             # P2048 height
    width_cm: str = ""              # P2049 width
    depth_cm: str = ""              # P2610 depth
    collection: str = ""            # P195  collection / lender
    inventory_number: str = ""      # P217  inventory number
    depicts: str = ""               # P180  depicted subjects
    image_url: str = ""             # P18   image URL (Wikimedia Commons if available)
    described_at_url: str = ""      # P973  described at URL

    # Artist fields (artists data model)
    artist_full_name: str = ""      # display name
    artist_given_name: str = ""     # P735
    artist_family_name: str = ""    # P734
    artist_birth_year: str = ""     # P569
    artist_death_year: str = ""     # P570
    artist_nationality: str = ""    # P27
    artist_profession: str = ""     # P106
    artist_wikidata_qid: str = ""   # reference QID
    artist_gnd_id: str = ""         # P227 GND identifier
    artist_ulan_id: str = ""        # P245 Getty ULAN

    # Exhibition fields (exhibition data model)
    exhibition_title: str = ""      # P1476
    exhibition_location: str = ""   # P276
    exhibition_start: str = ""      # P580
    exhibition_end: str = ""        # P582
    exhibition_organizer: str = ""  # P664
    exhibition_wikidata_qid: str = ""

    # Provenance / meta
    source_page: str = ""           # page number in catalogue
    notes: str = ""                 # free-text notes / OCR artefacts


CSV_COLUMNS = [f.name for f in fields(ArtworkRecord)]


# ---------------------------------------------------------------------------
# Heuristic parsing helpers
# ---------------------------------------------------------------------------

# Dimension patterns:  76 × 61 cm  |  76x61cm  |  76 cm x 61 cm
_DIM_RE = re.compile(
    r"(\d[\d,\.]*)\s*[x×xX]\s*(\d[\d,\.]*)"
    r"(?:\s*[x×xX]\s*(\d[\d,\.]*))?"
    r"\s*(cm|mm|m|in|\")?",
    re.IGNORECASE,
)

# Year:  2000  |  (2000)  |  1998-2000  |  ca. 1967
_YEAR_RE = re.compile(r"\b((?:ca\.?\s*)?\d{4}(?:[/-]\d{4})?)\b")

# Catalogue number patterns:  Kat.-Nr. 5  |  No. 12  |  Cat. 3  |  [5]
_CATNO_RE = re.compile(
    r"(?:Kat\.?-?Nr\.?|Kat\.?\s*Nr\.?|Cat\.?\s*(?:No\.?)?|No\.?)\s*(\d+)",
    re.IGNORECASE,
)
_CATNO_BRACKET_RE = re.compile(r"^\s*\[(\d+)\]\s*$")

# Inventory:  Inv. 1234  |  Inv.-Nr. AB-1234
_INV_RE = re.compile(r"Inv\.?(?:-?Nr\.?)?\s*([\w\-/\.]+)", re.IGNORECASE)

# Artist name: a line that is ALL CAPS (after cleaning) with at least 2 chars
_ALLCAPS_RE = re.compile(r"^[A-ZAOUOÜÄÖ\s\.\-\']+$")


def _clean(text: str) -> str:
    """Remove common OCR noise characters."""
    return text.replace("\u00ad", "").strip()


def _is_allcaps_name(line: str) -> bool:
    """Return True if the line looks like an ALL-CAPS artist name."""
    cleaned = _clean(line)
    if len(cleaned) < 4:
        return False
    # Allow accented uppercase letters common in German/French names
    return bool(re.match(r"^[A-Z\u00C0-\u00D6\u00D8-\u00DE\s\.\-\']+$", cleaned))


def _parse_dimensions(text: str) -> tuple[str, str, str]:
    """Return (height_cm, width_cm, depth_cm) from a text fragment."""
    m = _DIM_RE.search(text)
    if not m:
        return "", "", ""
    h, w, d = m.group(1), m.group(2), m.group(3) or ""
    # Normalise decimal separator
    h = h.replace(",", ".")
    w = w.replace(",", ".")
    d = d.replace(",", ".")
    return h, w, d


def _split_artist_name(full: str) -> tuple[str, str]:
    """
    Attempt to split 'GIVEN FAMILY' or 'FAMILY, GIVEN' into parts.
    Returns (given_name, family_name).
    """
    full = full.title()  # convert ALL-CAPS to Title Case
    if "," in full:
        parts = [p.strip() for p in full.split(",", 1)]
        return parts[1], parts[0]   # given, family
    parts = full.split()
    if len(parts) == 1:
        return "", parts[0]
    return " ".join(parts[:-1]), parts[-1]


def _extract_year(text: str) -> str:
    """Return the first plausible year found in text, else ''."""
    m = _YEAR_RE.search(text)
    return m.group(1) if m else ""


def _extract_cat_no(text: str) -> str:
    """Return catalogue number string, else ''."""
    m = _CATNO_RE.search(text)
    if m:
        return m.group(1)
    m2 = _CATNO_BRACKET_RE.match(text)
    if m2:
        return m2.group(1)
    return ""


def _extract_inv_no(text: str) -> str:
    m = _INV_RE.search(text)
    return m.group(1) if m else ""


def _looks_like_medium(line: str) -> bool:
    """Heuristic: does the line describe a medium/technique?"""
    medium_keywords = (
        "print", "photograph", "oil", "acrylic", "ink", "pencil",
        "watercolour", "watercolor", "gouache", "lithograph", "etching",
        "screen", "silkscreen", "collage", "video", "installation",
        "neon", "bronze", "marble", "canvas", "paper", "board",
        # German equivalents
        "druck", "fotografie", "foto", "ol", "acryl", "tinte",
        "bleistift", "aquarell", "lithografie", "radierung", "siebdruck",
        "collage", "video", "installation", "leinwand", "karton",
    )
    lower = line.lower()
    return any(kw in lower for kw in medium_keywords)


# ---------------------------------------------------------------------------
# Block-level parser
# ---------------------------------------------------------------------------

def parse_ocr_blocks(full_text: str, exhibition_defaults: dict) -> list[ArtworkRecord]:
    """
    Parse the full OCR text into a list of ArtworkRecord objects.

    The parser splits the text into page sections, then within each page
    attempts to identify catalogue entry blocks using the following signal:

      - A line in ALL-CAPS that looks like an artist name starts a new block.
      - Lines following the artist name are assigned to title, medium,
        dimensions, collection, and catalogue number using heuristics.
      - A block ends when the next ALL-CAPS artist name is encountered,
        or when a page boundary marker (=== PAGE N ===) is seen.
    """
    records: list[ArtworkRecord] = []

    # Split into page sections
    page_sections = re.split(r"={3}\s*PAGE\s+(\d+)\s*={3}", full_text)
    # re.split with a capture group interleaves page numbers and content:
    # ['', '1', 'page1 text', '2', 'page2 text', …]
    pages: list[tuple[int, str]] = []
    i = 1
    while i < len(page_sections) - 1:
        page_num = int(page_sections[i])
        page_text = page_sections[i + 1]
        pages.append((page_num, page_text))
        i += 2

    for page_num, page_text in pages:
        lines = [_clean(ln) for ln in page_text.splitlines()]

        # Group lines into candidate entry blocks
        blocks: list[tuple[int, list[str]]] = []  # (start_line_idx, lines)
        current_block: list[str] = []
        for idx, line in enumerate(lines):
            if not line:
                continue
            if _is_allcaps_name(line) and len(line) > 3:
                if current_block:
                    blocks.append((idx, current_block))
                current_block = [line]
            else:
                current_block.append(line)
        if current_block:
            blocks.append((len(lines), current_block))

        for _, block_lines in blocks:
            if not block_lines:
                continue

            rec = ArtworkRecord(**exhibition_defaults)
            rec.source_page = str(page_num)
            leftover_notes: list[str] = []

            # First line → artist name
            artist_raw = block_lines[0]
            if _is_allcaps_name(artist_raw):
                rec.artist_full_name = artist_raw.title()
                given, family = _split_artist_name(artist_raw)
                rec.artist_given_name = given
                rec.artist_family_name = family
            else:
                leftover_notes.append(artist_raw)

            # Remaining lines
            title_assigned = False
            for line in block_lines[1:]:
                if not line:
                    continue

                # Catalogue number
                cat = _extract_cat_no(line)
                if cat:
                    rec.catalogue_no = cat
                    continue

                # Inventory number
                inv = _extract_inv_no(line)
                if inv and not rec.inventory_number:
                    rec.inventory_number = inv

                # Dimensions
                if _DIM_RE.search(line) and not rec.height_cm:
                    h, w, d = _parse_dimensions(line)
                    rec.height_cm, rec.width_cm, rec.depth_cm = h, w, d
                    continue

                # Medium
                if _looks_like_medium(line) and not rec.medium_material:
                    rec.medium_material = line
                    continue

                # Collection / lender: lines mentioning "Museum", "Collection",
                # "Sammlung", "Leihgabe", "Courtesy", "Private"
                coll_kw = ("museum", "collection", "sammlung", "leihgabe",
                           "courtesy", "private", "gallery", "galerie",
                           "stiftung", "foundation", "estate")
                if any(kw in line.lower() for kw in coll_kw) and not rec.collection:
                    rec.collection = line
                    continue

                # Year on its own line
                if re.match(r"^\s*\(?\d{4}\)?\s*$", line):
                    if not rec.artwork_inception:
                        rec.artwork_inception = line.strip("() ")
                    continue

                # First unmatched non-empty line → title (may include year)
                if not title_assigned:
                    # Try to strip year from title line
                    year_m = _YEAR_RE.search(line)
                    if year_m and not rec.artwork_inception:
                        rec.artwork_inception = year_m.group(1)
                    rec.artwork_title = line
                    # Mark uncertain titles
                    if not rec.artist_full_name:
                        rec.artwork_title += " [?]"
                    title_assigned = True
                    continue

                leftover_notes.append(line)

            rec.notes = " | ".join(leftover_notes)
            records.append(rec)

    return records


# ---------------------------------------------------------------------------
# CSV output
# ---------------------------------------------------------------------------

def write_csv(records: list[ArtworkRecord], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for rec in records:
            writer.writerow(asdict(rec))
    print(f"[INFO] CSV saved: {path}  ({len(records)} rows)")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    default_txt = Path("output/ocr/baldessari-sprengel_ocr_full.txt")
    default_csv = Path("output/baldessari-sprengel-artworks.csv")

    parser = argparse.ArgumentParser(
        description="Stage 2 - Extract artwork records from OCR text into CSV"
    )
    parser.add_argument(
        "ocr_text",
        nargs="?",
        default=str(default_txt),
        help="Path to the full OCR text file produced by ocr_catalogue.py",
    )
    parser.add_argument("--output", default=str(default_csv), help="Output CSV path")
    parser.add_argument("--exhibition", default="Baldessari. Sprengel Museum Hannover",
                        help="Exhibition title")
    parser.add_argument("--location", default="Sprengel Museum Hannover",
                        help="Exhibition location")
    parser.add_argument("--start", default="", help="Exhibition start date YYYY-MM-DD")
    parser.add_argument("--end", default="", help="Exhibition end date YYYY-MM-DD")
    parser.add_argument("--organizer", default="Sprengel Museum Hannover",
                        help="Exhibition organizer")
    args = parser.parse_args()

    ocr_path = Path(args.ocr_text)
    if not ocr_path.exists():
        print(f"[ERROR] OCR text file not found: {ocr_path}")
        print("        Run ocr_catalogue.py first.")
        sys.exit(1)

    full_text = ocr_path.read_text(encoding="utf-8")

    exhibition_defaults = {
        "exhibition_title": args.exhibition,
        "exhibition_location": args.location,
        "exhibition_start": args.start,
        "exhibition_end": args.end,
        "exhibition_organizer": args.organizer,
    }

    print(f"[INFO] Parsing OCR text: {ocr_path}")
    records = parse_ocr_blocks(full_text, exhibition_defaults)
    print(f"[INFO] Extracted {len(records)} candidate artwork records")

    write_csv(records, Path(args.output))
    print("\nNext steps:")
    print("  1. Review the CSV in a spreadsheet editor.")
    print("  2. Correct OCR errors, fill blanks, remove [?] flags.")
    print("  3. Run scripts/validate_csv.py to check against the data model.")


if __name__ == "__main__":
    main()
