import csv
from distutils.log import debug 
from flask import Flask, render_template, jsonify

app = Flask(__name__)

with open("country.csv", "r") as file:
    reader = csv.DictReader(file)
    countries = list(reader)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/countries')
def get_countries():
    return jsonify(countries)

app.run(debug=True)
