# Plan A — ALTO Spatial Segmentation + Ollama CLI Extraction

## Approach summary
Use the ALTO XML output's bounding-box geometry to precisely segment the document into catalog entries vs. prose, then feed each entry block to a text LLM via `ollama run` for structured JSON extraction. Fully local — no external APIs.

## OCR Quality Gate (Step 0)

Before anything else, score the Tesseract output quality programmatically:

```bash
# Check aspell-de is available (needed for German text)
aspell dump dicts | grep de
# If missing: sudo apt install aspell-de aspell-en
```

Script: tokenise `baldessari-sprengel.txt`, run each word through `aspell -l` (list unrecognised words), compute:

```
validity_ratio = (total_words - unknown_words) / total_words
```

**Threshold**: `>= 0.93` → proceed with Plan A. `< 0.93` → consider Chandra-2 re-OCR or switch to Plan C (VLM).

Use both `-l en` and `-l de` passes and take the union of recognised words to handle bilingual text.

---

## Pipeline

### Step 1 — Parse ALTO XML with lxml

ALTO block structure:
```
<TextBlock ID="...">           ← spatial region
  <TextLine>
    <String CONTENT="..." />
  </TextLine>
</TextBlock>
```

Segmentation heuristics (tune on first 10 pages):
- **Catalog entry block**: short height, contains numeric tokens matching dimension patterns (`\d+[\.,]\d+\s*(cm|mm)`), date patterns (`\d{4}`), and material keywords
- **Essay/body text block**: tall block, high word count, no dimension tokens
- **Caption/label block**: single short line, near top or bottom of page

Output: list of text strings, one per candidate catalog entry.

### Step 2 — Structured extraction via `ollama run`

Model: **qwen2.5:14b** (best balance of speed and instruction-following for structured output; upgrade to `gemma3:27b` if results are inconsistent)

```bash
echo "$ENTRY_TEXT" | ollama run qwen2.5:14b \
  "Extract fields from this exhibition catalog entry. Return only valid JSON with these keys:
  title, creator, date, object_type, materials (array), height_cm, width_cm, depth_cm,
  inventory_number, catalog_number, notes.
  Use null for missing fields. Do not invent values."
```

Run in a Python loop, parse JSON response, validate schema, flag `null`-heavy records for manual review.

Temperature: 0 (deterministic). Batch all entries sequentially.

### Step 3 — Local entity resolution

No external APIs. Build a small local lookup JSON:

```json
{
  "creators": {"John Baldessari": "Q312793"},
  "institutions": {"Sprengel Museum": "Q673907", "Sprengel Museum Hannover": "Q673907"},
  "object_types": {"photograph": "Q125191", "painting": "Q3305213", "video": "Q34508", ...},
  "materials": {"acrylic": "Q207849", "gelatin silver print": "Q3286805", ...}
}
```

Fuzzy-match extracted strings against this table (`difflib.get_close_matches`). Unmatched entries stay as plain strings — flagged for later enrichment.

### Step 4 — Output

Write a flat CSV with Wikidata P-number column headers — QuickStatements-compatible for direct Wikibase upload. Also write a human-readable version with field name headers for QA.

Column order: `qid, P31, P1476, P170, P571, P276, P195, P186, P2048, P2049, P2610, P217, P528, P1431`

`P1431` (Exhibited at) is hardcoded to `Q138573075` (the Sprengel Museum exhibition Q-ID) for every record.

Output files: `output-plan-a.csv` (P-headers), `output-plan-a-readable.csv` (field name headers).

---

## Tradeoffs

| | |
|---|---|
| **Strengths** | Highest precision segmentation; explicit reading order from ALTO; easy to debug block classification |
| **Weaknesses** | Layout heuristics need tuning per catalog style; multi-column or rotated text may mis-segment |
| **Model** | qwen2.5:14b (~14B params, 9GB) — already pulled |
| **Speed** | ~2–5 min total for 40 entries on this hardware |
| **Risk** | Poor OCR quality propagates to extraction; ALTO block boundaries may not align with logical entry boundaries |

---

## Verification

1. Run quality gate script → report word validity ratio
2. Run pipeline on pages 10–20 (likely catalog section)
3. Manually compare 5 JSON records against PDF
4. Check JSON-LD structure validates against NFDI4Culture model
