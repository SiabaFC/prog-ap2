import random

class Obstaculo:
    def __init__(self, tesouro, obstaculos):
        pos_preenchidas = [[0, 0], tesouro.posicao] + [obstaculo.posicao for obstaculo in obstaculos]
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if [x, y] not in pos_preenchidas:
                break

        self.posicao = [x, y]

    def exportar(self):
        return {"posicao": self.posicao}

    def importar(self, dados):
        self.posicao = dados["posicao"]
