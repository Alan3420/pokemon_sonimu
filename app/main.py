from flask import Flask
from app.routes.batalla_routes import batalla_pb
from app.routes.home_routes import home_pb
from app.routes.pokedex_route import pokedex_pb
from flask_session import Session
# from app.database import db

app = Flask(__name__, template_folder='templates')
app.secret_key = "pokemonSonimu"
# Configuracion session
app.config["SESSION_TYPE"] = "filesystem"   # Guardar en ficheros
app.config["SESSION_PERMANENT"] = True     # Sesiones temporales
app.config["SESSION_FILE_DIR"] = "./.flask_session"  # Carpeta donde se guardan

# Configuracion alchemy
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////data/pokemons.db.sqlite"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Clave session
app.secret_key = "clave_super_secreta"

# Inicializar la extensión
Session(app)
# db.init_app(app)

app.register_blueprint(batalla_pb, url_prefix='/')
app.register_blueprint(home_pb, url_prefix='/')
app.register_blueprint(pokedex_pb, url_prefix='/pokedex/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
