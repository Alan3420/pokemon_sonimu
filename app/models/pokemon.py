import datetime
from xmlrpc.client import DateTime
from sqlalchemy import Column, Float, ForeignKey, Integer


class Pokemon:

    def __init__(self, id, name, height, weight, stats, sprites, moves, types):
        self.height = height
        self.id = id
        self.name = name
        self.weight = weight
        self.stats = stats
        self.sprites = sprites
        self.moves = moves
        self.types = types

    def __str__(self):
        return f"{self.name.capitalize()} (ID: {self.id})"
    
# class Compra():
#     __tablename__ = "compras"

#     id = Column(Integer, primary_key=True)

#     num_elemntos = Column(Integer, nullable=False)
#     precio_total = Column(Float, nullable=False)
#     creada_en = Column(DateTime, default=datetime.now, nullable=False)
#     usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)