# Catalogue Extraction

Extracts structured artwork metadata from scanned exhibition catalogue PDFs into the project's three data models (Item in Exhibition, Artist, Exhibition), using Tesseract OCR and a local LLM via Ollama.

## Use this: `catalogue-ocr-llm-extraction.ipynb`

The notebook to run on a new catalogue. It is self-documenting: open it, follow the setup table in the first cell, edit the **Parameters** cell (PDF path, artist, exhibition details), and *Run All*.

- **Output:** `<pdf name>-artworks.csv`, with the same columns as `scripts/extract_artworks.py` (the regex pipeline in `../catalogue-ocr.ipynb`), checked with `scripts/validate_csv.py`. There is also a QuickStatements CSV.
- **Review:** rows that need a human check are marked `[?]` in `notes`, with the reason and PDF page, and are listed at the end of the run. The optional review app (below) shows each entry next to its page for correcting.
- **Traceability:** every chunk of OCR text sent to the LLM and every raw reply are saved in `<pdf name>-llm-log.json`.
- **Resumable:** OCR output and finished LLM chunks are reused, so an interrupted run can be restarted.
- **Solo or group shows:** for a solo show, give the artist's name and QID. For a group show, leave them blank, and each entry's artist is matched on Wikidata.
- **Must be run from inside this repository**, because it imports the data-model columns and validator from `scripts/`.

Requirements: Tesseract with the catalogue's language data, poppler (`pdftoppm`), Ollama with `qwen2.5:14b` (about 10 GB of GPU memory; `qwen2.5:7b` on smaller machines), and `pip install beautifulsoup4 lxml`. `aspell` is optional and only used for the OCR quality score.

It can also be run headless with [papermill](https://papermill.readthedocs.io/):

```bash
papermill catalogue-ocr-llm-extraction.ipynb my-catalogue-run.ipynb \
  -p catalogue_pdf /path/to/my-catalogue.pdf \
  -p artist_name "" -p artist_qid "" \
  -p exhibition_title "…" -p exhibition_location "…" -p exhibition_start 2001 -p exhibition_end 2001
```

## Review app: `review_app.py`

A browser app (Gradio) for checking a run's results against the scans. The left pane shows the catalogue page, with each extracted value boxed where it was found. The right pane shows the entry in a form, grouped by where each value came from: the catalogue page (OCR + LLM), Wikidata, or the notebook's parameters. Entries can be edited, added and deleted, and the corrected CSV (`<pdf name>-artworks-reviewed.csv`) downloaded. Nothing is re-run: the app only reads the notebook's output folder (the CSV, the hOCR and the page images in `pages/`). Page images that aren't there are rendered from the PDF, if given.

Needs `pip install gradio pandas pillow`. Start it either:

- **from the notebook:** set `open_review_app = True` in the parameters, or run section 11. The app appears below the cell.
- **from the command line:**

  ```bash
  python review_app.py path/to/my-catalogue-output --pdf path/to/my-catalogue.pdf
  python review_app.py path/to/my-catalogue-output --pdf … --share    # also a public link, valid 72 h
  ```

`--share` (or `share=True` in the notebook) prints a temporary public link that **anyone who has it can open, scan pages included**. Set `REVIEW_APP_PASSWORD` to require a login (user `demo`). With no output folder, the app opens the Baldessari demo (`demo/baldessari-sprengel-artworks.csv`), which needs the June OCR files in `~/projects/datasets/stray_TIB/`, so it only runs on the machine that has them.

## Background: the June 2026 experiments

Three approaches were compared on the Baldessari catalogue (Sprengel Museum, 1999). Their method notes and outputs are in `../scan-2/`.

| Plan | Approach | Notebook |
|---|---|---|
| A | Tesseract ALTO XML, entries found from the layout geometry, then LLM extraction | none (outputs only) |
| B | Tesseract hOCR, overlapping text chunks, then LLM segmentation and extraction | `notebook_plan_b.ipynb` |
| C | Page images straight to a vision-language model, no OCR | `notebook_plan_c.ipynb` |

**Plan B was chosen.** It keeps the OCR text as an inspectable intermediate step, so failures can be traced, and it needs far less compute than Plan C. `catalogue-ocr-llm-extraction.ipynb` is the cleaned-up, general-purpose version of Plan B. The two experiment notebooks are kept as a record.
