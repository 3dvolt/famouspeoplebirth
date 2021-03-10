# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
import json
from SPARQLWrapper import SPARQLWrapper, JSON
from datetime import date
from datetime import timedelta

today = date.today()
i=0
while True:
    i+=1
    day = today + timedelta(days=i)

    endpoint_url = "https://query.wikidata.org/sparql"

    query = """PREFIX wikibase: <http://wikiba.se/ontology#>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT distinct  ?name ?date ?bornLabel ?occupationLabel ?Photo
    WHERE {  
        ?entityS wdt:P569 ?date .
        ?entityS wdt:P1477 ?name.
        ?entityS wdt:P18 ?Photo .
        ?entityS wdt:P106 ?occupation .
        ?entityS wdt:P19 ?born
    #   select ?occupationLabel ?Photo WHERE {}
        FILTER (datatype(?date) = xsd:dateTime)
        FILTER (month(?date) = %s)
        FILTER (day(?date) = %s)
       SERVICE wikibase:label {
        bd:serviceParam wikibase:language "en" .
      }
      }""" % (day.month,day.day)


    def get_results(endpoint_url, query):
        user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
        sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()


    results = get_results(endpoint_url, query)
    results = results["results"]["bindings"]

    filename = day.strftime("%d-%m") +'.json'

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
        print(filename +" done")

