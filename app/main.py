from flask import Flask
from app.routes.batalla_routes import batalla_pb
from app.routes.home_routes import home_pb
from app.routes.pokedex_route import pokedex_pb
from flask import Flask, session
from flask_session import Session

app = Flask(__name__, template_folder='templates')
app.secret_key = "pokemonSonimu"

app.config["SESSION_TYPE"] = "filesystem"   # Guardar en ficheros
app.config["SESSION_PERMANENT"] = True     # Sesiones temporales
app.config["SESSION_FILE_DIR"] = "./.flask_session"  # Carpeta donde se guardan
app.secret_key = "clave_super_secreta"

# Inicializar la extensión
Session(app)

app.register_blueprint(batalla_pb, url_prefix='/')
app.register_blueprint(home_pb, url_prefix='/')
app.register_blueprint(pokedex_pb, url_prefix='/pokedex/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
