# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"

query = """#title: Visual Timeline of exhibitions at the Sprengel Museum
#defaultView:Timeline
SELECT ?exhibition ?exhibitionLabel ?date ?image WHERE {
  ?exhibition wdt:P31/wdt:P279* wd:Q464980; # Instance of or subclass of exhibition
              wdt:P276 wd:Q510144.          # Location: Sprengel Museum
  
  # Check for either inception or start time
  OPTIONAL { ?exhibition wdt:P571 ?date. }
  OPTIONAL { ?exhibition wdt:P580 ?date. }
  
  # Fetch the image if it exists
  OPTIONAL { ?exhibition wdt:P18 ?image. }
  
  FILTER(BOUND(?date)) # Ensures a date exists for the timeline
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en,de". }
}
ORDER BY ?date"""


def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)

for result in results["results"]["bindings"]:
    print(result)
