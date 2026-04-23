# Project Protocol & Work Log

**Project:** Linked Open Exhibition  
**Repository:** [NFDI4Culture/linked-open-exhibition](https://github.com/NFDI4Culture/linked-open-exhibition)  
**Course:** BIM-126-02 Data Science, SoSe 2026 — Hochschule Hannover  
**Leads:** Simon Worthington (TIB); Prof. Ina Blümel (Hochschule Hannover)  
**AI tooling:** GitHub Copilot (Claude Sonnet 4.6)

---

## Purpose of this document

This file records all significant work carried out on the repository — decisions made, files created or modified, and issues encountered. It is updated as work progresses and is intended to give any contributor a clear overview of the project's history.

---

## Work Log

### 2026-04-22

#### Documentation — Glossary

- **Created** `Documentation/glossary.md` — a full glossary of terms and acronyms used across the project, covering:
  - Protocols & standards: SRU, CQL, MARC21, RDF, SPARQL, JSON-LD, OWL, XML, IRI/URI
  - Data models & ontologies: CIDOC-CRM, Linked Art, WB4R, LIDO, FOAF, GND
  - Platforms & tools: DNB, DNB Library Lab, Wikidata, Wikibase, MediaWiki, Wikimedia Commons, Wikiversity, GitHub Pages, Quarto, JupyterLite
  - APIs & libraries: DNB SRU API, Lobid-GND, SPARQLWrapper, wikibaseintegrator, mwclient, python-dotenv
  - Project-specific terms: GLAM, NFDI4Culture, BIM-126-02, WB4R, Sprengel Museum, IDN, QID, CC0, CC BY-SA 4.0

- **Updated** `Documentation/glossary.md` — expanded SRU entry with full DNB-specific details (endpoint URL, SRU 1.1, pagination behaviour, CC0 access terms).

- **Updated** `Documentation/glossary.md` — expanded QID entry to explain why the `Q` prefix was used (arbitrary choice by Wikidata developers to distinguish items from properties `P` and lexemes `L`; no semantic meaning; stable and language-neutral).

---

#### Wikibase Bot Test Notebook

- **Created** `catalogues/dnb-jupyter/00_wikibase_bot_test.ipynb` — a standalone notebook for testing a Wikibase bot account against the project instance at `https://wikibase.wbworkshop.tibwiki.io/`. Includes:
  - Prerequisites: how to create a bot password at `Special:BotPasswords`
  - Cell 1: install `wikibaseintegrator` and `python-dotenv`
  - Cell 2: load credentials from `.env`
  - Cell 3: configure `wikibaseintegrator` endpoints and log in
  - Cell 4: read test — fetch item `Q1`
  - Cell 5: write test — create a labelled temporary item
  - Cell 6: clean-up — delete the test item via the MediaWiki Action API
  - Troubleshooting table (common errors, causes, fixes)

- **Added** Part 2 cell to `00_wikibase_bot_test.ipynb` — brief explanations of `.env` files and `.gitignore`, with links to GeeksforGeeks guides.

---

#### Credentials & Version Control

- **Created** `.env.example` (repository root) — template for bot/MediaWiki credentials with all required keys (`WB_URL`, `WB_USER`, `WB_PASSWORD`, `MW_URL`, `MW_USER`, `MW_PASSWORD`) and inline comments explaining format.

- **Updated** `.gitignore` — added `.env` to prevent credentials from being committed.

---

#### PLAN.md Execution — Full Pipeline

Executed all phases of `PLAN.md` (DNB → Wikibase → Quarto Website pipeline):

**Phase 1 — Project Setup**

| File | Action |
|---|---|
| `requirements.txt` | Created with 8 Python dependencies: `requests`, `pandas`, `lxml`, `beautifulsoup4`, `wikibaseintegrator`, `mwclient`, `python-dotenv`, `SPARQLWrapper` |
| `_quarto.yml` | Converted output format from `revealjs` to `html`; added `website:` block with navbar (Home / Exhibitions / Data Analysis / About) and page footer |
| `index.qmd` | Replaced RevealJS slide content with a Quarto website homepage: project description, pipeline overview table, navigation links, live Wikidata SPARQL timeline iframe |
| `.gitignore` | Extended with: `catalogues/images/`, `catalogues/sprengel_raw/`, generated CSVs, `wikibase_property_map.json` |

**Phase 2 — DNB Data Retrieval Notebooks**

| Notebook | Purpose | Output |
|---|---|---|
| `catalogues/dnb-jupyter/01_dnb_search.ipynb` | SRU query to DNB API; paginated retrieval; saves raw MARC21-XML | `catalogues/sprengel_raw/page_NNN.xml` |
| `catalogues/dnb-jupyter/02_dnb_filter_exhibitions.ipynb` | Parse MARC21-XML; filter by `Ausstellungskatalog`; extract IDN, title, year, ISBN, URL, subjects; clean year field | `catalogues/sprengel_exhibitions.csv` |
| `catalogues/dnb-jupyter/03_dnb_cover_images.ipynb` | Download cover images via DNB enrichment API; includes rights disclaimer | `catalogues/images/{IDN}.jpg` (gitignored) |

**Phase 3 — Wikibase Data Model**

| Notebook | Purpose | Output |
|---|---|---|
| `catalogues/dnb-jupyter/04_wikibase_data_model.ipynb` | Define and upload minimal exhibition data model (properties + item classes) to Wikibase; idempotent (checks for existing entities before creating) | `catalogues/wikibase_property_map.json` |

Data model created:
- **Properties:** instance of, title, start date, end date, location, GND ID, DNB IDN, exhibition catalogue
- **Item classes:** Exhibition, Exhibition Catalogue, Sprengel Museum Hannover

**Phase 4 — Wikibase & MediaWiki Upload**

| Notebook | Purpose |
|---|---|
| `catalogues/dnb-jupyter/05_wikibase_upload.ipynb` | Create one Wikibase item per CSV row; idempotent via SPARQL DNB IDN lookup; adds statements for type, location, dates, DNB IDN |
| `catalogues/dnb-jupyter/06_mediawiki_upload.ipynb` | Upload cover images to MediaWiki via `mwclient`; adds file description pages; links images back to Wikibase items |

**Phase 5 — Quarto Website Pages**

| File | Content |
|---|---|
| `exhibitions.qmd` | Live SPARQL query against Wikibase; renders results as linked HTML table |
| `data-analysis.qmd` | Pipeline walkthrough; year distribution chart; notebook index table |
| `about.qmd` | Licences (CC0 for DNB data, CC BY-SA 4.0 for project content); AI attribution; full credits; technical stack |

---

#### Documentation — Protocol

- **Created** `Documentation/protocol.md` (this file) — project protocol and running work log.

---

## Decisions log

| Date | Topic | Decision |
|---|---|---|
| 2026-04-22 | Quarto format | Converted from RevealJS slides to full website (`html` format) |
| 2026-04-22 | Credentials | `.env` via `python-dotenv`; `.env.example` committed; `.env` gitignored |
| 2026-04-22 | Cover images | Fetched at runtime, not committed; gitignored `catalogues/images/` |
| 2026-04-22 | DNB data licence | CC0 1.0 Universal — documented in `about.qmd` |
| 2026-04-22 | AI attribution | GitHub Copilot (Claude Sonnet 4.6) credited in all documentation and notebooks |
| 2026-04-22 | Idempotency | Notebooks 04 and 05 check for existing entities before creating, preventing duplicates |
| 2026-04-22 | Wikibase instance | Temporary: `https://wikibase.wbworkshop.tibwiki.io/` — permanent URL TBD |

---

## Known issues & next steps

- [ ] Run notebooks 01–06 end-to-end in the `.venv` environment to verify the pipeline executes without errors
- [ ] Verify Wikibase property IDs after running Notebook 04 and confirm `wikibase_property_map.json` is correct
- [ ] Add an `image` property to the data model in Notebook 04 so Notebook 06 can link images
- [ ] Test `quarto render` locally and confirm GitHub Pages deployment from `docs/`
- [ ] Replace temporary Wikibase instance URL with a permanent one when available — update `WB_URL` in `.env`
- [ ] Add course session notes from Sessions 4–8 as they are completed

---

*This protocol is maintained by the project team. Update this file after each significant work session.*
