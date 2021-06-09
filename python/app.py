"""
Projet de programmation 2021 à l'UNC : application web de vote de départ
"""

import requests
from flask import Flask, render_template
# pylint: disable=no-member

URL = "https://simpsons-quotes-api.herokuapp.com/quotes"

app = Flask(__name__)

def get_citations():
    """Télécharge des citations des Simpsons depuis une API rest publique"""
    app.logger.info("get_citations()")
    resp = requests.get(URL, {"count" : 2})
    if resp.status_code != 200:
        app.logger.error(f"Error: {resp}")
        raise Exception("GET {}".format(resp.status_code))
    citations = resp.json()
    app.logger.info(f"  {citations[0]}")
    app.logger.info(f"  {citations[1]}")
    return citations


@app.route("/")
def index():
    """Racine de l'application : proposer le choix entre 2 personnages"""
    app.logger.info("index()")
    citations = get_citations()
    return render_template("index.html.jinja", citations=citations)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
