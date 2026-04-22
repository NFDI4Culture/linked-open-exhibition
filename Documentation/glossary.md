# Glossary of Terms and Acronyms

> **Project:** Linked Open Exhibition — NFDI4Culture / Hochschule Hannover (BIM-126-02)  
> **Last updated:** April 2026

---

## A

**AAT** — Art & Architecture Thesaurus  
A structured vocabulary published by the Getty Research Institute for describing art, architecture, and material culture. Used as a controlled vocabulary for Linked Art type classifications.

**API** — Application Programming Interface  
A defined interface allowing software applications to communicate. In this project, APIs include the DNB SRU API, Wikidata Query Service, Lobid-GND API, and the Wikibase MediaWiki Action API.

**Attribution (AI)**  
All notebooks and documentation in this project credit GitHub Copilot (Claude Sonnet 4.6) as the AI tool used during development, following the project's AI attribution policy.

---

## B

**BIM-126-02**  
The course code for *Data Science (SoSe 2026)* at Hochschule Hannover, taught by Simon Worthington and Prof. Ina Blümel. The course is an eight-session introduction to Linked Open Data for GLAM using Wikimedia Foundation platforms.

**Bot account**  
A dedicated Wikibase/MediaWiki user account used for automated data uploads via `wikibaseintegrator` or `mwclient`. Credentials are stored in a `.env` file (never committed to version control).

---

## C

**CC0** — Creative Commons Zero  
The public-domain dedication licence applied to DNB metadata. Records retrieved via the DNB SRU API are released under CC0 1.0 Universal and may be freely reused without attribution.

**CC BY-SA 4.0** — Creative Commons Attribution-ShareAlike 4.0 International  
The licence applied to project content (slides, documentation). Requires attribution and share-alike when reusing.

**CIDOC-CRM** — Comité International pour la Documentation — Conceptual Reference Model  
An event-based ontology for cultural heritage documentation, maintained by ICOM. Linked Art is an application profile of CIDOC-CRM 7.1.3. Core classes include `E7_Activity`, `E22_Human-Made_Object`, `E53_Place`, and `E55_Type`.

**CQL** — Contextual Query Language  
A standard query language used with the SRU protocol. DNB SRU queries use CQL syntax, e.g. `KOR="Sprengel Museum" and SWW="Ausstellungskatalog"`.

**CRMdig**  
An extension of CIDOC-CRM for describing digital provenance. Provides classes such as `D1_Digital_Object` and `D29_Annotation_Object`, referenced in the Linked Art ontology.

**CRMsci**  
A scientific observation extension of CIDOC-CRM, providing classes such as `S19_Encounter_Event` for describing the discovery of objects.

**CSV** — Comma-Separated Values  
A plain-text tabular data format used for intermediate outputs such as `sprengel_exhibitions.csv` and for encoding the WB4R data model (`wikibase_generic_model.csv`).

---

## D

**DNB** — Deutsche Nationalbibliothek (German National Library)  
The national library of Germany, maintaining a central bibliographic catalogue that includes exhibition catalogues. The DNB SRU API and Library Lab services are primary data sources in this project.

**DNB Library Lab**  
A programme by the DNB providing experimental API access, Jupyter notebook tutorials, and data services for developers and researchers. See: <https://www.dnb.de/librarylab>

**DNB SRU API**  
The DNB's implementation of the SRU (Search/Retrieve via URL) protocol. Endpoint: `https://services.dnb.de/sru/dnb`. Provides free, no-registration access to bibliographic records in MARC21-XML format.

**Dot / Graphviz DOT**  
A plain-text graph description language used in the file `data.dot` to represent data relationships. Rendered by Graphviz or embedded in Quarto via the `{dot}` code block.

---

## E

**ENV file (`.env`)**  
A file used to store environment-specific configuration values such as API credentials. The `.env` file is gitignored; a committed `.env.example` documents the required keys without revealing real values. Loaded at runtime via `python-dotenv`.

---

## F

**FOAF** — Friend of a Friend  
An RDF vocabulary for describing people and their relationships. Referenced in the WB4R data model as an equivalent class for actors (`foaf:Agent`).

---

## G

**GLAM** — Galleries, Libraries, Archives and Museums  
A collective term for cultural heritage institutions that collect, preserve, and provide access to cultural objects. The project targets GLAM use cases, specifically art museum exhibitions.

**GND** — Gemeinsame Normdatei (Integrated Authority File)  
The German-language union authority file maintained by the DNB and library network partners. Provides stable URIs for persons, organisations, places, and subjects. Accessible via the Lobid-GND API.

