class Pokemon:

    def __init__(self, id, name, height, weight, stats , sprites, moves, types):
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
    
class Batalla():

    def __init__(self, datos_pokemon_jugador, datos_pokemon_rival, hp_player, hp_rival):
        self.turno = 0
        self.log = []
        self.hp_player = hp_player
        self.hp_rival = hp_rival
        self.datos_pokemon_jugador = datos_pokemon_jugador
        self.datos_pokemon_rival = datos_pokemon_rival

    def siguienteTurno(self):
        self.turno += 1
        self.log.append(f"--- Turno {self.turno} ---")

    def dañoInflingido(self, golpea, recibe, movimiento):

        if self.datos_pokemon_jugador.stats["speed"].values > self.datos_pokemon_rival.stats["speed"].values:
            golpea = self.datos_pokemon_jugador
            recibe = self.datos_pokemon_rival
        else:
            recibe = self.datos_pokemon_jugador
            golpea = self.datos_pokemon_rival

        # daño simple = daño base * (ataque / defensa)
        dano = (golpea.stats["attack"].values*movimiento["power"].values)/recibe.stats["defense"].values
        return dano

    def formatMovimientoLog(self, movimiento, dano):
        mensaje = (
            f"{self.datos_pokemon_jugador.name} utilizó {movimiento}. "
            f"{self.datos_pokemon_rival.name} ha perdido {dano} puntos de salud. "
            f"PS restantes: {self.hp_rival - dano}."
        )
        self.log.append(mensaje)
        self.hp_rival -= dano

    def mostrarLog(self):
        for entrada in self.log:
            print(entrada)
