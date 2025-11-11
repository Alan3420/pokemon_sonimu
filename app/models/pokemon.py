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

    def __init__(self, datos_pokemon_jugador, datos_pokemon_rival):
        self.turno = 0
        self.log = []
        self.hp_player = self.getStat(datos_pokemon_jugador, 'hp')
        self.hp_rival = self.getStat(datos_pokemon_rival, 'hp')
        self.datos_pokemon_jugador = datos_pokemon_jugador
        self.datos_pokemon_rival = datos_pokemon_rival

    def getStat(self, poke, nombreStat):
        for stat in poke.stats:
            if stat["name"] == nombreStat:
                return stat["value"]

    def getPW(self, poke ,nombreMove):
        for move in poke.stats:
            if move["name"] == nombreMove:
                return move["power"]
            
    def getPC(self, poke, nombreMove):
        for move in poke.stats:
            if move["name"] == nombreMove:
                return move["accuracy"]                

    def dañoInflingido(self, golpea, recibe, movimiento):

        if self.getStat(self.datos_pokemon_jugador, 'speed') > self.getStat(self.datos_pokemon_rival, 'speed'):
            golpea = self.datos_pokemon_jugador
            recibe = self.datos_pokemon_rival
        else:
            recibe = self.datos_pokemon_jugador
            golpea = self.datos_pokemon_rival

        # daño simple = daño base * (ataque / defensa)
        dano = (self.getStat(golpea, 'attack')*self.getPW(golpea, movimiento))/self.getStat(recibe, 'defense')
        return dano

    def siguienteTurno(self, movimiento, dano):

        self.turno += 1
        self.hp_rival -= dano
        self.log.append(f"--- Turno {self.turno} ---")

        mensaje = (
            f"{self.datos_pokemon_jugador.name} utilizó {movimiento}. "
            f"{self.datos_pokemon_rival.name} ha perdido {dano} puntos de salud. "
            f"PS restantes: {self.hp_rival - dano}."
        )
        self.log.append(mensaje)
        

    def mostrarLog(self):
        for entrada in self.log:
            print(entrada)
