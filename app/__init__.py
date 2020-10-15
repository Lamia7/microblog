from flask import Flask

app = Flask(__name__)

"""contournement aux importations circulaires , un problème courant avec les applications Flask. 
routes module a besoin d'importer la variable app définie dans ce script"""
from app import routes