import random

class Pocao:
    def __init__(self):
        """
        Crie um objeto "poção", que será representado no mapa pelo caractere `%`. Esse objeto deve ser inicializado no início do jogo, e deve ficar visível no mapa enquanto o jogador não tiver passado por ele. Ao chegar no item, um de três possíveis efeitos pode acontecer:
        - Dobra a vida do jogador;
        - Aumenta em 15 a força do jogador;
        - Aumenta em 10 a defesa do jogador;
        """
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if not (x == y == 0):
                break

        self.posicao = [x, y]
        self.ativa = "1"

    def exportar(self):
        return {"posicao": self.posicao, "ativa": self.ativa}

    def importar(self, dados):
        self.posicao = dados["posicao"]
        self.ativa = dados["ativa"]
