from app.repositories.entrenador_Repo import crear_entrenador, obtener_todos_los_entrenadores


def registrar_entrenador(nombre, password):
    existe = False

    for entrenador in obtener_todos_los_entrenadores():

        if entrenador.nombre == nombre:
            existe = True

    if existe == False:
        crear_entrenador(nombre, password)


def autenticar_entrenador(nombre, password):

    pass
