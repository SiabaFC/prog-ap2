import pygame

from ..gui.buttonbox import ButtonBox

def selecionar_classe(prompt):
    buttonbox = ButtonBox(prompt)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "Aventureiro"

            if evento.type == pygame.MOUSEBUTTONUP:
                coord_clique = pygame.mouse.get_pos()
                match buttonbox.analisar_coord(coord_clique):
                    case "Guerreiro":
                        return "Guerreiro"
                    case "Tank":
                        return "Tank"

        buttonbox.renderizar()
        pygame.time.Clock().tick(60)
