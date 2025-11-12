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
        self.hp_player = self.getStat(datos_pokemon_jugador, 'hp')
        self.hp_rival = self.getStat(datos_pokemon_rival, 'hp')
        self.datos_pokemon_jugador = datos_pokemon_jugador
        self.datos_pokemon_rival = datos_pokemon_rival

    def getStat(self, poke, nombreStat):
        for stat in poke.stats:
            if stat["name"] == nombreStat:
                return stat["value"]

    def getPW(self, poke, nombreMove):
        for move in poke.stats:
            if move["name"] == nombreMove:
                return move["power"]

    def getPC(self, poke, nombreMove):
        for move in poke.stats:
            if move["name"] == nombreMove:
                return move["accuracy"]

    def getName(self, poke):
        for name in poke.stats:
            return name["name"]

    def gethp(self, pokemon):
        if pokemon == self.datos_pokemon_jugador:
            return self.hp_player
        elif pokemon == self.datos_pokemon_rival:
            return self.hp_rival

    def calcularDano(self, atacante, defensor, movimiento):
        ataque = self.getStat(atacante, 'attack')
        defensa = self.getStat(defensor, 'defense')

        dano = (ataque*self.getPW(atacante, movimiento))/defensa
        return round(dano, 1)

    def combate(self, movimiento_jugador, movimiento_rival):

        if self.getStat(self.datos_pokemon_jugador, 'speed') >= self.getStat(self.datos_pokemon_rival, 'speed'):
            primero = {"poke": self.datos_pokemon_jugador,
                       "move": movimiento_jugador}
            segundo = {"poke": self.datos_pokemon_rival,
                       "move": movimiento_rival}
        else:
            primero = {"poke": self.datos_pokemon_rival,
                       "move": movimiento_rival}
            segundo = {"poke": self.datos_pokemon_jugador,
                       "move": movimiento_jugador}

        # Primer ataque
        dano = self.calcularDano(
            primero["poke"], segundo["poke"], primero["move"])
        self.aplicarDano(primero, dano)

        self.log.append(
            f"{primero['poke']} usó {primero['move']} e hizo {dano} de daño.")
        self.log.append(
            f"{segundo['poke']} tiene ahora 10 PS.")

        # Segundo ataque
        if self.hp_player > 0 and self.hp_rival > 0:
            dano = self.calcularDano(
                segundo["poke"], primero["poke"], segundo["move"])
            self.aplicarDano(segundo, dano)

        self.log.append(
            f"{segundo['poke']} usó {segundo['move']} e hizo {dano} de daño.")
        self.log.append(
            f"{primero['poke']} tiene ahora 10 PS.")

    def aplicarDano(self, hace, dano):
        if hace["poke"] == self.datos_pokemon_jugador:
            self.hp_rival -= dano
            if self.hp_rival < 0:
                self.hp_rival = 0
        else:
            self.hp_player -= dano
            if self.hp_player < 0:
                self.hp_player = 0

    # Ejecutar un turno completo

    def ejecutarTurno(self, movimiento_jugador, movimiento_rival):
        self.turno += 1
        self.log.append(f"--- Turno {self.turno} ---")

        self.combate(movimiento_jugador, movimiento_rival)

        self.mostrarLog()

    def mostrarLog(self):
        for entrada in self.log:
            print(entrada)

    # A PARTIR DEL PUNTO DE SESSIONES  no lo entendemos

    def to_dict(self):
        return {
            'turno': self.turno,
            'log': self.log,
            'hp_player': self.hp_player,
            'hp_rival': self.hp_rival,
            'hp_player': self.hp_player,
            'hp_rival': self.hp_rival,
            'pokemon_jugador_name': self.getName(self.datos_pokemon_jugador),
            'pokemon_rival_name': self.getName(self.datos_pokemon_rival),
            'pokemon_rival': self.datos_pokemon_rival,
            'pokemon_jugador': self.datos_pokemon_jugador
        }
