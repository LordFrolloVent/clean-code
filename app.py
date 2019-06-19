from flask import Flask, jsonify

import json


app = Flask(__name__)

from jsonify import convert
convert.jsonify('quotes.csv')


@app.route('/quotes.json', methods=['GET'])
def get_tasks():
    return ({'tasks': tasks})



with open('quotes.json') as json_file:  
    data = json.load(json_file)
        