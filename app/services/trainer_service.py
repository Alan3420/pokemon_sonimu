from app.repositories.entrenador_Repo import crear_entrenador, obtener_entrenador_por_nombre, obtener_todos_los_entrenadores


def registrar_entrenador(nombre, password):
    # El nombre identifica al entrenador, no puede repetirse
    if obtener_entrenador_por_nombre(nombre) is not None:
        return False

    crear_entrenador(nombre, password)
    return True


def autenticar_entrenador(nombre, password):

    for entrenador in obtener_todos_los_entrenadores():

        if entrenador.nombre == nombre and entrenador.verificar_password(password) == True:
            return True
    
    return False

