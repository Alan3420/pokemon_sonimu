from flask import Blueprint, redirect, render_template, request, session, url_for
from app.forms.trainer_form import TrainerForm
home_pb = Blueprint('home_route',__name__,template_folder='templates')

@home_pb.route('/')
def Bienvenido():

    form = TrainerForm()

    if form.validate_on_submit():
        return redirect(url_for('batalla_pb.pokedexSeleccion'))
    
    return render_template('index.html', form=form)