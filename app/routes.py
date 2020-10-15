"""
Module contenant routes
- routes: différentes URL implémentées par l'application.
- view function : dans Flask, les gestionnaires des routes d'application sont écrits sous forme de fonctions Python
- elles sont mappées à une ou pls URL de routage pr que Flask sache quelle logique exécuter qd client demande une URL donnée.
"""
from flask import render_template

from app import app


"""Lorsqu'un navigateur Web dde l'une de ces 2 URL, Flask va appeler la fonction index() 
et en transmettre la valeur de retour au navigateur en tant que réponse."""


@app.route('/')  # view function with route URL
@app.route('/index')  # view function with 'index' as route URL
def index():
    user = {'username': 'Lamia'}
    return render_template('templates/index.html', title='Accueil', user=user)
