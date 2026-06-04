"""
fetch_wikidata_exhibitions.py
Reads ausstellungen/liste-2026-04-29.csv, resolves every Wikidata QID
(including short w.wiki/* redirects), queries the Wikidata SPARQL endpoint
for exhibition metadata, and writes two output files:
  - ausstellungen/exhibitions-wikidata.csv   (enriched CSV)
  - ausstellungen/exhibitions.xml            (XML valid against the DTD)
"""

import csv
import json
import re
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from xml.dom import minidom
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_IN   = BASE_DIR / "ausstellungen" / "liste-2026-04-29.csv"
CSV_OUT  = BASE_DIR / "ausstellungen" / "exhibitions-wikidata.csv"
XML_OUT  = BASE_DIR / "ausstellungen" / "exhibitions.xml"

WIKIDATA_API = "https://www.wikidata.org/w/api.php"

HEADERS = {
    "User-Agent": "LinkedOpenExhibition/1.0 (https://github.com/NFDI4Culture/linked-open-exhibition)",
    "Accept": "application/json",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_qid(raw: str) -> str | None:
    """Return 'Q123456' from any Wikidata / w.wiki URL, or None."""
    raw = raw.strip()
    if not raw:
        return None
    # Already bare QID
    m = re.fullmatch(r"Q\d+", raw)
    if m:
        return raw
    # Standard wikidata.org URL
    m = re.search(r"/wiki/(Q\d+)", raw)
    if m:
        return m.group(1)
    # Short redirect  w.wiki/XXXX  — follow the HTTP redirect
    if "w.wiki" in raw:
        return resolve_short_url(raw)
    return None


def resolve_short_url(url: str) -> str | None:
    """Follow a w.wiki short redirect and extract the QID from the final URL."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": HEADERS["User-Agent"]})
        # urllib follows redirects by default; we need the final URL
        with urllib.request.urlopen(req, timeout=10) as resp:
            final_url = resp.url
        m = re.search(r"/wiki/(Q\d+)", final_url)
        if m:
            return m.group(1)
    except Exception as exc:
        print(f"  [WARN] Could not resolve {url}: {exc}")
    return None


def api_get(params: dict) -> dict:
    """Call the Wikidata MediaWiki API and return parsed JSON."""
    params["format"] = "json"
    qs = urllib.parse.urlencode(params)
    url = f"{WIKIDATA_API}?{qs}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def _label(entity: dict, lang: str = "en") -> str:
    return entity.get("labels", {}).get(lang, {}).get("value", "")


def _datavalue(claims: dict, pid: str) -> str:
    """Extract the first datavalue string/label for a property."""
    if pid not in claims:
        return ""
    snak = claims[pid][0].get("mainsnak", {})
    dv = snak.get("datavalue", {})
    vtype = dv.get("type", "")
    val = dv.get("value", "")
    if vtype == "string":
        return val
    if vtype == "monolingualtext":
        return val.get("text", "") if isinstance(val, dict) else ""
    if vtype == "time":
        return val.get("time", "")[:11].lstrip("+") if isinstance(val, dict) else ""
    if vtype == "wikibase-entityid":
        return val.get("id", "") if isinstance(val, dict) else ""
    return str(val)


def fetch_exhibitions(qids: list[str]) -> dict[str, dict]:
    """
    Batch-fetch exhibition metadata using wbgetentities.
    Returns dict keyed by QID.
    """
    results: dict[str, dict] = {}
    chunk_size = 50  # API supports up to 50 per call

    for i in range(0, len(qids), chunk_size):
        chunk = qids[i : i + chunk_size]
        data = api_get({
            "action": "wbgetentities",
            "ids": "|".join(chunk),
            "props": "labels|descriptions|claims",
            "languages": "en|de",
        })
        entities = data.get("entities", {})

        # Collect all location / person QIDs we need to resolve to labels
        linked_qids: set[str] = set()
        for qid, ent in entities.items():
            if "missing" in ent:
                continue
            claims = ent.get("claims", {})
            for pid in ("P276", "P1640", "P664", "P17"):
                val = _datavalue(claims, pid)
                if val.startswith("Q"):
                    linked_qids.add(val)

        # Resolve linked QIDs to labels in one extra call
        label_cache: dict[str, str] = {}
        if linked_qids:
            ldata = api_get({
                "action": "wbgetentities",
                "ids": "|".join(linked_qids),
                "props": "labels",
                "languages": "en|de",
            })
            for lqid, lent in ldata.get("entities", {}).items():
                label_cache[lqid] = (
                    lent.get("labels", {}).get("en", {}).get("value", "")
                    or lent.get("labels", {}).get("de", {}).get("value", "")
                    or lqid
                )

        for qid, ent in entities.items():
            if "missing" in ent:
                continue
            claims = ent.get("claims", {})
            title = (
                _datavalue(claims, "P1476")
                or _label(ent, "en")
                or _label(ent, "de")
            )
            loc_qid  = _datavalue(claims, "P276")
            cur_qid  = _datavalue(claims, "P1640")
            org_qid  = _datavalue(claims, "P664")
            cty_qid  = _datavalue(claims, "P17")

            results[qid] = {
                "title":       title,
                "startDate":   _datavalue(claims, "P580"),
                "endDate":     _datavalue(claims, "P582"),
                "location":    label_cache.get(loc_qid, loc_qid),
                "locationQID": loc_qid,
                "curator":     label_cache.get(cur_qid, cur_qid),
                "organizer":   label_cache.get(org_qid, org_qid),
                "country":     label_cache.get(cty_qid, cty_qid),
                "website":     _datavalue(claims, "P856"),
                "image":       _datavalue(claims, "P18"),
                "description": (
                    ent.get("descriptions", {}).get("en", {}).get("value", "")
                    or ent.get("descriptions", {}).get("de", {}).get("value", "")
                ),
            }
        time.sleep(0.5)

    return results



# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # 1. Read CSV
    rows_in = []
    with open(CSV_IN, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            rows_in.append(row)

    print(f"Read {len(rows_in)} rows from {CSV_IN.name}")

    # 2. Resolve QIDs
    qid_map: dict[str, str | None] = {}  # row wikidata cell -> QID
    for row in rows_in:
        wd_cell = row.get("Wikidata", "").strip()
        if wd_cell:
            qid = extract_qid(wd_cell)
            qid_map[wd_cell] = qid
            if qid:
                print(f"  {wd_cell[:50]:<52} -> {qid}")
            else:
                print(f"  [SKIP] Could not resolve: {wd_cell}")

    unique_qids = [q for q in set(qid_map.values()) if q]
    print(f"\nFetching {len(unique_qids)} QIDs from Wikidata SPARQL …")

    # 3. Fetch from Wikidata
    wd_data = fetch_exhibitions(unique_qids)
    print(f"Received data for {len(wd_data)} items.")

    # 4. Build enriched rows
    enriched: list[dict] = []
    for row in rows_in:
        wd_cell = row.get("Wikidata", "").strip()
        qid = qid_map.get(wd_cell) if wd_cell else None
        data = wd_data.get(qid, {}) if qid else {}

        # Derive a slug from the museum URL
        museum_url = row.get("Exhibition", "").strip()
        slug = museum_url.rstrip("/").split("/")[-1]

        enriched.append({
            "qid":         qid or "",
            "wikidata_url": f"https://www.wikidata.org/wiki/{qid}" if qid else "",
            "museum_url":  museum_url,
            "slug":        slug,
            "title":       data.get("title", ""),
            "start_date":  data.get("startDate", "")[:10] if data.get("startDate") else "",
            "end_date":    data.get("endDate", "")[:10]   if data.get("endDate")   else "",
            "location":    data.get("location", ""),
            "location_qid": data.get("locationQID", ""),
            "curator":     data.get("curator", ""),
            "organizer":   data.get("organizer", ""),
            "country":     data.get("country", ""),
            "website":     data.get("website", ""),
            "image":       data.get("image", ""),
            "description": data.get("description", ""),
        })

    # 5. Write enriched CSV (only rows that have a QID and a start date)
    fieldnames = [
        "qid", "wikidata_url", "museum_url", "slug",
        "title", "start_date", "end_date",
        "location", "location_qid", "curator", "organizer",
        "country", "website", "image", "description",
    ]
    with open(CSV_OUT, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for r in enriched:
            if r["qid"] and r["start_date"]:   # must have a date for the timeline
                writer.writerow(r)

    written = sum(1 for r in enriched if r["qid"] and r["start_date"])
    print(f"\nWrote {written} rows (with QID + start date) to {CSV_OUT.name}")

    # 6. Write XML
    root = ET.Element("exhibitions")
    for r in enriched:
        if not (r["qid"] and r["start_date"]):
            continue
        ex = ET.SubElement(root, "exhibition")
        for field, value in r.items():
            child = ET.SubElement(ex, field)
            child.text = value

    xml_str = minidom.parseString(ET.tostring(root, encoding="unicode")).toprettyxml(indent="  ")
    # Remove the redundant <?xml ...?> line added by toprettyxml when we add our DOCTYPE
    xml_lines = xml_str.split("\n")
    xml_body = "\n".join(xml_lines[1:])  # strip first line

    doctype = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE exhibitions SYSTEM "exhibitions.dtd">\n'
    with open(XML_OUT, "w", encoding="utf-8") as fh:
        fh.write(doctype + xml_body)

    print(f"Wrote XML to {XML_OUT.name}")


if __name__ == "__main__":
    main()
