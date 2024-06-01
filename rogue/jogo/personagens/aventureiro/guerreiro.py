import random

from .aventureiro import Aventureiro

class Guerreiro(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome)
        self.char = "G"
        self.forca = random.randint(20, 30)
        self.chars_possiveis.append("G")

    def subir_nivel(self):
        super().subir_nivel()
        self.forca += 2
