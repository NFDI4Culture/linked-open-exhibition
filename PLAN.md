# Plan: Sprengel Museum Exhibition Pipeline
## DNB → Wikibase → Quarto Website

> **Generated with:** GitHub Copilot (Claude Sonnet 4.6), April 2026  
> **Project:** Linked Open Exhibition — NFDI4Culture / Hochschule Hannover (BIM-126-02)  
> **Contact:** Simon Worthington <simon.worthington@tib.eu>

---

## Overview

This plan describes a fully-documented, student-reproducible Python pipeline for the Sprengel Museum Hannover exhibition project. The goal is to:

1. Retrieve exhibition catalogue records from the Deutsche Nationalbibliothek (DNB) SRU API
2. Filter and parse records relating to Sprengel Museum exhibitions
3. Design and upload a minimal data model to an online Wikibase instance
4. Upload exhibition metadata records to Wikibase via a bot interface
5. Fetch and upload DNB cover images to the accompanying MediaWiki
6. Publish a Quarto **website** to GitHub Pages: each page is a Jupyter Notebook that executes SPARQL queries against the Wikibase endpoint at runtime to retrieve and render exhibition data

Each step is implemented as a standalone Jupyter Notebook with student-facing documentation, explanations of what the code does, licence information, and AI attribution.

---

## Preliminary Work

This pipeline builds on preliminary work carried out in the course **BIM-126-02 Data Science** (SoSe 2026, Hochschule Hannover — Worthington/Blümel), documented on Wikiversity:

> **https://en.wikiversity.org/wiki/BIM-126-02-Data-Science-Linked-Open-Exhibition**

The course is an 8-session introduction to Linked Open Data for GLAM using Wikimedia Foundation platforms (Wikidata, Wikibase, MediaWiki, Wikimedia Commons).

### Completed sessions (as of April 2026)

| Session | Activity | Status |
|---|---|---|
| 1 | Students created minimal exhibition entries in **Wikidata** (title, museum, dates, curator, artist, website) | ✅ Done |
| 2 | Added artists, exhibition catalogues (from DNB/Sprengel shop), and performed AI LLM SPARQL experiments | ✅ Done |
| 3 | Museum visit — Sprengel Museum Hannover (19 March 2026); explored use cases for prototype | ✅ Done |
| 4–8 | Prototyping: Quarto website + Jupyter Notebooks + SPARQL queries; data model development | 🔄 In progress |

### Key outputs from preliminary sessions

