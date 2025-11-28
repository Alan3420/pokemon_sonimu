from app.database.db import db
from app.models.trainer import trainer


def crear_entrenador(nombreNewTrainer, newPasswd):

    newTrainer = trainer(nombreNewTrainer, newPasswd, id=None)

    db.session.add(newTrainer)
    db.session.commit()

    return newTrainer


# FUNCION  FINALZIADA
def obtener_entrenador_por_nombre(nombre):
    # Hace una consulta en la base de datos filtrando por nombres y toma el primer resultado
    infoTrainerDB = db.session.query(trainer).filter(
        trainer.nombre == nombre).first()

    if infoTrainerDB is None:
        return None

    return infoTrainerDB


def obtener_todos_los_entrenadores():
    listaEntrenadores = db.session.query(trainer).all()

    return listaEntrenadores
