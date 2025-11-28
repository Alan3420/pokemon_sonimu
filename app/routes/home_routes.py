from flask import Blueprint, redirect, render_template, session, url_for
from app.forms.trainer_form import TrainerForm
from app.repositories import pokemon_Repo
from app.repositories.entrenador_Repo import obtener_todos_los_entrenadores
from app.services.trainer_service import registrar_entrenador

home_pb = Blueprint('home_route', __name__, template_folder='templates')


@home_pb.route('/', methods=['GET', 'POST'])
def Bienvenido():

    form = TrainerForm()

    if form.validate_on_submit():
        session["trainer"] = form.trainer.data

        # Obtencion de los datos del usuario entrenador que añadio en el formulario.
        nombreTrainer = form.trainer.data
        passwdTrainer = form.passwd.data

        # Recordar que la funcion crear_entrenador crear y retorna el objeto trainer, lo añade a la session y un commit en la bd.
        registrar_entrenador(nombreTrainer, passwdTrainer)
        return redirect(url_for('batalla_route.PokedexS'))

    return render_template('index.html', form=form)


@home_pb.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home_route.Bienvenido'))


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
