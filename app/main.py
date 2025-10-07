from flask import Flask, render_template, jsonify, current_app
import json
from pathlib import Path

app = Flask(__name__, template_folder='templates')

with open("data/pokemon.json", encoding="utf-8") as f:
    app.config["data"] = json.load(f)
    
@app.route('/')
def Bienvenido():
    return render_template('index.html')

@app.route('/pokedex/')
def Pokedex():
    return render_template('pokemons.html', pokemons = current_app.config["data"])

@app.route('/pokedex/details')
def PokedexDetails():
    return render_template('pokemonsID.html', pokemons = current_app.config["data"])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)