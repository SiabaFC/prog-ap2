from .cores import CORES

import pygame

MARGEM = 10

LARGURA = 400
ALTURA = 100

FONTE = "Courier New"

class InputBox:
    def __init__(self, prompt):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")
        self.fonte = pygame.font.SysFont(FONTE, 20)
        self.prompt = prompt

    def renderizar(self, nome):
        self.display.fill(CORES.preto)

        # Renderizar o prompt
        texto = self.fonte.render(self.prompt, True, CORES.branco)
        self.display.blit(texto, [MARGEM, MARGEM])

        # Renderizar o nome
        texto = self.fonte.render(nome, True, CORES.branco)
        self.display.blit(texto, [2 * MARGEM, ALTURA - 2 * MARGEM - texto.get_height()])

        # Renderizar a caixa de texto
        rect = pygame.Rect(MARGEM, ALTURA - MARGEM - 40, LARGURA - 2 * MARGEM, 40)
        pygame.draw.rect(self.display, CORES.branco, rect, 3)

        pygame.display.update()