- Wikidata items for Sprengel Museum exhibitions — see example: https://www.wikidata.org/wiki/Q138547468
- Wikidata items for exhibition catalogues — see example: https://www.wikidata.org/wiki/Q138646145
- Wikidata query examples: timeline (https://w.wiki/J8NJ), graphed (https://w.wiki/J8aS), map of artists (https://w.wiki/JPT3)
- Minimal data model for exhibitions (properties: P31, P1476, P276, P580, P582, P1640, P710, P856)
- Prototype Quarto repo for students: https://github.com/mrchristian/prototype

### Relationship to this pipeline

The present pipeline automates what students did manually in sessions 1–3 using the **DNB SRU API** as source instead of manual entry, targets the **project Wikibase instance** rather than public Wikidata, and produces a **Quarto website driven by Jupyter Notebooks with SPARQL queries** following the approach introduced in session 4.

---

## Key Decisions

| Topic | Decision |
|---|---|
| Credentials | `.env` file via `python-dotenv`; `.env.example` committed; `.env` gitignored |
| Images | DNB cover images API (retrieved at runtime, not redistributed in repo) |
| Quarto format | Full **website** replacing the existing RevealJS slides |
| Wikibase data model | Minimal exhibition model referencing WB4R property names/IDs |
| DNB metadata licence | **CC0 1.0 Universal** — documented in `about.qmd` |
| AI attribution | GitHub Copilot (Claude Sonnet 4.6) credited in all documentation |

---

## Repository File Map

### Files to Modify

| File | Change |
|---|---|
| `_quarto.yml` | Convert project type from `revealjs` to `website`; add navbar |
| `index.qmd` | Replace slide content with website homepage |

### Files to Create

```
requirements.txt
.env.example

# Quarto website pages
exhibitions.qmd
data-analysis.qmd
about.qmd

# New documented notebooks
catalogues/dnb-jupyter/01_dnb_search.ipynb
catalogues/dnb-jupyter/02_dnb_filter_exhibitions.ipynb
catalogues/dnb-jupyter/03_dnb_cover_images.ipynb
catalogues/dnb-jupyter/04_wikibase_data_model.ipynb
catalogues/dnb-jupyter/05_wikibase_upload.ipynb
catalogues/dnb-jupyter/06_mediawiki_upload.ipynb
```

### Existing Reference Files

| File | Role |
|---|---|
| `WB4R/wikibase_generic_model.csv` | Property/class alignment reference |
| `catalogues/dnb-jupyter/DNB_SRU_Einstieg.ipynb` | Existing SRU API pattern (JupyterLite/pyodide — not reused directly) |
| `timeline.py` | Existing Wikidata SPARQL pattern for exhibitions |

---

## Python Dependencies (`requirements.txt`)

```
requests
pandas
lxml
beautifulsoup4
wikibaseintegrator
mwclient
python-dotenv
SPARQLWrapper
```

---

## Phase 1 — Project Setup

*Steps are independent and can be done in parallel.*

1. **Create `requirements.txt`** with the libraries listed above.
2. **Create `.env.example`** with the following keys (no real values committed):
   ```
   WB_URL=https://wikibase.wbworkshop.tibwiki.io
   WB_USER=your-bot-username
   WB_PASSWORD=your-bot-password
   MW_URL=https://wikibase.wbworkshop.tibwiki.io
   MW_USER=your-mediawiki-username
   MW_PASSWORD=your-mediawiki-password
   ```
3. **Update `.gitignore`** to ensure `.env` is excluded.
4. **Modify `_quarto.yml`** — change project type to `website`, add a top-level navbar linking: Home / Exhibitions / Data Analysis / About. Keep `output-dir: docs` for GitHub Pages compatibility.

---

## Phase 2 — DNB Data Retrieval Notebooks

*Notebooks run sequentially: 01 → 02 → 03.*

### Notebook 01 — `01_dnb_search.ipynb`

**Purpose:** Retrieve all DNB records related to Sprengel Museum and save raw data.

**Documentation covers:**
- What the SRU protocol is (Search/Retrieve via URL, Library of Congress standard)
- CQL (Contextual Query Language) query syntax
- DNB SRU endpoint: `https://services.dnb.de/sru/dnb`
- Free, no-registration access terms
- **DNB data licence: CC0 1.0 Universal**
- Pagination: 100 records per request, `startRecord` parameter for continuation

**Key queries:**
```
KOR="Sprengel Museum"
KOR="Sprengel Museum" and SWW="Ausstellungskatalog"
```

**Output:** `catalogues/sprengel_raw.xml` (one file per page of results)

---

### Notebook 02 — `02_dnb_filter_exhibitions.ipynb`

**Purpose:** Parse MARC21-XML, filter for exhibition catalogues, extract structured fields.

**Documentation covers:**
- MARC21 field structure (control fields, data fields, subfields)
- How to identify exhibition catalogues (subject heading `SWW=Ausstellungskatalog`, DNB classification)
- Fields extracted:

| MARC21 Field | Subfield | Meaning |
|---|---|---|
| `001` | — | IDN (unique record ID) |
| `245` | `a` | Title |
| `264` or `260` | `c` | Publication year |
| `689` | `a` | Subject headings |
| `856` | `u` | URL / link |
| `020` | `a` | ISBN |

**Output:** `catalogues/sprengel_exhibitions.csv`

---

### Notebook 03 — `03_dnb_cover_images.ipynb`

**Purpose:** Retrieve cover images from the DNB catalogue enrichment API.

**Documentation covers:**
- DNB cover image URL pattern: `https://portal.dnb.de/opac/mvb/cover?isbn={ISBN}`
- Cover images are **not** CC0 — they are publisher-supplied. Images are fetched at runtime for educational display only and **must not be redistributed** in the repository.
- Images saved locally to `catalogues/images/{IDN}.jpg` for temporary use during upload
- A disclaimer cell is included in the notebook

**Output:** `catalogues/images/*.jpg` (gitignored)

---

## Phase 3 — Wikibase Data Model

*Depends on Phase 1 (credentials). Independent of Phase 2.*

### Notebook 04 — `04_wikibase_data_model.ipynb`

**Purpose:** Define and upload a minimal exhibition data model to the online Wikibase instance.

**Documentation covers:**
- What Wikibase is and how it differs from Wikidata
- The WB4R (Wikibase 4 Research) generic model and this project's alignment with it
- CIDOC-CRM equivalences for each property
- How to use `wikibaseintegrator` for creating properties and items
- Idempotency: checking whether a property/item already exists before creating it

**Minimal data model:**

#### Item Classes (Q items)

| Label | Description | WB4R equivalent |
|---|---|---|
| Exhibition | A temporary display of artworks | event (WB4R) |
| Exhibition Catalogue | A publication accompanying an exhibition | bibliographic_work (WB4R Q14) |
| Sprengel Museum Hannover | The museum in Hannover | place |

#### Properties (P items)

| Label | Data type | WB4R ref | CIDOC-CRM |
|---|---|---|---|
| instance of | Item | P1 | E55 Type |
| title | Monolingual text | P4 | E35 Title |
| start date | Time | P10 | P82a |
| end date | Time | P11 | P82b |
| location | Item | P38 | P53 |
| GND ID | External identifier | P102 | — |
| DNB IDN | External identifier | new | — |
| image | Commons media | new | — |
| exhibition catalogue | Item | P5 (has_part) | P46 |

**Output:** `catalogues/wikibase_property_map.json` — maps property labels to Wikibase P-IDs on the online instance

---

## Phase 4 — Wikibase Upload

*Depends on Phase 2 (CSV) and Phase 3 (property map). Run 05 before 06.*

### Notebook 05 — `05_wikibase_upload.ipynb`

**Purpose:** Create one Wikibase item per exhibition record from the CSV.

**Documentation covers:**
- Loading `wikibase_property_map.json` to get correct local P-IDs
- Creating items with `wikibaseintegrator`
- Idempotency strategy: search for existing item by DNB IDN before creating
- Adding statements: title, dates, location, GND ID, DNB IDN
- Recording data provenance (DNB as source, CC0 licence as qualifier)

---

### Notebook 06 — `06_mediawiki_upload.ipynb`

**Purpose:** Upload cover images to the MediaWiki instance accompanying Wikibase.

**Documentation covers:**
- `mwclient` library and MediaWiki file upload API
- File naming convention: `Sprengel_Exhibition_{IDN}.jpg`
- Adding a file description page with: source (DNB), date fetched, copyright notice
- Linking the uploaded file to the corresponding Wikibase item via the `image` property

---

## Phase 5 — Quarto Website

*Depends on Phase 1 (Quarto config). Can be previewed before Phase 4 is complete using static/mock data.*

### `index.qmd` (replace)

Project homepage: introduction to the Sprengel Museum Hannover, the goal of the project, links to the exhibitions timeline and data-analysis notebooks. Credits section.

### `exhibitions.qmd`

Chronological exhibition timeline page, implemented as a **Jupyter Notebook** executed by Quarto at render time.
- Executes a SPARQL query against the online Wikibase SPARQL endpoint (`https://wikibase.wbworkshop.tibwiki.io/query/sparql`) to retrieve all Exhibition items
- Renders a sortable table of exhibitions with: title, date range, link to DNB record, cover thumbnail
- SPARQL query and results displayed inline so students can follow the data flow
- **Note on endpoint:** The current temporary instance is at `https://wikibase.wbworkshop.tibwiki.io`. This will be replaced with a permanent URL at a later date — update `WB_URL` in `.env` when migrating.
- *Approach matches the prototype pattern from Session 4 of BIM-126-02: SPARQL query → Jupyter Notebook → Quarto HTML render (see: https://github.com/mrchristian/prototype)*

### `data-analysis.qmd`

Data analysis page implemented as a **Jupyter Notebook** executed by Quarto.
- Executes SPARQL queries against the Wikibase endpoint to retrieve and analyse the full exhibition dataset
- Embeds Notebooks 01–02 (DNB retrieval and filtering) as Quarto executable documents, allowing students to follow the full pipeline from DNB raw data → Wikibase → rendered publication

### `about.qmd`

Full credits and licence page, including:

#### DNB Data Licence

> All bibliographic metadata retrieved from the Deutsche Nationalbibliothek (DNB) SRU interface is released under the **Creative Commons Zero 1.0 Universal (CC0 1.0)** public domain dedication.  
> Source: [dnb.de/metadataservice](https://www.dnb.de/EN/Professionell/Metadatendienste/metadatendienste_node.html)  
> The SRU interface is freely accessible without registration.

#### Cover Image Terms

> Cover images retrieved via the DNB catalogue enrichment API are supplied by publishers and are **not** covered by the CC0 licence. They are used here solely for educational/non-commercial identification purposes and are not redistributed in this repository. Always verify image rights before reuse.

#### AI Attribution

> This project was developed with the assistance of **GitHub Copilot** using the **Claude Sonnet 4.6** model (April 2026). AI assistance was used for code generation, documentation drafting, data model design, and planning. All outputs were reviewed and edited by the project team.

#### Project Credits

> Project: Linked Open Exhibition Prototype  
> Course: BIM-126-02 Data Science, Hochschule Hannover  
> Lead: Simon Worthington (TIB — Leibniz Information Centre for Science and Technology)  
> Repository licence: CC BY-SA 4.0

---

## DNB Search Reference

| Query | Purpose |
|---|---|
| `KOR="Sprengel Museum"` | All records with Sprengel Museum as corporate name |
| `KOR="Sprengel Museum" and SWW="Ausstellungskatalog"` | Narrow to exhibition catalogues |
| Base URL | `https://services.dnb.de/sru/dnb` |
| Format | `recordSchema=MARC21-xml` |
| Pagination | `maximumRecords=100`, `startRecord=101, 201, …` |

---

## Verification Checklist

- [ ] `quarto preview` renders the website locally without errors
- [ ] `requirements.txt` installs cleanly in a fresh virtual environment
- [ ] `01_dnb_search.ipynb` returns records containing "Sprengel Museum" titles from DNB
- [ ] `sprengel_exhibitions.csv` contains valid parseable date values
- [ ] `04_wikibase_data_model.ipynb` creates properties on the online Wikibase instance without duplicate errors
- [ ] `05_wikibase_upload.ipynb` creates Exhibition items visible in the Wikibase UI
- [ ] `06_mediawiki_upload.ipynb` uploads images visible in MediaWiki
- [ ] `exhibitions.qmd` renders a populated timeline in the Quarto output
- [ ] `quarto render` produces a deployable `docs/` folder
- [ ] Push to `main` branch triggers GitHub Pages deployment

---

## Important Notes for Students

1. **Never commit your `.env` file.** It contains passwords. Use `.env.example` as a template.
2. **Run notebooks in order** within each phase (01 → 02 → 03, then 04, then 05 → 06).
3. **DNB rate limiting:** The SRU interface is free but should not be hammered. The notebooks include `time.sleep()` calls between paginated requests.
4. **Wikibase credentials** for the online instance at `https://wikibase.wbworkshop.tibwiki.io` are required before running notebooks 04–06. A more permanent Wikibase instance will be provided at a later date — update `WB_URL` in `.env` when this changes.
5. **Cover images are not stored in git.** The `catalogues/images/` directory is gitignored. Re-run notebook 03 to recreate them locally.

---

*Last updated: April 2026*
