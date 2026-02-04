from flask import Blueprint, redirect, render_template, session, url_for
from app.forms.trainer_form import TrainerForm
from app.models.trainer import trainer
from app.repositories import pokemon_Repo
from app.repositories.batallas_Repo import obtener_batallas_por_entrenador
from app.repositories.entrenador_Repo import obtener_entrenador_por_nombre, obtener_todos_los_entrenadores
from app.services.trainer_service import registrar_entrenador, autenticar_entrenador

home_pb = Blueprint('home_route', __name__, template_folder='templates')


@home_pb.route('/', methods=['GET', 'POST'])
def Bienvenido():

    form = TrainerForm()
    verifTrainer = None

    if form.validate_on_submit():
        # Obtencion de los datos del usuario entrenador que añadio en el formulario.
        nombreTrainer = form.trainer.data
        passwdTrainer = form.passwd.data

        entrenador = trainer(nombreTrainer, passwdTrainer)

        verifTrainer = autenticar_entrenador(nombreTrainer, passwdTrainer)
        if verifTrainer == True:
            session["trainer"] = entrenador.to_dict()
            return redirect(url_for('batalla_route.PokedexS'))

    return render_template('index.html', form=form, verifTrainer=verifTrainer)


@home_pb.route('/register', methods=['GET', 'POST'])
def registro():

    form = TrainerForm()

    if form.validate_on_submit():

        # Obtencion de los datos del usuario entrenador que añadio en el formulario.
        nombreTrainer = form.trainer.data
        passwdTrainer = form.passwd.data

        entrenador = trainer(nombreTrainer, passwdTrainer)

        # Recordar que la funcion crear_entrenador crear y retorna el objeto trainer, lo añade a la session y un commit en la bd.
        registrar_entrenador(nombreTrainer, passwdTrainer)

        session["trainer"] = entrenador.to_dict()

        return redirect(url_for('batalla_route.PokedexS'))

    return render_template('registro.html', form=form)


@home_pb.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home_route.Bienvenido'))

# Historial del jugador
# PENDIENTE


@home_pb.route("/historial")
def historial_batallas():
    entrenador_dict = session["trainer"]
    entrenadorJugador = obtener_entrenador_por_nombre(
        entrenador_dict["nombre"])
    historial = obtener_batallas_por_entrenador(entrenadorJugador.id)

    # for batalla in historial:
    #     # print(batalla.info())
    #     pass
    # print(entrenadorJugador.id)

    return render_template("historial.html", listaBatallas=historial,
                           entrenadorJugador=entrenadorJugador,
                           entrenadorContrincante=obtener_todos_los_entrenadores())


# AREA DE PRUEBAS DEL PROYECTO
@home_pb.route("/test")
def listar_productos():
    conn = pokemon_Repo.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, password FROM entrenador ORDER BY id;")

    entrenadores = cur.fetchall()

    cur.close()
    conn.close()

    listaEntrenadores = obtener_todos_los_entrenadores()
    return render_template("error404.html", entrenadores=entrenadores, listaEntrenadores=listaEntrenadores)
