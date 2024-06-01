from .cores import CORES

import pygame

MARGEM = 10

LARGURA = 400
ALTURA = 100

LARGURA_BOTAO = 150
ALTURA_BOTAO = 50

FONTE = "Courier New"

class ButtonBox:
    def __init__(self, prompt):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")
        self.fonte = pygame.font.SysFont(FONTE, 20)
        self.prompt = prompt

    def renderizar(self):
        self.display.fill(CORES.preto)

        # Desenhar o prompt
        texto = self.fonte.render(self.prompt, True, CORES.branco)
        self.display.blit(texto, [MARGEM, MARGEM])

        # Desenhar os botões
        rect = pygame.Rect(MARGEM, ALTURA - MARGEM - ALTURA_BOTAO, LARGURA_BOTAO, ALTURA_BOTAO)
        pygame.draw.rect(self.display, CORES.branco, rect)

        rect = pygame.Rect(LARGURA - MARGEM - LARGURA_BOTAO, ALTURA - MARGEM - ALTURA_BOTAO, LARGURA_BOTAO, ALTURA_BOTAO)
        pygame.draw.rect(self.display, CORES.branco, rect)

        # Desenhar os textos das classes
        texto = self.fonte.render("Guerreiro", True, CORES.preto)
        x = MARGEM + (LARGURA_BOTAO - texto.get_width()) // 2
        y = ALTURA - MARGEM - ALTURA_BOTAO + (ALTURA_BOTAO - texto.get_height()) // 2
        self.display.blit(texto, [x, y])

        texto = self.fonte.render("Tank", True, CORES.preto)
        x = LARGURA - MARGEM - LARGURA_BOTAO + (LARGURA_BOTAO - texto.get_width()) // 2
        y = ALTURA - MARGEM - ALTURA_BOTAO + (ALTURA_BOTAO - texto.get_height()) // 2
        self.display.blit(texto, [x, y])

        pygame.display.update()

    def analisar_coord(self, coord):
        x, y = coord

        x_g_esq = MARGEM
        x_g_dir = MARGEM + LARGURA_BOTAO

        x_t_esq = LARGURA - MARGEM - LARGURA_BOTAO
        x_t_dir = LARGURA - MARGEM

        y_inf = ALTURA - MARGEM - ALTURA_BOTAO
        y_sup = ALTURA - MARGEM

        if x_g_esq <= x <= x_g_dir and y_inf <= y <= y_sup:
            return "Guerreiro"

        if x_t_esq <= x <= x_t_dir and y_inf <= y <= y_sup:
            return "Tank"

        return ""
