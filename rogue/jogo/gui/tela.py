from .cores import CORES

from ..mecanicas import relogio

import pygame

GRID = 40
TAMANHO_MAPA = 10

LARGURA_ADICIONAL = 500
ALTURA_ADICIONAL = 100
MARGEM = 10

LARGURA = TAMANHO_MAPA * GRID + LARGURA_ADICIONAL
ALTURA = TAMANHO_MAPA * GRID + ALTURA_ADICIONAL

FONTE = "Courier New"

def centralizar_texto_mapa(posicao_inicial, texto):
    x0 = posicao_inicial[0] * GRID + (GRID - texto.get_width()) // 2
    y0 = posicao_inicial[1] * GRID + (GRID - texto.get_height()) // 2
    return [x0 + LARGURA_ADICIONAL // 2, y0 + ALTURA_ADICIONAL // 2]

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")

    def renderizar(self, aventureiro, tesouro, mensagem_combate, obstaculos):
        self.display.fill(CORES.preto)
        self.aventureiro(aventureiro)
        self.tesouro(tesouro)
        self.obstaculos(obstaculos)
        self.mapa(aventureiro, tesouro, obstaculos)
        self.combate(mensagem_combate)
        self.cronometro()

        pygame.display.update()

    def cronometro(self):
        tempo = relogio.tempo_decorrido()
        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        texto = fonte.render(tempo, True, CORES.branco)
        self.display.blit(texto, [LARGURA - MARGEM - texto.get_width(), MARGEM])

    def obstaculos(self, obstaculos):
        for obstaculo in obstaculos:
            self.desenha_mensagem("O", obstaculo.posicao)

    def combate(self, mensagem_combate):
        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        texto = fonte.render(mensagem_combate, True, CORES.branco)
        self.display.blit(texto, [MARGEM, MARGEM])

    def desenha_mensagem(self, mensagem, posicao, cor=CORES.branco):
        fonte = pygame.font.SysFont(FONTE, GRID)
        texto = fonte.render(mensagem, True, cor)
        self.display.blit(texto, centralizar_texto_mapa(posicao, texto))

    def aventureiro(self, aventureiro):
        self.desenha_mensagem(aventureiro.char, aventureiro.posicao, aventureiro.cor)

        atributos = f"{aventureiro.nome} nv. {aventureiro.nivel} ({aventureiro.xp}/{aventureiro.xp_por_nivel}): " \
            f"vida {aventureiro.vida}; força {aventureiro.forca}; defesa {aventureiro.defesa}"

        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        texto = fonte.render(atributos, True, CORES.branco)

        y = GRID * TAMANHO_MAPA + ALTURA_ADICIONAL - MARGEM - texto.get_height()
        self.display.blit(texto, [MARGEM, y])

    def tesouro(self, tesouro):
        self.desenha_mensagem("X", tesouro.posicao)

    def mapa(self, aventureiro, tesouro, obstaculos):
        for linha in range(TAMANHO_MAPA):
            for coluna in range(TAMANHO_MAPA):
                pos_preenchidas = [aventureiro.posicao, tesouro.posicao]
                for obstaculo in obstaculos:
                    pos_preenchidas.append(obstaculo.posicao)
                if [linha, coluna] not in pos_preenchidas:
                    self.desenha_mensagem(".", [linha, coluna])
