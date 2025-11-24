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

    def __init__(self, datos_pokemon_jugador, movimientosJugador, hp_Jugador, datos_pokemon_rival, movimientosRival, hp_rival, turno=0, log=[]):
        self.turno = turno
        self.log = log
        self.movimientosJugador = movimientosJugador
        self.movimientosRival = movimientosRival
        self.datos_pokemon_jugador = datos_pokemon_jugador
        self.datos_pokemon_rival = datos_pokemon_rival
        self.hp_Jugador = hp_Jugador
        self.hp_rival = hp_rival
    
    def ejecutarTurno(self, pokemonJugador, pokemonRival, habilidadJugador, hp_Jugador, habilidadRival, hp_rival):        
        self.turno +=1
        bloque = []
        bloque.append(f"___ Turno {self.turno} ___")

        if self.get_stat(pokemonJugador, "speed") >= self.get_stat(pokemonRival, "speed"):
            primero = {
                "name": pokemonJugador,
                "habilidad": habilidadJugador,
                "hp": hp_Jugador
            }
            segundo = {
                "name": pokemonRival,
                "habilidad": habilidadRival,
                "hp": hp_rival
            }
        else :
            primero = {
                "name": pokemonRival,
                "habilidad": habilidadRival,
                "hp": hp_rival
            }
            segundo = {
                "name": pokemonJugador,
                "habilidad": habilidadJugador,
                "hp": hp_Jugador
            }

        dano = self.calcularDano(primero["name"], primero["habilidad"])
        segundo["hp"] -= dano

        bloque.append(f"1º: {primero['name'].name} usó {primero['habilidad']} e hizo {dano} de daño. {segundo['name'].name} tiene ahora {segundo["hp"]} PS.")

        dano = self.calcularDano(segundo["name"], segundo["habilidad"])
        primero["hp"] -= dano

        bloque.append(f"2º: {segundo['name'].name} usó {segundo['habilidad']} e hizo {dano} de daño. {primero['name'].name} tiene ahora {primero["hp"]} PS.")
        
        self.log.insert(0, bloque)

        if primero["name"] == pokemonJugador.name:
            return primero["hp"], segundo["hp"]
        else:
            return segundo["hp"], primero["hp"]
        
    def calcularDano(self, pokemonAtaque , habilidad):
        power = self.get_move_stat(pokemonAtaque, habilidad, "power")
        if power is None:
            power = 0
        dano = power*0.10
        return int(dano)
    
    @staticmethod
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
            "hp_rival": self.hp_rival,
            "hp_Jugador": self.hp_Jugador
        }