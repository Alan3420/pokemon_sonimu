from flask import Blueprint, redirect, render_template, request, session, url_for
from app.forms.pokemon_form import PokemonForm
from app.forms.trainer_form import TrainerForm
home_pb = Blueprint('home_route', __name__, template_folder='templates')


@home_pb.route('/', methods=['GET', 'POST'])
def Bienvenido():

    form = TrainerForm()

    if form.validate_on_submit():
        session["trainer"] = form.trainer.data
        return redirect(url_for('batalla_route.PokedexS'))

    if form.validate_on_submit():
        session["pokemon"] = form.trainer.data
        return redirect(url_for("batalla_route.BatallaP"))

    return render_template('index.html', form=form)


@home_pb.route('/pickpokemon/<name>', methods=['GET', 'POST'])
def pick_pokemon():
    form = PokemonForm()

    if form.validate_on_submit():
        session["pokemon"] = form.pokemon.data
        return redirect(url_for('batalla_route.BatallaP'))

    return render_template('pickpokemon.html', form=form)
