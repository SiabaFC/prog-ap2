import os
import os.path

import pygame

CAMINHO = os.path.join(os.getcwd(), "assets", "som")

def iniciar_musica():
    pygame.mixer.music.load(os.path.join(CAMINHO, "tema.ogg"))
    pygame.mixer.music.play(-1)

def level_up():
    audio = pygame.mixer.Sound(os.path.join(CAMINHO, "levelup.wav"))
    audio.play()
