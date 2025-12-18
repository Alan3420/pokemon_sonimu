from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database.db import db


class batalla_bd(db.Model):

    __tablename__ = "batalla"

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

    def info(self):
        return self.id_batalla, self.fecha, self.id_entrenador1, self.id_pokemon1, self.id_entrenador2, self.id_pokemon2, self.resultado


class participa(db.Model):
    __tablename__ = "Participar"

    id_Entrenador = Column(Integer, ForeignKey(
        "Entrenador.id"), primary_key=True)
    id_Batalla = Column(Integer, ForeignKey(
        "batalla.id_batalla"), primary_key=True)
