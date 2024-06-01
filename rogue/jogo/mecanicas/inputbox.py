import pygame

from ..gui.inputbox import InputBox

def ler_texto(prompt):
    inputbox = InputBox(prompt)

    nome = ""
    while True:
        teclas = pygame.key.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return nome

            if evento.type == pygame.KEYUP:
                if teclas[pygame.K_RETURN]:
                    return nome

                if teclas[pygame.K_BACKSPACE]:
                    nome = nome[:-1]
                else:
                    if len(nome) < 25:
                        nome += evento.unicode

        inputbox.renderizar(nome)
        pygame.time.Clock().tick(60)
