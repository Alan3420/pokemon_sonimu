from app.database.db import db
from app.models.trainer import trainer


def crear_entrenador(nombreNewTrainer, newPasswd):

    newTrainer = trainer(nombreNewTrainer, newPasswd, id=None)

    db.session.add(newTrainer)
    db.session.commit()

    return newTrainer


# PENDIENTE...
def obtener_entrenador_por_nombre(nombre):
    infoTrainerDB = db.Query.filter_by(nombre=nombre).all()

    for entrenador in infoTrainerDB:
        entrenador = infoTrainerDB

    # entrenador = trainer()

    return print(entrenador)
