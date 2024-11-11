import csv
import json
from pprint import pprint

# Read CSV file
with open("country.csv", "r") as f:
    reader = csv.DictReader(f)
    countries = list(reader)

countries_begging_with_i = []

for country in countries:
    if country["value"].startswith("I"):
        countries_begging_with_i.append(country)

# Convert CSV to JSON
with open("countries_begging_with_i.json", "w") as f:
    json.dump(countries_begging_with_i, f, indent=4)