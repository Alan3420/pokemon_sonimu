from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class PokemonForm(FlaskForm):
    pokemon = StringField(
        "Introduce el nombre del pokemon",
        validators=[
            DataRequired(message="El campo no puede estar vacío."),
        ]        
    )
    enviar = SubmitField("Enviar")
