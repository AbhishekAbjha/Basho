import csv
import json
from pprint import pprint

INDIA = {
    "id":"IN",
    "value":"India",
}

india_json = json.dumps(INDIA, indent=4)
india_dict = json.loads(india_json)

pprint(india_json)
pprint(india_dict)

# Read CSV file
with open("country.csv", "r") as f:
    reader = csv.DictReader(f)
    countries = list(reader)

# Convert CSV to JSON
with open("country.json", "w") as f:
    json.dump(countries, f, indent=4)