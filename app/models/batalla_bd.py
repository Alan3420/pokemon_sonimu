from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database.db import db


class Batalla(db.Model):

    __tablename__ = "Batalla"

    id_batalla = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime, default=datetime.now)
    id_entrenador1 = Column(Integer, nullable=False)
    id_pokemon1 = Column(Integer, nullable=False)
    id_entrenador2 = Column(Integer, nullable=False)
    id_pokemon2 = Column(Integer, nullable=False)
    resultado = Column(Boolean, nullable=False)
    entrenadores = relationship(
        "trainer",
        secondary="Participar",
        back_populates="batallas"
    )


class participa(db.Model):
    __tablename__ = "Participar"

    id_Entrenador = Column(Integer, ForeignKey(
        "Entrenador.id"), primary_key=True)
    id_Batalla = Column(Integer, ForeignKey(
        "Batalla.id_batalla"), primary_key=True)
