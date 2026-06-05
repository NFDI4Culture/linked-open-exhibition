# Catalogue Extraction Notebooks

These notebooks extract structured artwork metadata (title, creator, date, materials, dimensions, inventory numbers) from exhibition catalogue PDFs and output QuickStatements-compatible CSV for Wikibase upload.

Two extraction strategies are provided. Use Plan B for catalogues with clean OCR; use Plan C when OCR quality is poor or the layout is complex.

## Plans

**Plan B — hOCR Chunked Extraction** (`notebook_plan_b.ipynb`)
Runs Tesseract OCR, reconstructs reading order from hOCR bounding boxes, then feeds 800-word overlapping chunks to a local text LLM (Ollama `qwen2.5:14b`) that segments and extracts artwork records in one pass. Faster and simpler; works well when OCR quality is ≥ 80%.

**Plan C — VLM Direct Extraction** (`notebook_plan_c.ipynb`)
Skips OCR entirely. Sends each page image to a local vision-language model (Ollama `qwen2.5vl:7b` for triage, `qwen3-vl:8b` for extraction). More robust on complex layouts or poor OCR but requires more GPU memory and time.

Detailed methodology for each plan is documented in `../scan-2/`.

## Input files required (not in this repository)

The source PDF and OCR transcript files are not committed to this repository. To run these notebooks you need:

- The catalogue PDF (set `pdf_file` in the parameters cell)
- For Plan B only: the `.hocr` file is generated automatically by the Tesseract cell inside the notebook — you do not need to supply it separately
- For Plan C: no OCR files needed; the notebook works directly from page images

Contact the project maintainers or run the OCR pipeline locally to obtain the source materials.

## System dependencies

Install these before running either notebook:

```bash
# Tesseract and PDF rendering (required by Plan B)
sudo apt-get install tesseract-ocr tesseract-ocr-deu poppler-utils

# Spell-checking quality gate (required by Plan B)
sudo apt-get install aspell aspell-de aspell-en

# Ollama (required by both plans)
# Install from https://ollama.com, then pull the models:
ollama pull qwen2.5:14b          # Plan B text extraction
ollama pull qwen2.5vl:7b         # Plan C triage
ollama pull qwen3-vl:8b          # Plan C extraction
```

Python dependencies are in `../../requirements.txt`. Install with:

```bash
pip install -r ../../requirements.txt
```

## Running the notebooks

1. Open a notebook in JupyterLab or VS Code
2. Edit the **parameters cell** (second cell, tagged `parameters`) — at minimum set `pdf_file` to the path of your PDF
3. Run all cells

The notebooks are also [papermill](https://papermill.readthedocs.io/)-compatible, so you can override parameters from the command line:

```bash
papermill notebook_plan_b.ipynb output.ipynb \
  -p pdf_file "/path/to/catalogue.pdf" \
  -p output_dir "/path/to/output"
```

## Outputs

Both plans write to the directory specified by `output_dir` (defaults to `.`):

| File | Contents |
|------|----------|
| `output-plan-b.csv` | Extracted records with Wikidata P-number headers (QuickStatements-ready) |
| `output-plan-b-readable.csv` | Same records with human-readable field names |
| `output-plan-b-failures.txt` | Chunks where extraction failed |
| `output-plan-c.csv` | QuickStatements-ready CSV (Plan C) |
| `output-plan-c-readable.csv` | Human-readable CSV (Plan C) |
| `output-plan-c-triage.json` | Per-page triage cache (resume-on-interrupt) |
| `output-plan-c-raw.json` | Per-page extraction cache (resume-on-interrupt) |
