"""
ocr_catalogue.py
----------------
Stage 1 of the catalogue OCR pipeline.

Converts each page of a scanned PDF catalogue into a greyscale TIFF image,
runs Tesseract OCR over it, and saves:
  - per-page plain-text files  -> output_dir/pages/
  - a single concatenated text -> output_dir/<stem>_ocr_full.txt

Dependencies (install via requirements.txt):
    pymupdf, pytesseract, Pillow

No Poppler required – PDF rendering is handled by PyMuPDF.

Tesseract language pack must be installed separately.
  Windows:  https://github.com/UB-Mannheim/tesseract/wiki
  Linux:    sudo apt install tesseract-ocr tesseract-ocr-deu tesseract-ocr-eng

Usage:
    python scripts/ocr_catalogue.py [PDF_PATH] [--output OUTPUT_DIR] [--lang LANG] [--dpi DPI]

    PDF_PATH   Path to the catalogue PDF (default: scans/baldessari-sprengel.pdf)
    --output   Directory for output files (default: output/ocr)
    --lang     Tesseract language string, e.g. deu, eng, deu+eng (default: deu+eng)
    --dpi      Rendering resolution in DPI (default: 300)
    --pages    Page range to OCR, e.g. 1-20 or 5,10,15 (default: all)
"""

import argparse
import sys
import os
from pathlib import Path


def parse_page_range(spec: str, total: int) -> list[int]:
    """Parse a page-range string into a sorted list of 1-based page numbers."""
    pages = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            start_str, end_str = part.split("-", 1)
            start = int(start_str) if start_str else 1
            end = int(end_str) if end_str else total
            pages.update(range(start, end + 1))
        else:
            pages.add(int(part))
    return sorted(p for p in pages if 1 <= p <= total)


def ocr_pdf(
    pdf_path: Path,
    output_dir: Path,
    lang: str = "deu+eng",
    dpi: int = 300,
    page_range: str | None = None,
    tesseract_cmd: str | None = None,
) -> Path:
    """
    OCR a scanned PDF catalogue.

    Parameters
    ----------
    pdf_path   : Path to the input PDF
    output_dir : Root directory for output artefacts
    lang          : Tesseract language string
    dpi           : Rendering DPI (300 is a good minimum for printed text)
    page_range    : Optional page-range string (None = all pages)
    tesseract_cmd : Full path to tesseract.exe if not on system PATH

    Returns
    -------
    Path to the concatenated full-text file.
    """
    try:
        import fitz  # pymupdf
        from PIL import Image
    except ImportError as exc:
        print(f"[ERROR] Missing dependency: {exc}\nRun: pip install pymupdf Pillow")
        sys.exit(1)

    # Tesseract is optional – only needed when PDF has no embedded text layer
    try:
        import pytesseract
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        pytesseract.get_tesseract_version()  # raises TesseractNotFoundError if binary missing
        _tesseract_available = True
    except Exception:
        _tesseract_available = False

    pages_dir = output_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    print(f"[INFO] Opening PDF: {pdf_path}")
    doc = fitz.open(str(pdf_path))
    total = len(doc)
    print(f"[INFO] Total pages: {total}")

    # --- Probe: does the PDF have an embedded text layer? ---
    # Sample up to 5 pages; if they yield substantial text, skip Tesseract.
    probe_pages = list(range(0, min(5, total)))
    probe_chars = sum(len(doc[i].get_text("text")) for i in probe_pages)
    avg_probe = probe_chars / len(probe_pages) if probe_pages else 0
    use_tesseract = avg_probe < 100  # fewer than 100 chars/page => image-only scan

    if use_tesseract:
        print(f"[INFO] PDF appears to be an image scan (avg {avg_probe:.0f} chars/page).")
        if not _tesseract_available:
            print("[ERROR] Tesseract OCR is required but not installed.")
            print("        Install from: https://github.com/UB-Mannheim/tesseract/wiki")
            print("        Then add it to your PATH and re-run.")
            sys.exit(1)
        print(f"[INFO] Using Tesseract OCR at {dpi} DPI …")
        scale = dpi / 72
        mat = fitz.Matrix(scale, scale)
    else:
        print(f"[INFO] PDF has embedded text (avg {avg_probe:.0f} chars/page). Using direct extraction.")

    selected = parse_page_range(page_range, total) if page_range else list(range(1, total + 1))
    print(f"[INFO] Processing {len(selected)} page(s) …")

    full_text_parts: list[str] = []

    for page_num in selected:
        page = doc[page_num - 1]
        page_txt_path = pages_dir / f"page_{page_num:04d}.txt"

        if page_txt_path.exists():
            print(f"  [SKIP] Page {page_num} already processed")
            text = page_txt_path.read_text(encoding="utf-8")
        elif use_tesseract:
            print(f"  [OCR]  Page {page_num}/{total} …", end="", flush=True)
            pix = page.get_pixmap(matrix=mat, colorspace=fitz.csGRAY)
            img_grey = Image.frombytes("L", [pix.width, pix.height], pix.samples)
            text = pytesseract.image_to_string(
                img_grey,
                lang=lang,
                config="--psm 6",  # psm 6 = assume a uniform block of text
            )
            page_txt_path.write_text(text, encoding="utf-8")
            print(" done")
        else:
            print(f"  [TEXT] Page {page_num}/{total} …", end="", flush=True)
            text = page.get_text("text")
            page_txt_path.write_text(text, encoding="utf-8")
            print(" done")

        # Annotate text with a page marker so downstream parsers can locate entries
        full_text_parts.append(f"=== PAGE {page_num} ===\n{text}")

    full_text = "\n\n".join(full_text_parts)
    stem = pdf_path.stem
    full_txt_path = output_dir / f"{stem}_ocr_full.txt"
    full_txt_path.write_text(full_text, encoding="utf-8")
    print(f"\n[INFO] Full OCR text saved: {full_txt_path}")
    return full_txt_path


def main() -> None:
    default_pdf = Path("scans/baldessari-sprengel.pdf")
    default_out = Path("output/ocr")

    parser = argparse.ArgumentParser(
        description="Stage 1 – OCR a scanned PDF exhibition catalogue"
    )
    parser.add_argument("pdf_path", nargs="?", default=str(default_pdf), help="Path to the PDF file")
    parser.add_argument("--output", default=str(default_out), help="Output directory")
    parser.add_argument("--lang", default="deu+eng", help="Tesseract language(s), e.g. deu+eng")
    parser.add_argument("--dpi", type=int, default=300, help="Rendering DPI (default: 300)")
    parser.add_argument("--pages", default=None, help="Page range, e.g. 1-20 or 5,10,15")
    args = parser.parse_args()

    pdf_path = Path(args.pdf_path)
    if not pdf_path.exists():
        print(f"[ERROR] PDF not found: {pdf_path}")
        sys.exit(1)

    ocr_pdf(
        pdf_path=pdf_path,
        output_dir=Path(args.output),
        lang=args.lang,
        dpi=args.dpi,
        page_range=args.pages,
    )


if __name__ == "__main__":
    main()
