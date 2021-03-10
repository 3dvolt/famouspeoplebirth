### Server Api

run on port 9999
calling localhost:9999/persons?date=2021-10-03 return a json of people with birthday in the day you insert.
The database is populated with data getted from Wikipedia.
# Python Script

before running

<code>pip install sparqlwrapper</code>

The python script run a query on wikidata that get name birthdate occupation and photo of people and store it inside a json.


