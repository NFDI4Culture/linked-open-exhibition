# Linked Open Exhibition

> Helping art exhibitions attract more visitors and enable deeper engagement using Linked Open Data.

**[Website](https://nfdi4culture.github.io/linked-open-exhibition/) · [Learning Exercises](https://en.wikiversity.org/wiki/BIM-126-02-Data-Science-Linked-Open-Exhibition) · [Exhibitions](https://nfdi4culture.github.io/linked-open-exhibition/exhibitions.html) · [Data Analysis](https://nfdi4culture.github.io/linked-open-exhibition/data-analysis.html)**

A prototype pipeline for publishing art exhibition data as **Linked Open Data (LOD)**, developed with students of the Bachelor of Arts Information Management at Hochschule Hannover in the course *BIM-126-02 Data Science (SoSe 2026)*.

The pipeline retrieves exhibition catalogue records from the Deutsche Nationalbibliothek (DNB) SRU API, structures them using an open data model, uploads them to a Wikibase knowledge base, and publishes the results as a Quarto website driven by live SPARQL queries.

---

## The pipeline

```
DNB SRU API → MARC21-XML → CSV → Wikibase → SPARQL → Quarto website
```

| Step | Notebook | Output |
|---|---|---|
| 1. Retrieve DNB records | `catalogues/dnb-jupyter/01_dnb_search.ipynb` | `sprengel_raw/*.xml` |
| 2. Filter & extract fields | `catalogues/dnb-jupyter/02_dnb_filter_exhibitions.ipynb` | `sprengel_exhibitions.csv` |
| 3. Fetch cover images | `catalogues/dnb-jupyter/03_dnb_cover_images.ipynb` | `images/*.jpg` |
| 4. Upload data model | `catalogues/dnb-jupyter/04_wikibase_data_model.ipynb` | Wikibase properties |
| 5. Upload exhibitions | `catalogues/dnb-jupyter/05_wikibase_upload.ipynb` | Wikibase items |
| 6. Upload images | `catalogues/dnb-jupyter/06_mediawiki_upload.ipynb` | MediaWiki files |

Helper notebooks: `00_sparql_health_check.ipynb`, `00_wikibase_bot_test.ipynb`

---

## Getting started

### Requirements

- [Quarto](https://quarto.org/) >= 1.3
- Python >= 3.10 (with virtual environment)

### Install Python dependencies

```bash
python -m venv .venv
.venv/Scripts/activate      # Windows
pip install -r requirements.txt
```

### Configure credentials

Copy `.env.example` to `.env` and fill in your Wikibase credentials:

```bash
cp .env.example .env
```

The `.env` file is gitignored and never committed.

### Build the website

```bash
quarto render
```

Output is written to `docs/` for GitHub Pages. Preview locally with:

```bash
quarto preview
```

---

## Repository structure

| Path | Description |
|---|---|
| `catalogues/dnb-jupyter/` | Jupyter Notebooks: DNB retrieval to Wikibase upload pipeline |
| `catalogues/sprengel_raw/` | Raw MARC21-XML pages from DNB SRU API |
| `catalogues/sprengel_exhibitions.csv` | Filtered, structured exhibition records |
| `catalogues/images/` | DNB cover images (gitignored; fetched at runtime) |
| `WB4R/wikibase_generic_model.csv` | WB4R property/class alignment reference |
| `Documentation/` | Glossary (EN + DE), protocol |
| `Linkedart/` | Linked Art ontology reference files |
| `LIDO/` | Example LIDO XML files |
| `docs/` | Rendered Quarto website (GitHub Pages) |
| `_quarto.yml` | Quarto project configuration |
| `requirements.txt` | Python dependencies |
| `.env.example` | Credentials template |
| `CITATION.cff` | Citation metadata |

---

## Course context

This repository accompanies an eight-session course introducing students to Linked Open Data for GLAM (Galleries, Libraries, Archives, Museums) using Wikimedia Foundation platforms.

| Session | Activity | Status |
|---|---|---|
| 1 | Manual entry of Sprengel Museum exhibitions in **Wikidata** | Done |
| 2 | Added artists, catalogues; AI-assisted SPARQL experiments | Done |
| 3 | Museum visit — Sprengel Museum Hannover (19 March 2026) | Done |
| 4–8 | Quarto website + Jupyter pipeline + SPARQL queries + Wikibase upload | Done |

**Leads:** Simon Worthington (TIB — Leibniz Information Centre for Science and Technology) · Prof. Ina Blümel (Hochschule Hannover; TIB — Leibniz Information Centre for Science and Technology)
**Wikiversity:** https://en.wikiversity.org/wiki/BIM-126-02-Data-Science-Linked-Open-Exhibition

---

## Licences

| Content | Licence |
|---|---|
| Project code, notebooks, documentation | [MIT](LICENSE) |
| Original written content (slides, website text) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| DNB bibliographic metadata | [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) |
| DNB cover images | Publisher-supplied; not redistributed — educational use only |

---

## Citation

See [CITATION.cff](CITATION.cff) or use the **Cite this repository** button on GitHub.

---

## AI attribution

Developed with assistance from **GitHub Copilot** (Claude Sonnet 4.6, April 2026). All AI-generated outputs were reviewed and edited by the project team.