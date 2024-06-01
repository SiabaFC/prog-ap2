import random

from .monstro import Monstro

class Boss(Monstro):
    def __init__(self, dificuldade):
        self.nome = "Boss"
        self.vida = int(dificuldade * random.randint(80, 120))
        self.forca = int(dificuldade * random.randint(15, 30))
        self.defesa = int(dificuldade * random.randint(1, 10))
        self.xp = int(5 * dificuldade)
        print("O boss do mapa apareceu!")

    def defender(self, dano):
        dano_levado = dano - self.defesa
        if dano_levado > 0:
            self.vida -= dano_levado