**GitHub Pages**  
A static website hosting service provided by GitHub, used to publish the Quarto website output from the `docs/` directory. URL: <https://nfdi4culture.github.io/linked-open-exhibition/>

---

## I

**IDN** — Identifikationsnummer  
The unique record identifier used in the DNB catalogue. Encoded in MARC21 field `001`. Used to construct cover image URLs and link records across systems.

**IRI** — Internationalised Resource Identifier  
A generalisation of the URI/URL standard that supports Unicode characters. Used in RDF and ontologies to uniquely identify entities and properties, e.g. `https://www.cidoc-crm.org/cidoc-crm/E22_Human-Made_Object`.

**ISBN** — International Standard Book Number  
A numeric identifier for published books. Encoded in MARC21 field `020`. Used to retrieve cover images from the DNB cover image API (`https://portal.dnb.de/opac/mvb/cover?isbn={ISBN}`).

---

## J

**JSON-LD** — JavaScript Object Notation for Linked Data  
A method of encoding Linked Data using JSON syntax. The Linked Art API serialises its records as JSON-LD 1.1. Wikibase also supports JSON-LD export.

**JupyterLite**  
A browser-based Jupyter environment that runs Python (via Pyodide/WebAssembly) without a server. The DNB Library Lab provides a JupyterLite instance at <https://deutsche-nationalbibliothek.github.io/jupyterlite/lab/>. The project's earlier notebooks in `catalogues/dnb-jupyter/` were designed for JupyterLite.

---

## L

**LDS** — Linked Data Service (DNB)  
The DNB's service for downloading bulk metadata as RDF or other Linked Data formats. See: <https://www.dnb.de/EN/Professionell/Metadatendienste/Datenbezug/LDS/lds_node.html>

**LIDO** — Lightweight Information Describing Objects  
An XML schema for contributing, harvesting, and exchanging museum collection data. Example files are stored in the `LIDO/` directory of this project. Used as a reference format for cultural heritage object description.

**Linked Art**  
An international initiative and data model providing a community-maintained application profile of CIDOC-CRM for describing art and cultural heritage objects. Serialised as JSON-LD 1.1. Version 1.0. See: <https://linked.art/>

**Lobid-GND**  
An API provided by the Hochschule für Bibliotheks- und Informationswesen (hbz) that exposes GND authority data as JSON-LD. Supports fast auto-suggest and URI-based lookup. Documentation in `LOD-API/Lobid-GND.md`.

**LOD** — Linked Open Data  
Data published on the web using open standards (RDF, HTTP, URIs) and linked to other datasets. The project demonstrates LOD for art exhibitions by connecting DNB, Wikidata, GND, and Wikibase data.

**LOD-API**  
A directory in the project repository containing documentation and examples for working with Linked Open Data APIs, particularly Lobid-GND.

---

## M

**MARC21** — MAchine-Readable Cataloging (version 21)  
A bibliographic metadata standard used in library systems. DNB SRU API responses are delivered as MARC21-XML. Key fields used in this project include `001` (IDN), `245` (title), `264`/`260` (publication year), `020` (ISBN), `689` (subject headings), and `856` (URL).

**MediaWiki**  
The wiki software underlying Wikipedia and Wikibase. The project uses `mwclient` to upload images to the project's MediaWiki instance.

**Mermaid**  
A JavaScript-based diagramming syntax used to generate flowcharts and sequence diagrams from plain text. Used in `exhibition.mmd`, `flow.mmd`, and rendered by Quarto.

**mwclient**  
A Python library for interacting with MediaWiki APIs. Used in this project for uploading cover images to the project MediaWiki instance.

---

## N

**NFDI** — Nationale Forschungsdateninfrastruktur (National Research Data Infrastructure)  
A German federal initiative building research data infrastructure across scientific domains.

**NFDI4Culture**  
The NFDI consortium for research on material and immaterial cultural heritage. The project is carried out under NFDI4Culture auspices.

---

## O

**OWL** — Web Ontology Language  
A W3C standard for defining ontologies on the Semantic Web. The WB4R data model uses OWL class definitions (`owl:Class`) to describe entity types.

---

## P

**python-dotenv**  
A Python library that reads key-value pairs from `.env` files into environment variables. Used to load Wikibase credentials at runtime without hardcoding them.

---

## Q

