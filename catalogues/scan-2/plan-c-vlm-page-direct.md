# Plan C — Direct VLM on Page Images (No OCR Text)

## Approach summary
Skip the Tesseract text entirely. Feed the already-generated page PNGs (`baldessari-sprengel_pages/`) directly to a vision-language model via `ollama run` — one page at a time. The VLM reads layout, typography, and content simultaneously, bypassing OCR error propagation. Best fit if Tesseract output quality is poor or layout is complex.

No OCR quality gate needed — this plan is the fallback for when OCR fails.

---

## Model selection

Available vision models (already pulled):

| Model | Size | Notes |
|---|---|---|
| **qwen2.5vl:7b** | 6.0 GB | Fastest; good at structured document reading |
| **qwen3-vl:8b** | 6.1 GB | Newer Qwen VL; stronger instruction-following |
| **llama3.2-vision:11b** | 7.8 GB | Strong general vision; slightly slower |
| llava:13b | 8.0 GB | Older architecture; less reliable for structured output |

**Recommended**: `qwen3-vl:8b` (newest, strong document understanding) with `qwen2.5vl:7b` as faster fallback for pages with simple layout.

---

## Pipeline

### Step 1 — Page triage (fast pre-pass)

Not all 67 pages contain catalog entries. Run a lightweight VLM triage pass to classify each page:

```bash
ollama run qwen2.5vl:7b \
  "Does this page contain structured artwork catalog entries (with title, date, materials, dimensions)?
   Reply with exactly one word: YES or NO." \
  --image baldessari-sprengel_pages/page-01.png
```

This is fast (small prompt, binary output). Produces a list of "catalog pages" to process fully. Discard essay/image-only pages.

### Step 2 — Per-page structured extraction

For each page flagged YES:

```bash
ollama run qwen3-vl:8b \
  "Extract all artwork catalog entries visible on this page. Return a JSON array.
   Each entry: {title, creator, date, object_type, materials[], height_cm, width_cm,
   depth_cm, inventory_number, catalog_number}.
   Use null for fields not visible. Do not invent values. Return [] if no entries found." \
  --image baldessari-sprengel_pages/page-XX.png
```

Run sequentially in a shell loop over the flagged pages. Parse JSON response per page, accumulate records.

### Step 3 — Deduplication & merge

Some entries may span two pages (e.g. entry starts on page N, dimensions listed on page N+1). Detect by matching `catalog_number` or `title` across adjacent pages and merging fields.

### Step 4 — Local entity resolution

Same local lookup JSON as Plans A/B (no external APIs). Fuzzy match creator names, material terms, object types to Q-IDs.

### Step 5 — Output

Write a flat CSV with Wikidata P-number column headers — QuickStatements-compatible for direct Wikibase upload. Also write a human-readable version with field name headers for QA.

Column order: `qid, P31, P1476, P170, P571, P276, P195, P186, P2048, P2049, P2610, P217, P528, P1431`

`P1431` (Exhibited at) is hardcoded to `Q138573075` (the Sprengel Museum exhibition Q-ID) for every record.

Output files: `output-plan-c.csv` (P-headers), `output-plan-c-readable.csv` (field name headers).

---

## Tradeoffs

| | |
|---|---|
| **Strengths** | No OCR error propagation; handles complex typography, multi-column, mixed scripts natively; sees the actual page layout; no geometry tuning |
| **Weaknesses** | Slower than text-based approaches (~10–30s per page); VLM may misread small text or unusual fonts; harder to batch; page-spanning entries need cross-page merge logic |
| **Model** | qwen3-vl:8b (6.1GB) — already pulled |
| **Speed** | ~10–30s per page × ~30 catalog pages = 5–15 min |
| **Risk** | VLM hallucination on dense pages; small dimension numbers (e.g. "27.3 × 19.1 cm") may be mis-read |

## When to choose this plan

- Tesseract word validity ratio < 0.93 (OCR quality is poor)
- PDF appears to be a scan rather than born-digital
- Layout is highly complex (full-bleed images, wrapped captions, non-linear reading order)
- You want to avoid Chandra-2 dependency for now

## Compared to Plans A & B

- **No OCR dependency** — completely bypasses the Tesseract output
- **Most robust to layout complexity** — VLM sees the page as a human would
- **Slowest** and most GPU-bound of the three
- **Best for scanned/complex documents**; Plans A/B are better for clean born-digital catalogs

---

## Verification

1. Manual spot-check: compare VLM output for 5 pages against the PDF visually
2. Confirm no hallucinated entries (titles not on the page)
3. Check dimension accuracy (common VLM failure point — small numbers)
4. Validate JSON-LD structure against NFDI4Culture model
