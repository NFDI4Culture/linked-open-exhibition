import requests
import pandas as pd
import matplotlib.pyplot as plt
from urllib.parse import unquote, urlparse

# 1. Fetch Data
sparql_query = """https://query.wikidata.org/#%23defaultView%3AGraph%0ASELECT%20%3Fitem%20%3FitemLabel%20%3FrelatedItem%20%3FrelatedItemLabel%20%3FpLabel%20%3Frgb%20WHERE%20%7B%0A%20%20%0A%20%20%23%201.%20The%20Centerpiece%3A%20Sprengel%20Museum%20%28Crushed%20Berry%29%0A%20%20BIND%28wd%3AQ510144%20AS%20%3Fmuseum%29%0A%20%20%0A%20%20%7B%0A%20%20%20%20%23%20Level%201%3A%20Links%20from%20Museum%20to%20Exhibitions%0A%20%20%20%20%3Fexhibition%20wdt%3AP31%2Fwdt%3AP279%2a%20wd%3AQ464980%3B%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20wdt%3AP276%20%3Fmuseum.%0A%20%20%20%20BIND%28%3Fmuseum%20AS%20%3Fitem%29%0A%20%20%20%20BIND%28%3Fexhibition%20AS%20%3FrelatedItem%29%0A%20%20%20%20BIND%28wdt%3AP276%20AS%20%3Fp%29%0A%20%20%20%20BIND%28%22841617%22%20AS%20%3Frgb%29%20%23%20Crushed%20Berry%20for%20the%20Museum%20center%0A%20%20%7D%0A%20%20UNION%0A%20%20%7B%0A%20%20%20%20%23%20Level%202%3A%20Links%20from%20Exhibitions%20to%20their%20Parts%20%28Artists%2C%20Curators%2C%20etc.%29%0A%20%20%20%20%3Fexhibition%20wdt%3AP31%2Fwdt%3AP279%2a%20wd%3AQ464980%3B%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20wdt%3AP276%20wd%3AQ510144%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Fp%20%3FrelatedItem.%0A%20%20%20%20%0A%20%20%20%20%23%20Filter%20for%20meaningful%20%22parts%22%20of%20an%20exhibition%0A%20%20%20%20FILTER%28%3Fp%20IN%20%28wdt%3AP170%2C%20wdt%3AP1640%2C%20wdt%3AP921%2C%20wdt%3AP180%29%29%20%0A%20%20%20%20BIND%28%3Fexhibition%20AS%20%3Fitem%29%0A%20%20%20%20%23%20Default%20color%20for%20exhibitions%20and%20their%20parts%0A%20%20%7D%0A%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20%0A%20%20%20%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%2Cde%22.%20%0A%20%20%20%20%3Fitem%20rdfs%3Alabel%20%3FitemLabel.%0A%20%20%20%20%3FrelatedItem%20rdfs%3Alabel%20%3FrelatedItemLabel.%0A%20%20%20%20%3Fp%20wikibase%3ApropertyLabel%20%3FpLabel.%0A%20%20%7D%0A%7D%0ALIMIT%20300"""

if sparql_query.startswith("https://query.wikidata.org/#"):
	parsed = urlparse(sparql_query)
	sparql_query = unquote(parsed.fragment)

if sparql_query.startswith("#"):
	sparql_query = sparql_query.split("\n", 1)[1]

url = "https://query.wikidata.org/sparql"
r = requests.get(
	url,
	params={'query': sparql_query, 'format': 'json'},
	headers={
		'Accept': 'application/sparql-results+json',
		'User-Agent': 'linked-open-exhibition/1.0 (educational project)'
	},
	timeout=30,
)
r.raise_for_status()
data = r.json()

# 2. Process into DataFrame
results = [ {k: v['value'] for k, v in row.items()} for row in data['results']['bindings'] ]
df = pd.DataFrame(results)

if df.empty:
	raise ValueError("SPARQL query returned no rows")

count_candidates = ['pLabel', 'p', 'relatedItemLabel', 'itemLabel', 'relatedItem', 'item']
property_column = next((column for column in count_candidates if column in df.columns), None)

if property_column is None:
	raise ValueError(f"No expected columns found in SPARQL results. Available columns: {list(df.columns)}")

exhibition_column = 'itemLabel' if 'itemLabel' in df.columns else 'item'

# 3. Aggregation Logic
num_exhibitions = df[exhibition_column].nunique()
property_counts = df[property_column].value_counts()

# 4. Visualization (Dashboard)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
property_counts.plot(kind='bar', ax=ax1, color='#841617')
ax1.set_title("Property Breakdown")
ax2.pie(property_counts, labels=property_counts.index, autopct='%1.1f%%')
ax2.set_title("Distribution of Roles")
plt.savefig('my_dashboard.png')