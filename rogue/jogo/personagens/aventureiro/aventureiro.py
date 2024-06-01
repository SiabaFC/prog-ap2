import random

from ...mecanicas import som
from ...gui.cores import CORES

CORES_POSSIVEIS = [CORES.branco, CORES.vermelho, CORES.verde, CORES.azul]

def pega_prox_valor(lista, valor_atual):
    ind = lista.index(valor_atual) + 1
    if ind == len(lista):
        ind = 0

    return lista[ind]

class Aventureiro:
    def __init__(self, nome):
        self.nome = nome

        self.vida = random.randint(100, 120)
        self.forca = random.randint(10, 18)
        self.defesa = random.randint(10, 18)
        self.posicao = [0, 0]

        self.cor = CORES.branco
        self.char = "@"
        self.chars_possiveis = ["@", "#", "$", "&"]

        self.dificuldade = 1

        self.xp = 0
        self.nivel = 1
        self.xp_por_nivel = 5

    def exportar(self):
        return {
            "nome": self.nome,
            "vida": self.vida,
            "forca": self.forca,
            "defesa": self.defesa,
            "posicao": self.posicao,
            "cor": self.cor,
            "char": self.char,
            "chars_possiveis": self.chars_possiveis,
            "dificuldade": self.dificuldade,
            "xp": self.xp,
            "nivel": self.nivel,
            "xp_por_nivel": self.xp_por_nivel,
            "classe": self.__class__.__name__
        }

    def importar(self, dados):
        self.nome = dados["nome"]

        self.vida = dados["vida"]
        self.forca = dados["forca"]
        self.defesa = dados["defesa"]
        self.posicao = dados["posicao"]

        self.cor = dados["cor"]
        self.char = dados["char"]
        self.chars_possiveis = dados["chars_possiveis"]

        self.dificuldade = dados["dificuldade"]

        self.xp = dados["xp"]
        self.nivel = dados["nivel"]
        self.xp_por_nivel = dados["xp_por_nivel"]

    def ganhar_xp(self, valor):
        self.xp += valor
        if self.xp >= self.xp_por_nivel:
            self.xp -= self.xp_por_nivel
            self.subir_nivel()

    def subir_nivel(self):
        som.level_up()
        self.nivel += 1
        self.vida += 50
        self.forca += 1
        self.defesa += 1
        self.aumentar_dificuldade()
        self.xp_por_nivel = int(self.xp_por_nivel * 1.2)

    def aumentar_dificuldade(self):
        self.dificuldade *= 1.1
        print(f"Aumentando dificuldade para {self.dificuldade:.3f}")

    def diminuir_dificuldade(self):
        self.dificuldade /= 1.1
        print(f"Reduzindo dificuldade para {self.dificuldade:.3f}")

    def mudar_cor(self):
        self.cor = pega_prox_valor(CORES_POSSIVEIS, self.cor)

    def mudar_char(self):
        self.char = pega_prox_valor(self.chars_possiveis, self.char)

    def calcular_pos_futura(self, direcao):
        x, y = self.posicao
        match direcao:
            case "W":
                y -= 1
            case "S":
                y += 1
            case "A":
                x -= 1
            case "D":
                x += 1

        return [x, y]

    def andar(self, nova_posicao):
        self.posicao = nova_posicao

    def atacar(self):
        """
        Retorna um inteiro igual à Força do aventureiro, mais um valor aleatório
        entre 1 e 6.
        """
        return self.forca + random.randint(1, 6)

    def defender(self, dano):
        """
        Calcula o dano a ser absorvido pelo aventureiro, igual ao dano causado
        menos o atributo de defesa do aventureiro.

        Se o dano a ser absorvido é menor ou igual a zero, não faz nada. Se for
        maior que zero, reduz esse dano da vida do aventureiro.
        """
        dano_levado = dano - self.defesa
        if dano_levado > 0:
            self.vida -= dano_levado

    def esta_vivo(self):
        """
        Retorna True se a vida do aventureiro é maior que zero.
        """
        return self.vida > 0
