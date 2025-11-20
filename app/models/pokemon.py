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
    
class Batalla():

    def __init__(self, datos_pokemon_jugador, datos_pokemon_rival):
        self.turno = 0
        self.log = []
        self.datos_pokemon_jugador = datos_pokemon_jugador
        self.datos_pokemon_rival = datos_pokemon_rival

    def mostrarLog(self, pokemonAtaque, pokemonDañado):
        self.log.append(
        f"{pokemonAtaque} usó lanzallams e hizo 10 de daño."
        f"{pokemonDañado} tiene ahora 10 PS.")
        return self.log