**QID** — Q Item Identifier  
A unique identifier for an item in Wikidata or Wikibase, prefixed with `Q` (e.g. `Q510144` for Sprengel Museum). The `Q` prefix was chosen arbitrarily by Wikidata's original developers to distinguish item identifiers from property identifiers (which use `P`) and lexeme identifiers (which use `L`). The letter itself carries no semantic meaning — it was simply a letter not already in common use in the technical context. QIDs are stable and language-neutral, making them reliable identifiers for interlinking data across systems regardless of the label language. Referenced throughout SPARQL queries and data model mappings in this project.

**Quarto**  
An open-source scientific and technical publishing system (version ≥ 1.3) used to render the project website from Markdown (`.qmd`) and Jupyter Notebook sources. Output is published to `docs/` for GitHub Pages.

---

## R

**RDF** — Resource Description Framework  
A W3C standard for representing information as subject–predicate–object triples. The foundation of Linked Data and SPARQL.

**RevealJS**  
A JavaScript presentation framework. The project's `index.qmd` was originally formatted as RevealJS slides before conversion to a Quarto website.

---

## S

**SPARQL** — SPARQL Protocol and RDF Query Language  
A query language for RDF data. Used in this project to query Wikidata and the project Wikibase endpoint. Example queries visualise exhibitions as timelines, graphs, and maps.

**SPARQLWrapper**  
A Python library for sending SPARQL queries to RDF endpoints and parsing results. Listed as a project dependency in `requirements.txt`.

**Sprengel Museum Hannover**  
An art museum in Hannover, Germany, specialising in modern and contemporary art. The primary use-case institution for the project, providing the exhibition dataset sourced from DNB records.

**SRU** — Search/Retrieve via URL  
An OASIS/Library of Congress standard protocol for performing bibliographic search and record retrieval over HTTP. Queries are written in CQL and results are returned as XML. The DNB operates an SRU endpoint at `https://services.dnb.de/sru/dnb` that provides free, no-registration access to the full DNB catalogue in MARC21-XML format. Supports pagination via the `startRecord` parameter (up to 100 records per request). The protocol version used by DNB is SRU 1.1.

**SWW** — Schlagwort / Subject Word  
A CQL index field used in DNB SRU queries to search by subject heading. `SWW="Ausstellungskatalog"` filters for exhibition catalogue records.

---

## U

**URI** — Uniform Resource Identifier  
A string that uniquely identifies a resource. In Linked Data, URIs are used as identifiers for entities, properties, and concepts to enable interlinking across datasets.

---

## W

**WB4R** — Wikibase for Research (Generic Model)  
A reference data model developed by NFDI4Culture (Rossenova, Sohmen, Duchesne) that defines a set of generic classes and properties for a research-purpose Wikibase instance. Repository: <https://gitlab.com/nfdi4culture/wikibase4research/model/>. The CSV file `WB4R/wikibase_generic_model.csv` is used as a property and class alignment reference in this project.

**Wikibase**  
An open-source software platform (part of the Wikimedia suite) for creating structured, linked knowledge bases. In this project, the hosted instance at `https://wikibase.wbworkshop.tibwiki.io/` is used to store exhibition metadata.

**wikibaseintegrator**  
A Python library for reading and writing data to Wikibase instances via the MediaWiki API. Used for programmatic upload of exhibition records.

**Wikidata**  
A free, collaborative, multilingual knowledge base maintained by the Wikimedia Foundation. Students manually created exhibition entries in Wikidata during early course sessions. Public Wikidata SPARQL endpoint: <https://query.wikidata.org/>

**Wikimedia Commons**  
A repository of freely licensed media files (images, audio, video) maintained by the Wikimedia Foundation. Referenced as part of the course platform context.

**Wikiversity**  
A Wikimedia Foundation project for open educational content. Course materials for BIM-126-02 are hosted at: <https://en.wikiversity.org/wiki/BIM-126-02-Data-Science-Linked-Open-Exhibition>

---

## X

**XML** — Extensible Markup Language  
A structured text format used for data exchange. MARC21-XML is the format returned by the DNB SRU API. LIDO files in this project are also XML-based.

---

*This glossary covers terms and acronyms appearing in the project files, data models, notebooks, and documentation. For ontology class definitions see [Linkedart/linked-art-terms.md](../Linkedart/linked-art-terms.md) and [Linkedart/linked-art-ontology.md](../Linkedart/linked-art-ontology.md). For WB4R property details see [WB4R/wikibase_generic_model.csv](../WB4R/wikibase_generic_model.csv).*
