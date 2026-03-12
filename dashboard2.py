import requests
import pandas as pd
import matplotlib.pyplot as plt

# 1. Configuration
url = "https://query.wikidata.org/sparql"
sparql_query = """#defaultView:Graph
SELECT ?item ?itemLabel ?relatedItem ?relatedItemLabel ?pLabel ?rgb WHERE {
  
  # 1. The Centerpiece: Sprengel Museum (Crushed Berry)
  BIND(wd:Q510144 AS ?museum)
  
  {
    # Level 1: Links from Museum to Exhibitions
    ?exhibition wdt:P31/wdt:P279* wd:Q464980; 
                wdt:P276 ?museum.
    BIND(?museum AS ?item)
    BIND(?exhibition AS ?relatedItem)
    BIND(wdt:P276 AS ?p)
    BIND("841617" AS ?rgb) # Crushed Berry for the Museum center
  }
  UNION
  {
    # Level 2: Links from Exhibitions to their Parts (Artists, Curators, etc.)
    ?exhibition wdt:P31/wdt:P279* wd:Q464980; 
                wdt:P276 wd:Q510144;
                ?p ?relatedItem.
    
    # Filter for meaningful "parts" of an exhibition
    FILTER(?p IN (wdt:P170, wdt:P1640, wdt:P921, wdt:P180)) 
    BIND(?exhibition AS ?item)
    # Default color for exhibitions and their parts
  }

  SERVICE wikibase:label { 
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en,de". 
    ?item rdfs:label ?itemLabel.
    ?relatedItem rdfs:label ?relatedItemLabel.
    ?p wikibase:propertyLabel ?pLabel.
  }
}
LIMIT 300"""

# 2. Fetch Data
headers = {'Accept': 'application/sparql-results+json', 'User-Agent': 'WikiDashboardBot/1.0'}
response = requests.get(url, params={'query': sparql_query, 'format': 'json'}, headers=headers)
response.raise_for_status()
data = response.json()

# 3. Process to DataFrame
results = [{k: v['value'] for k, v in row.items()} for row in data['results']['bindings']]
df = pd.DataFrame(results)

if df.empty:
  raise ValueError("SPARQL query returned no rows")

group_column = 'pLabel' if 'pLabel' in df.columns else 'relatedItemLabel'
property_counts = df[group_column].value_counts().head(12)

# 4. Generate Dashboard
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
property_counts.plot(kind='bar', ax=ax1, color='#841617')
ax1.set_title("Property Breakdown")
ax1.set_xlabel("Property")
ax1.set_ylabel("Count")
ax1.tick_params(axis='x', rotation=45)

ax2.pie(property_counts, labels=property_counts.index, autopct='%1.1f%%', startangle=140)
ax2.set_title("Distribution of Roles")

plt.tight_layout()
plt.savefig('dashboard2.png', dpi=200)
print('dashboard2.png')