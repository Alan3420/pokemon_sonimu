from app.repositories.entrenador_Repo import crear_entrenador


def registrar_entrenador(nombre, password):

    crear_entrenador(nombre, password)


def autenticar_entrenador(nombre, password):
