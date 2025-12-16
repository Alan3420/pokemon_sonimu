from sqlalchemy import Column, ForeignKey, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from app.database.db import db
from sqlalchemy.orm import relationship


class trainer(db.Model):
    __tablename__ = "Entrenador"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    batallas = relationship(
        "batalla_bd",
        secondary="Participar",
        back_populates="entrenadores"
    )

    def __init__(self, nombre, password, id=None):
        self.id = id
        self.nombre = nombre
        self.password = generate_password_hash(password)

    def set_password(self, newPassword):
        self.password = generate_password_hash(newPassword)

    def verificar_password(self, passwd):
        return check_password_hash(self.password, passwd)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }
