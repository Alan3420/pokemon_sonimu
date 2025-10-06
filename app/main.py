from flask import Flask, render_template, jsonify
import json
from pathlib import Path

app = Flask(__name__, template_folder='templates')

with open(Path("data\pokemon.json"), "r", encoding="utf-8") as f:
    DATA = json.load(f)
    
@app.route('/')
def Bienvenido():
    return render_template('index.html')
@app.route('/pokedex')
def home():
    return jsonify(DATA)

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)