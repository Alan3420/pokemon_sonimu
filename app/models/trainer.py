from werkzeug.security import generate_password_hash, check_password_hash


class trainer:
    def __init__(self, id, nombre, password):
        self.id = id
        self.nombre = nombre
        self.password = generate_password_hash(password)

    def set_password(self, newPassword):
        self.password = generate_password_hash(newPassword)

    def verificar_password(self, passwd):
        return check_password_hash(self.password, passwd)
