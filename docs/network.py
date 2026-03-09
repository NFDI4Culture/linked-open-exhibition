import argparse
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone

from SPARQLWrapper import JSON, SPARQLWrapper

ENDPOINT_URL = "https://query.wikidata.org/sparql"
MUSEUM_URI = "http://www.wikidata.org/entity/Q510144"

QUERY_TEMPLATE = """#defaultView:Graph
SELECT ?item ?itemLabel ?relatedItem ?relatedItemLabel ?pLabel ?rgb WHERE {
  BIND(wd:Q510144 AS ?museum)

  {
    ?exhibition wdt:P31/wdt:P279* wd:Q464980;
                wdt:P276 ?museum.
    BIND(?museum AS ?item)
    BIND(?exhibition AS ?relatedItem)
    BIND(wdt:P276 AS ?p)
    BIND("841617" AS ?rgb)
  }
  UNION
  {
    ?exhibition wdt:P31/wdt:P279* wd:Q464980;
                wdt:P276 wd:Q510144;
                ?p ?relatedItem.

    FILTER(?p IN (wdt:P170, wdt:P1640, wdt:P921, wdt:P180))
    BIND(?exhibition AS ?item)
  }

  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en,de".
    ?item rdfs:label ?itemLabel.
    ?relatedItem rdfs:label ?relatedItemLabel.
    ?p wikibase:propertyLabel ?pLabel.
  }
}
LIMIT __LIMIT__
"""


def get_results(endpoint_url: str, query: str):
    user_agent = f"linked-open-exhibition-dashboard Python/{sys.version_info[0]}.{sys.version_info[1]}"
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def extract_id(uri: str) -> str:
    return uri.rsplit("/", 1)[-1] if uri else ""


def upsert_node(nodes: dict, node_id: str, label: str, node_type: str):
    priority = {"related": 0, "exhibition": 1, "museum": 2}
    existing = nodes.get(node_id)
    if not existing:
        nodes[node_id] = {"id": node_id, "label": label or node_id, "type": node_type}
        return

    if label and (existing["label"] == existing["id"]):
        existing["label"] = label

    if priority[node_type] > priority[existing["type"]]:
        existing["type"] = node_type


def build_graph_data(results_json: dict):
    nodes = {}
    edges = {}

    bindings = results_json.get("results", {}).get("bindings", [])
    for row in bindings:
        source_uri = row.get("item", {}).get("value", "")
        source_label = row.get("itemLabel", {}).get("value", "")
        target_uri = row.get("relatedItem", {}).get("value", "")
        target_label = row.get("relatedItemLabel", {}).get("value", "")
        prop_label = row.get("pLabel", {}).get("value", "related to")

        source_id = extract_id(source_uri)
        target_id = extract_id(target_uri)
        if not source_id or not target_id:
            continue

        source_type = "museum" if source_uri == MUSEUM_URI else "exhibition"
        target_type = "exhibition" if source_uri == MUSEUM_URI else "related"

        upsert_node(nodes, source_id, source_label, source_type)
        upsert_node(nodes, target_id, target_label, target_type)

        edge_key = (source_id, target_id, prop_label)
        if edge_key not in edges:
            edges[edge_key] = {
                "source": source_id,
                "target": target_id,
                "label": prop_label,
                "count": 0,
            }
        edges[edge_key]["count"] += 1

    node_list = sorted(nodes.values(), key=lambda item: (item["type"], item["label"]))
    edge_list = list(edges.values())

    node_type_counts = Counter(node["type"] for node in node_list)
    property_counts = Counter(edge["label"] for edge in edge_list)

    return {
        "nodes": node_list,
        "edges": edge_list,
        "stats": {
            "nodes": len(node_list),
            "edges": len(edge_list),
            "exhibitions": node_type_counts.get("exhibition", 0),
            "related_entities": node_type_counts.get("related", 0),
        },
        "property_counts": property_counts.most_common(),
    }


def render_dashboard_html(graph_data: dict, generated_at: str) -> str:
    payload = json.dumps(graph_data, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Linked Open Exhibition · Project Dashboard</title>
  <style>
    :root {{
      --bg: #0f172a;
      --panel: #111827;
      --muted: #94a3b8;
      --text: #e5e7eb;
      --border: #1f2937;
      --accent: #841617;
      --exhibition: #b45309;
      --related: #0ea5e9;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: var(--bg); color: var(--text); font-family: Segoe UI, Roboto, Arial, sans-serif; }}
    .wrap {{ max-width: 1320px; margin: 0 auto; padding: 18px; }}
    h1 {{ margin: 0 0 8px; font-size: 28px; }}
    .sub {{ color: var(--muted); margin-bottom: 16px; }}
    .grid {{ display: grid; gap: 14px; grid-template-columns: repeat(4, minmax(0, 1fr)); margin-bottom: 14px; }}
    .card {{ background: var(--panel); border: 1px solid var(--border); border-radius: 10px; padding: 12px; }}
    .kpi-label {{ color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: .04em; }}
    .kpi-value {{ margin-top: 6px; font-size: 28px; font-weight: 600; }}
    .main {{ display: grid; gap: 14px; grid-template-columns: 2fr 1fr; }}
    .canvas-wrap {{ position: relative; min-height: 680px; }}
    #graph {{ width: 100%; height: 680px; border-radius: 10px; background: #0b1220; border: 1px solid var(--border); }}
    .legend {{ display: flex; gap: 16px; margin-top: 8px; color: var(--muted); font-size: 13px; }}
    .dot {{ width: 10px; height: 10px; border-radius: 50%; display: inline-block; margin-right: 6px; }}
    .dot-museum {{ background: var(--accent); }}
    .dot-exhibition {{ background: var(--exhibition); }}
    .dot-related {{ background: var(--related); }}
    .panel-title {{ margin: 0 0 10px; font-size: 16px; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
    th, td {{ text-align: left; border-bottom: 1px solid var(--border); padding: 7px 6px; vertical-align: top; }}
    th {{ color: var(--muted); font-weight: 600; }}
    .small {{ color: var(--muted); font-size: 12px; }}
  </style>
</head>
<body>
  <div class="wrap">
    <h1>Linked Open Exhibition Dashboard</h1>
    <div class="sub">Generated from Wikidata via <code>docs/network.py</code> · {generated_at}</div>

    <section class="grid">
      <article class="card"><div class="kpi-label">Nodes</div><div class="kpi-value" id="kpi-nodes">0</div></article>
      <article class="card"><div class="kpi-label">Edges</div><div class="kpi-value" id="kpi-edges">0</div></article>
      <article class="card"><div class="kpi-label">Exhibitions</div><div class="kpi-value" id="kpi-exhibitions">0</div></article>
      <article class="card"><div class="kpi-label">Related Entities</div><div class="kpi-value" id="kpi-related">0</div></article>
    </section>

    <section class="main">
      <article class="card canvas-wrap">
        <h2 class="panel-title">Network Overview</h2>
        <canvas id="graph" width="900" height="680"></canvas>
        <div class="legend">
          <span><span class="dot dot-museum"></span>Museum</span>
          <span><span class="dot dot-exhibition"></span>Exhibition</span>
          <span><span class="dot dot-related"></span>Related entity</span>
        </div>
      </article>

      <aside>
        <article class="card" style="margin-bottom:14px;">
          <h2 class="panel-title">Relationship Types</h2>
          <table id="rel-table">
            <thead><tr><th>Property</th><th>Count</th></tr></thead>
            <tbody></tbody>
          </table>
        </article>
        <article class="card">
          <h2 class="panel-title">Sample Links</h2>
          <table id="edge-table">
            <thead><tr><th>From</th><th>To</th><th>Type</th></tr></thead>
            <tbody></tbody>
          </table>
          <div class="small" style="margin-top:10px;">Showing first 25 links.</div>
        </article>
      </aside>
    </section>
  </div>

  <script>
    const DATA = {payload};

    function setKpis() {{
      document.getElementById('kpi-nodes').textContent = DATA.stats.nodes;
      document.getElementById('kpi-edges').textContent = DATA.stats.edges;
      document.getElementById('kpi-exhibitions').textContent = DATA.stats.exhibitions;
      document.getElementById('kpi-related').textContent = DATA.stats.related_entities;
    }}

    function fillTables() {{
      const relBody = document.querySelector('#rel-table tbody');
      DATA.property_counts.forEach(([name, count]) => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${{name}}</td><td>${{count}}</td>`;
        relBody.appendChild(tr);
      }});

      const edgeBody = document.querySelector('#edge-table tbody');
      const lookup = new Map(DATA.nodes.map(n => [n.id, n]));
      DATA.edges.slice(0, 25).forEach(edge => {{
        const source = lookup.get(edge.source)?.label || edge.source;
        const target = lookup.get(edge.target)?.label || edge.target;
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${{source}}</td><td>${{target}}</td><td>${{edge.label}}</td>`;
        edgeBody.appendChild(tr);
      }});
    }}

    function renderForceGraph() {{
      const canvas = document.getElementById('graph');
      const ctx = canvas.getContext('2d');
      const width = canvas.width;
      const height = canvas.height;
      const centerX = width / 2;
      const centerY = height / 2;

      const colorForType = (type) => {{
        if (type === 'museum') return '#841617';
        if (type === 'exhibition') return '#b45309';
        return '#0ea5e9';
      }};

      const nodes = DATA.nodes.map((node, index) => {{
        const angle = (index / Math.max(DATA.nodes.length, 1)) * Math.PI * 2;
        const radius = node.type === 'museum' ? 0 : (node.type === 'exhibition' ? 180 : 280);
        return {{
          ...node,
          x: centerX + Math.cos(angle) * radius,
          y: centerY + Math.sin(angle) * radius,
          vx: 0,
          vy: 0,
        }};
      }});

      const nodeById = new Map(nodes.map(n => [n.id, n]));
      const links = DATA.edges
        .map(edge => ({{ source: nodeById.get(edge.source), target: nodeById.get(edge.target) }}))
        .filter(link => link.source && link.target);

      for (let step = 0; step < 220; step++) {{
        for (let i = 0; i < nodes.length; i++) {{
          for (let j = i + 1; j < nodes.length; j++) {{
            const a = nodes[i];
            const b = nodes[j];
            let dx = b.x - a.x;
            let dy = b.y - a.y;
            const dist2 = Math.max(dx * dx + dy * dy, 1);
            const force = 4200 / dist2;
            const dist = Math.sqrt(dist2);
            dx /= dist;
            dy /= dist;
            a.vx -= dx * force;
            a.vy -= dy * force;
            b.vx += dx * force;
            b.vy += dy * force;
          }}
        }}

        links.forEach(link => {{
          const dx = link.target.x - link.source.x;
          const dy = link.target.y - link.source.y;
          const distance = Math.sqrt(dx * dx + dy * dy) || 1;
          const desired = (link.source.type === 'museum' || link.target.type === 'museum') ? 180 : 120;
          const force = (distance - desired) * 0.003;
          const nx = dx / distance;
          const ny = dy / distance;
          link.source.vx += nx * force;
          link.source.vy += ny * force;
          link.target.vx -= nx * force;
          link.target.vy -= ny * force;
        }});

        nodes.forEach(node => {{
          node.vx *= 0.86;
          node.vy *= 0.86;
          node.x += node.vx;
          node.y += node.vy;
          node.x = Math.max(25, Math.min(width - 25, node.x));
          node.y = Math.max(25, Math.min(height - 25, node.y));
        }});
      }}

      ctx.clearRect(0, 0, width, height);

      ctx.strokeStyle = 'rgba(148, 163, 184, 0.22)';
      ctx.lineWidth = 1;
      links.forEach(link => {{
        ctx.beginPath();
        ctx.moveTo(link.source.x, link.source.y);
        ctx.lineTo(link.target.x, link.target.y);
        ctx.stroke();
      }});

      nodes.forEach(node => {{
        const radius = node.type === 'museum' ? 10 : (node.type === 'exhibition' ? 7 : 5);
        ctx.beginPath();
        ctx.fillStyle = colorForType(node.type);
        ctx.arc(node.x, node.y, radius, 0, Math.PI * 2);
        ctx.fill();

        if (node.type !== 'related') {{
          ctx.fillStyle = '#e5e7eb';
          ctx.font = '11px Segoe UI, Arial';
          ctx.fillText(node.label, node.x + 9, node.y - 8);
        }}
      }});
    }}

    setKpis();
    fillTables();
    renderForceGraph();
  </script>
</body>
</html>
"""


def write_dashboard_html(output_path: str, html_content: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(html_content)


def main():
    parser = argparse.ArgumentParser(description="Generate a standalone project dashboard HTML from Wikidata network data.")
    parser.add_argument(
        "--output",
        default=os.path.join(os.path.dirname(__file__), "project-dashboard.html"),
        help="Output HTML path (default: docs/project-dashboard.html)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=300,
        help="SPARQL result limit (default: 300)",
    )
    args = parser.parse_args()

    query = QUERY_TEMPLATE.replace("__LIMIT__", str(max(1, args.limit)))
    results = get_results(ENDPOINT_URL, query)
    graph_data = build_graph_data(results)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    html = render_dashboard_html(graph_data, generated_at)
    write_dashboard_html(args.output, html)

    print(f"Dashboard written: {args.output}")
    print(
        f"Nodes: {graph_data['stats']['nodes']} | "
        f"Edges: {graph_data['stats']['edges']} | "
        f"Exhibitions: {graph_data['stats']['exhibitions']}"
    )


if __name__ == "__main__":
    main()
