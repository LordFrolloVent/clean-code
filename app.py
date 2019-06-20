from flask import Flask, jsonify

import json

from jsonify import convert
convert.jsonify('quotes.csv')

with open('quotes.json') as json_file:  
    data = json.load(json_file)

    print(data)


    


# @app.route('/quotes.json', methods=['GET'])
# def get_tasks():
#     return ({'tasks': tasks})



# with open('quotes.json') as json_file:  
#     data = json.load(json_file)
       
