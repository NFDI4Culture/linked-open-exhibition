"""
validate_csv.py
---------------
Stage 3 of the catalogue OCR pipeline.

Validates the artwork CSV against the Linked Open Exhibition data models and
prints a quality report. Also flags rows still containing " [?]" markers,
missing required fields, and suspicious dimension values.

Usage:
    python scripts/validate_csv.py [CSV_PATH]

    CSV_PATH  Path to the artwork CSV (default: output/baldessari-sprengel-artworks.csv)
"""

import argparse
import csv
import sys
from pathlib import Path


# Fields that SHOULD be filled for a usable Wikibase import
REQUIRED_FIELDS = [
    "artwork_title",
    "artist_full_name",
    "exhibition_title",
    "exhibition_location",
]

# Fields that ideally have values
RECOMMENDED_FIELDS = [
    "artwork_inception",
    "medium_material",
    "height_cm",
    "width_cm",
    "catalogue_no",
    "collection",
]


def validate(csv_path: Path) -> None:
    with open(csv_path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)

    total = len(rows)
    if total == 0:
        print("[WARN] CSV is empty.")
        return

    print(f"=== Validation Report: {csv_path.name} ===")
    print(f"Total rows: {total}\n")

    missing_required: dict[str, int] = {f: 0 for f in REQUIRED_FIELDS}
    missing_recommended: dict[str, int] = {f: 0 for f in RECOMMENDED_FIELDS}
    uncertain_rows: list[int] = []
    dim_issues: list[int] = []

    for i, row in enumerate(rows, start=2):  # row 1 = header
        # Missing required
        for field in REQUIRED_FIELDS:
            if not row.get(field, "").strip():
                missing_required[field] += 1

        # Missing recommended
        for field in RECOMMENDED_FIELDS:
            if not row.get(field, "").strip():
                missing_recommended[field] += 1

        # Uncertain flags
        for val in row.values():
            if "[?]" in val:
                uncertain_rows.append(i)
                break

        # Dimension sanity check
        for dim_field in ("height_cm", "width_cm"):
            val = row.get(dim_field, "").strip()
            if val:
                try:
                    num = float(val)
                    if num <= 0 or num > 5000:
                        dim_issues.append(i)
                        break
                except ValueError:
                    dim_issues.append(i)
                    break

    # --- Report ---
    print("Required fields – missing values:")
    for field, count in missing_required.items():
        pct = count / total * 100
        status = "OK" if count == 0 else ("WARN" if pct < 20 else "ERROR")
        print(f"  [{status:5}] {field:<30} {count:>4}/{total} ({pct:.0f}% missing)")

    print("\nRecommended fields – missing values:")
    for field, count in missing_recommended.items():
        pct = count / total * 100
        status = "OK" if count == 0 else ("INFO" if pct < 50 else "WARN")
        print(f"  [{status:5}] {field:<30} {count:>4}/{total} ({pct:.0f}% missing)")

    print(f"\nRows with [?] uncertain markers : {len(uncertain_rows)}")
    if uncertain_rows:
        print(f"  Row numbers: {uncertain_rows[:20]}" + (" …" if len(uncertain_rows) > 20 else ""))

    print(f"\nRows with dimension anomalies   : {len(dim_issues)}")
    if dim_issues:
        print(f"  Row numbers: {dim_issues[:20]}" + (" …" if len(dim_issues) > 20 else ""))

    # Overall quality score
    required_ok = sum(1 for v in missing_required.values() if v == 0)
    score = required_ok / len(REQUIRED_FIELDS) * 100
    print(f"\nQuality score (required fields complete): {score:.0f}%")
    if score == 100 and len(uncertain_rows) == 0:
        print("==> Data looks clean. Ready to proceed to XML/Wikibase import.")
    else:
        print("==> Manual review recommended before XML/Wikibase import.")


def main() -> None:
    default_csv = Path("output/baldessari-sprengel-artworks.csv")
    parser = argparse.ArgumentParser(description="Stage 3 - Validate artwork CSV")
    parser.add_argument("csv_path", nargs="?", default=str(default_csv))
    args = parser.parse_args()

    path = Path(args.csv_path)
    if not path.exists():
        print(f"[ERROR] File not found: {path}")
        sys.exit(1)

    validate(path)


if __name__ == "__main__":
    main()
