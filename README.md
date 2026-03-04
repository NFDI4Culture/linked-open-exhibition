# Verknüpfte Offene Ausstellung

Prototyp zur Erstellung verknüpfter offener Ausstellungsdatensätze

Ein Projekt der [NFDI4Culture](https://nfdi4culture.de/) zur Demonstration von Linked Open Data Standards für Ausstellungsobjekte.

## 📊 Projektstruktur

- **GND/** - Daten der Gemeinsamen Normdatei (German Authority File)
- **LIDO/** - Museum object metadata in LIDO XML format
  - `artist.xml` - Artist information
  - `catalogue.xml` - Catalogue data
  - `exhibition.xml` - Exhibition metadata
  - `exhibition-object.xml` - Exhibition object descriptions
- **LOD-API/** - Documentation for Linked Open Data API integration
  - `Lobid-GND.md` - Lobid GND API documentation
- **flow.mmd** - Datenfluss-Diagramm
- **notebook.ipynb** - Jupyter Notebook für Datenverarbeitung

## 🎬 Quarto Webseite

Das Projekt wird als Quarto Website präsentiert. Die Website wird aus den Markdown- und Notebook-Dateien generiert.

### Webseite rendern

```bash
quarto render
```

Die Website wird unter `_output/index.html` generiert.

### Webseite in Live-Vorschau anschauen

```bash
quarto preview
```

## 📋 Anforderungen

- [Quarto](https://quarto.org/) ≥ 1.3
- Python (für Jupyter Notebook)

## 📄 Lizenz

Siehe [LICENSE](LICENSE) Datei

## 🤖 Entwicklung

Dieses Projekt wurde mit Unterstützung von GitHub Copilot entwickelt.
