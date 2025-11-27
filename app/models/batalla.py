class Batalla():

    def __init__(self, datos_pokemon_jugador, movimientosJugador, hp_Jugador, datos_pokemon_rival, movimientosRival, hp_rival, turno=0, log=[]):
        self.turno = turno
        self.log = log
        self.movimientosJugador = movimientosJugador
        self.movimientosRival = movimientosRival
        self.datos_pokemon_jugador = datos_pokemon_jugador
        self.datos_pokemon_rival = datos_pokemon_rival
        self.hp_Jugador = hp_Jugador
        self.hp_rival = hp_rival
      
    @staticmethod
    def get_stat(pokemon, nombre):
        for stat in pokemon.stats:
            if stat["name"] == nombre:
                return stat["value"]
        return 0


    def to_dict(self):
        return {
            "turno": self.turno,
            "log": self.log,
            "movimientosJugador": self.movimientosJugador,
            "movimientosRival": self.movimientosRival,
            "datos_pokemon_jugador": self.datos_pokemon_jugador,
            "datos_pokemon_rival": self.datos_pokemon_rival,
            "hp_rival": self.hp_rival,
            "hp_Jugador": self.hp_Jugador
        }