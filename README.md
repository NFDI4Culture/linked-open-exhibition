# Verknüpfte Offene Ausstellung

Prototyp zur Erstellung verknüpfter offener Ausstellungsdatensätze

Demonstration von Linked Open Data‑Standards für Ausstellungsobjekte.

Ein Prototypprojekt, das mit den Studierenden des Bachelor of Arts Informationsmanagement der Hochschule Hannover im Seminar „BIM-126-02 Data Science (2026)" erstellt wurde. Frühe Arbeit fand sich im Repository https://github.com/NFDI4Culture/open-museum.

Weitere Hintergrundinformationen und Kursmaterialien finden sich auf der Wikiversity-Seite: https://en.wikiversity.org/wiki/BIM-126-02-Data-Science-Linked-Open-Exhibition


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

## 🎨 Styling

Die Präsentation verwendet angepasste Styles:

- hellgrauer Hintergrund über `styles.css`
- Fußzeile auf allen Folien mit `CC BY-SA 4.0` (konfiguriert in `_quarto.yml`)

## 📝 Projektzusammenfassung

Das Repository begleitet einen achtteiligen Kurs „Linked Open Exhibition“,
bei dem die Studierenden an der Hochschule Hannover in das Thema Linked Open
Data (LOD) eingeführt werden. Schwerpunkte sind:

1. Einsatz von LOD im GLAM‑Bereich (Galleries, Libraries, Archives, Museums)
2. Nutzung von Wikimedia-Plattformen wie Wikidata, Wikibase, MediaWiki und
   Wikimedia Commons

Ziel ist es, Museumsausstellungen als **Linked Open Exhibitions** zu erfassen –
als Ablaufplan, Objektkatalog und weitere relevante Metadaten. Dabei kommen
Open-Source-Software, Open-Science-Praktiken und Rapid Prototyping zum Einsatz.
Der Workflow nutzt KI‑Hilfsmittel (Copilot, Chat‑LLMs) zur Code‑ und
Abfragegenerierung.

## 🤖 Entwicklung

Dieses Projekt wurde mit Unterstützung von GitHub Copilot entwickelt.
