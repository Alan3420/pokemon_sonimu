from flask import Flask, render_template, jsonify, current_app
import json
from pathlib import Path

app = Flask(__name__, template_folder='templates')

with open("data/data.json", encoding="utf-8") as f:
    app.config["DATA"] = json.load(f)
    
@app.route('/')
def Bienvenido():
    return render_template('index.html')

@app.route('/pokedex/')
def Pokedex():
    return render_template('pokemons.html'),jsonify(current_app.config["data"])

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)