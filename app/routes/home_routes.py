from flask import Blueprint, redirect, render_template, request, session, url_for
from app.forms.trainer_form import TrainerForm
home_pb = Blueprint('home_route', __name__, template_folder='templates')


@home_pb.route('/', methods=['GET', 'POST'])
def Bienvenido():

    form = TrainerForm()

    if form.validate_on_submit():
        session["trainer"] = form.trainer.data
        return redirect(url_for('batalla_route.PokedexS'))

    return render_template('index.html', form=form)

@home_pb.route("/logout")
def logout():
    session.clear()
    return "Sesión cerrada. Hasta pronto."