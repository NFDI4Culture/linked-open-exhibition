# Plan B — hOCR Chunked Reading + Combined Segmentation & Extraction

## Approach summary
Use the hOCR output (HTML with embedded word coordinates) to reconstruct reading order, then feed document chunks to a text LLM via `ollama run` that handles **both segmentation and extraction in one pass** — no separate geometry-based classifier. Simpler pipeline, trades spatial precision for flexibility.

## OCR Quality Gate (Step 0)

Same aspell-based word validity check as Plan A:

```
validity_ratio = recognised_words / total_words  (aspell -l en + -l de union)
```

Threshold: `>= 0.80` proceed. Below that: consider Chandra-2 or Plan C.

---

## Pipeline

### Step 1 — Reconstruct reading order from hOCR

Parse `baldessari-sprengel.hocr` with BeautifulSoup. hOCR encodes each word with:
```html
<span class='ocrx_word' title='bbox 120 340 210 360'>Acrylic</span>
```

Reconstruct page text in reading order (sort by y-then-x bbox), preserving paragraph breaks where vertical gap between lines exceeds a threshold. Output: plain text per page, with page boundary markers.

Advantage over ALTO: hOCR is standard HTML; no custom XML namespace handling needed.

### Step 2 — Chunk the document

Split reconstructed text into overlapping chunks of ~800 tokens (roughly 2–3 pages). Each chunk passed to the LLM with a dual instruction:

```
"In the following text from an exhibition catalog, identify any artwork entries
(catalog items with title, date, materials, dimensions) and extract each one as JSON.
Ignore essay prose. Return a JSON array — one object per artwork found, or [] if none.

Fields: title, creator, date, object_type, materials[], height_cm, width_cm, depth_cm,
inventory_number, catalog_number.

Text:
<CHUNK>
"
```

Model: **qwen2.5:14b** or **qwen2.5:32b** (the larger model is better at not hallucinating entries from prose).

```bash
echo "$CHUNK_TEXT" | ollama run qwen2.5:32b "<prompt above>"
```

Overlap between chunks (100-token overlap) catches entries that straddle chunk boundaries. Deduplicate by `(title, catalog_number)` after all chunks processed.

### Step 3 — Local entity resolution

Same local lookup JSON as Plan A (no external APIs). Fuzzy match with `difflib`.

### Step 4 — Output

Write a flat CSV with Wikidata P-number column headers — QuickStatements-compatible for direct Wikibase upload. Also write a human-readable version with field name headers for QA.

Column order: `qid, P31, P1476, P170, P571, P276, P195, P186, P2048, P2049, P2610, P217, P528, P1431`

`P1431` (Exhibited at) is hardcoded to `Q138573075` (the Sprengel Museum exhibition Q-ID) for every record.

Output files: `output-plan-b.csv` (P-headers), `output-plan-b-readable.csv` (field name headers).

---

## Tradeoffs

| | |
|---|---|
| **Strengths** | No geometry tuning needed; LLM tolerates minor OCR errors naturally ("heals" garbled tokens in context); handles non-standard layouts gracefully |
| **Weaknesses** | LLM may miss entries or fabricate them from essay prose (hallucination risk); harder to debug than geometric segmentation; slower if using qwen2.5:32b (19GB) |
| **Model** | qwen2.5:14b (fast) or qwen2.5:32b (more reliable — already pulled) |
| **Speed** | ~5–15 min depending on model size and chunk count |
| **Risk** | Hallucination of non-existent catalog entries from essay passages; duplicate detection logic needed |

## Compared to Plan A

- **Simpler** to implement (no ALTO lxml parsing or geometry heuristics)
- **More robust** to OCR errors and unusual layouts
- **Less precise** — segmentation depends entirely on LLM judgment
- **Better choice** if the catalog mixes entries and essay text on the same pages (no clean layout separation)

---

## Verification

1. Run quality gate → word validity ratio
2. Run chunked extraction on pages 10–20
3. Cross-reference all found entries against a manual count of artworks in the catalog
4. Check for fabricated entries (titles not in PDF)
5. Validate JSON-LD structure
