#!/usr/bin/env python
"""
dump_cps_rdf.py
---------------
Exports the CPS Wikibase (https://cps.tibwiki.io/) as RDF triples (Turtle) using the
standard Wikibase RDF output (Special:EntityData). The output is the same RDF that the
Wikibase Query Service holds, including wdt:/p:/ps:/pq:/prov: triples.

Output (written next to this script)
    cps.ttl     Turtle, UTF-8, with the usual Wikibase prefixes

Usage
    python data-models/portability/dump_cps_rdf.py
    python data-models/portability/dump_cps_rdf.py --url https://cps.tibwiki.io
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import requests
from rdflib import Graph

HERE = Path(__file__).resolve().parent
OUT_PATH = HERE / "cps.ttl"
NAMESPACES = {"item": 120, "property": 122}


def get_json(session: requests.Session, api: str, **params) -> dict:
    params.update(format="json", formatversion="2")
    response = session.get(api, params=params, timeout=60)
    response.raise_for_status()
    return response.json()


def list_entity_ids(session: requests.Session, api: str, namespace: int) -> list[str]:
    ids: list[str] = []
    params = {"action": "query", "list": "allpages", "apnamespace": namespace, "aplimit": "max"}
    while True:
        data = get_json(session, api, **params)
        ids.extend(page["title"].split(":", 1)[1] for page in data["query"]["allpages"])
        if "continue" not in data:
            return ids
        params.update(data["continue"])


def fetch_ntriples(session: requests.Session, base: str, entity_id: str) -> str:
    url = f"{base}/wiki/Special:EntityData/{entity_id}.nt"
    for attempt in range(4):
        response = session.get(url, params={"flavor": "dump"}, timeout=60)
        if response.status_code == 429 or response.status_code >= 500:
            time.sleep(2 * (attempt + 1))
            continue
        response.raise_for_status()
        return response.content.decode("utf-8")
    response.raise_for_status()
    raise RuntimeError("unreachable")


def prefixes(base: str) -> dict[str, str]:
    return {
        "wd": f"{base}/entity/",
        "wdt": f"{base}/prop/direct/",
        "p": f"{base}/prop/",
        "ps": f"{base}/prop/statement/",
        "pq": f"{base}/prop/qualifier/",
        "pr": f"{base}/prop/reference/",
        "wds": f"{base}/entity/statement/",
        "wdref": f"{base}/reference/",
        "wikibase": "http://wikiba.se/ontology#",
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--url", default="https://cps.tibwiki.io", help="Wikibase base URL")
    args = parser.parse_args()
    base = args.url.rstrip("/")
    api = f"{base}/w/api.php"

    session = requests.Session()
    session.headers["User-Agent"] = "linked-open-exhibition-dump/1.0 (NFDI4Culture)"

    graph = Graph()
    for prefix, uri in prefixes(base).items():
        graph.bind(prefix, uri)
    for kind, namespace in NAMESPACES.items():
        ids = list_entity_ids(session, api, namespace)
        for entity_id in ids:
            graph.parse(data=fetch_ntriples(session, base, entity_id), format="nt")
        print(f"{kind}: {len(ids)}")

    graph.serialize(destination=OUT_PATH, format="turtle", encoding="utf-8")
    print(f"wrote {len(graph)} triples to {OUT_PATH.name}")


if __name__ == "__main__":
    main()
