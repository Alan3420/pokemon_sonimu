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

    def mostrarLog(self, pokemonAtaque,habilidadUsada, pokemonDañado , vidaDañado , dano):
        mensaje = (
            f"___ Turno {self.turno} ___\n"
            f"{pokemonAtaque.name} usó {habilidadUsada} e hizo {dano} de daño. "
            f"{pokemonDañado.name} tiene ahora {vidaDañado} PS."
        )

        self.log.insert(0, mensaje)
        return self.log
    
    # def ejecutarTurno(self, pokemonJugador, pokemonRival, habilidadJugador, hp_Jugador, habilidadRival, hp_rival):
    #     self.turno +=1
    #     if self.get_stat(pokemonJugador, "speed") >= self.get_stat(pokemonRival, "speed"):
    #         primero = {
    #             "name": pokemonJugador,
    #             "habilidad": habilidadJugador,
    #             "hp": hp_Jugador
    #         }
    #         segundo = {
    #             "name": pokemonRival,
    #             "habilidad": habilidadRival,
    #             "hp": hp_rival
    #         }
    #     else :
    #         primero = {
    #             "name": pokemonRival,
    #             "habilidad": habilidadRival,
    #             "hp": hp_rival
    #         }
    #         segundo = {
    #             "name": pokemonJugador,
    #             "habilidad": habilidadJugador,
    #             "hp": hp_Jugador
    #         }

    #     dano = self.calcularDano(primero["name"], primero["habilidad"])
    #     hp_segundo = self.restarHp(segundo["hp"], dano)

    #     self.mostrarLog(primero["name"], primero["habilidad"], segundo["name"], segundo["hp"], dano)

    #     dano = self.calcularDano(segundo["name"], segundo["habilidad"])
    #     hp_primero = self.restarHp(primero["hp"], dano)

    #     self.mostrarLog(segundo["name"], segundo["habilidad"], primero["name"], primero["hp"], dano)


    #     return hp_primero, hp_segundo

    def ejecutarTurno(self, pokemonJugador, pokemonRival, habilidadJugador, hp_Jugador, habilidadRival, hp_rival):
        self.turno +=1

        dano = self.calcularDano(pokemonJugador, habilidadJugador)
        hp_segundo = self.restarHp(hp_rival, dano)

        self.mostrarLog(pokemonJugador, habilidadJugador, pokemonRival, hp_rival, dano)

        dano = self.calcularDano(pokemonRival, habilidadRival)
        hp_primero = self.restarHp(hp_Jugador, dano)

        self.mostrarLog(pokemonRival, habilidadRival, pokemonJugador, hp_Jugador, dano)


        return hp_primero, hp_segundo
        
    def calcularDano(self, pokemonAtaque , habilidad):
        power = self.get_move_stat(pokemonAtaque, habilidad, "power")
        if power is None:
            power = 0
        dano = power*0.10
        return int(dano)
    
    def restarHp(self, hp, dano):
        return hp-dano
    
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