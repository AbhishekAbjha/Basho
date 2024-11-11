import csv
from pprint import pprint

# Read CSV file
with open("country.csv", "r") as f:
    reader = csv.DictReader(f)
    countries = list(reader)

for country in countries:
    if country["value"] == "India":
        pprint(country)
        break


