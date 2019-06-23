#-----------------------------------------------------------------------------------------------------------

# Pour commencer, voici ma tentative de création d'un API via Python, Langage que je n'avais jamais
# utilisé auparavant. Il n'est constitué que d'une cinquantaine de ligne. J'ai en cours de route supprimée 
# une partie de mes essais pour garder ce qui semblait le plus utile, selon mon expérience en python.
# Je m'excuse d'avant pour le résultat plus que décevant. La majorité des fonctions ne sont pas fonctionnelle.
# J'avais le goût d'essayer quelque chose de nouveau, peut-être un peu trop nouveau.

# Mes sincères salutations




# Début du code -------------------------------------------


# -----------------------------------
# importation de Flask et de jsonify
# --------------

from flask import Flask, jsonify

# -------------------------------------------
# Appel a FLask pour faire fonctionner l'app
# --------------

app = Flask(__name__)

# -----------------------------------
# importation de l'interpréteur JSON
# --------------

import json

# --------------------------------------------------
# Convertisseur de fichier CSV vers un fichier JSON
# --------------

from jsonify import convert
convert.jsonify('quotes.csv')

# ----------------------------------
# Convertisseur de JSON vers Python
# --------------

with open('quotes.json') as json_file:  
    data = json.load(json_file)

# ---------------------------------------------------------------
# Tantative d'imporation de donnée via URL ** non fonctionnel **
# --------------

@app.route('/stock/quotes/?currency=<currencyType>')
def index(currencyType):
    return jsonify(data[{}]).format(currencyType)

# ---------------------------------------------------
# Tntative d'importation de donnée via la method GET
# --------------

# @app.route('/quotes.json', methods=['GET'])
# def get_currencyType():
#     return ({'currencyType': currencyType})