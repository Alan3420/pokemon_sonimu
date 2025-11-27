from flask import Blueprint, redirect, render_template, session, url_for
from app.forms.trainer_form import TrainerForm
from app.database.db import db
from app.models.trainer import trainer
home_pb = Blueprint('home_route', __name__, template_folder='templates')


@home_pb.route('/', methods=['GET', 'POST'])
def Bienvenido():

    form = TrainerForm()

    if form.validate_on_submit():
        session["trainer"] = form.trainer.data

        # Obtencion de los datos del usuario entrenador que añadio en el formulario.
        nombreTrainer = form.trainer.data
        passwdTrainer = form.passwd.data

        usuarioTrainer = trainer(nombreTrainer, passwdTrainer, id=None)
        db.session.add(usuarioTrainer)
        db.session.commit()

        return redirect(url_for('batalla_route.PokedexS'))

    return render_template('index.html', form=form)


@home_pb.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home_route.Bienvenido'))
