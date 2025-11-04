from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TrainerForm(FlaskForm):
    trainer = StringField(
        "Introduce el nombre del entrenador",
        validators=[
            DataRequired(message="El campo no puede estar vacío."),
            Length(min=3, max=15, message="Debe tener entre 3 y 15 caracteres.")
        ]
    )
    enviar = SubmitField("Enviar")
