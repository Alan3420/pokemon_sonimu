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

    def __init__(self, datos_pokemon_jugador, movimientosJugador, datos_pokemon_rival, movimientosRival, hp_rival, turno=0, log=[]):
        self.turno = turno
        self.log = log
        self.movimientosJugador = movimientosJugador
        self.movimientosRival = movimientosRival
        self.datos_pokemon_jugador = datos_pokemon_jugador
        self.datos_pokemon_rival = datos_pokemon_rival
        self.hp_rival = hp_rival

    def mostrarLog(self, pokemonAtaque,habilidadUsada, pokemonDañado , vidaDañado):
        mensaje = (
            f"___ Turno {self.turno} ___\n"
            f"{pokemonAtaque.name} usó {habilidadUsada} e hizo 10 de daño. "
            f"{pokemonDañado.name} tiene ahora {vidaDañado} PS."
        )

        self.log.insert(0, mensaje)
        return self.log
    
    def calcularDano(self, pokemonAtaque , habilidad, hp_rival):
        self.turno+=1
        power = self.get_move_stat(pokemonAtaque, habilidad, "power")
        dano = power
        hp_restante = hp_rival-int(dano)
        return hp_restante
    
    def get_stat(pokemon, nombre):
        for stat in pokemon.stats:
            if stat["name"] == nombre:
                return stat["value"]
        return 0
    
    def get_move_stat(self,pokemon, move_name, key):
        for move in pokemon.moves:
            if move["name"] == move_name:
                return move.get(key)
        return None


    def to_dict(self):
        return {
            "turno": self.turno,
            "log": self.log,
            "movimientosJugador": self.movimientosJugador,
            "movimientosRival": self.movimientosRival,
            "datos_pokemon_jugador": self.datos_pokemon_jugador,
            "datos_pokemon_rival": self.datos_pokemon_rival,
            "hp_rival": self.hp_rival
        }