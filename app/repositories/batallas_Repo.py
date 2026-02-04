from app.database.db import db
from app.models.batalla_bd import batalla_bd
import sqlite3


def crear_batalla(id_entrenador1, id_pokemon1, id_entrenador2, id_pokemon2, resultado):

    # -------------------------------------PENDIENTE--------------------------------------
    # Idea pendiente:  llamo a la funcion de entrenador (obtener_todos_los_entrenadores) para sacar el id de los entrenadores ya que este retorna una
    # lista de los entrenadores que tenemos en la base de datos. (DESCARTADO)

    newBatalla = batalla_bd(id_entrenador1=id_entrenador1, id_pokemon1=id_pokemon1,
                            id_entrenador2=id_entrenador2, id_pokemon2=id_pokemon2, resultado=resultado)

    db.session.add(newBatalla)
    db.session.commit()

    return newBatalla


def obtener_batalla_por_id(id):
    # Hace una consulta en la base de datos filtrando por nombres y toma el primer resultado
    infoBatallaDB = db.session.query(batalla_bd).filter(
        batalla_bd.id_batalla == id).first()

    if infoBatallaDB is None:
        return None


# Segun el ejercicio podriamos meter una varible entrenador para que solo muestre las batallas en las que ese entrenador la a iniciado
def obtener_batallas_por_entrenador(id_entrenador):

    batallas = db.session.query(batalla_bd).filter(
        (batalla_bd.id_entrenador1 == id_entrenador)).all()

    if batallas is None:
        return None

    return batallas


def get_connection():
    conn = sqlite3.connect("data/batallas.db")
    conn.row_factory = sqlite3.Row
    return conn
