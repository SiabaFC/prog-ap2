import random

from .aventureiro import Aventureiro

class Tank(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome)
        self.char = "T"
        self.vida = random.randint(120, 150)
        self.defesa = random.randint(15, 25)
        self.chars_possiveis.append("T")

    def subir_nivel(self):
        super().subir_nivel()
        self.vida += 15
        self.defesa += 1
