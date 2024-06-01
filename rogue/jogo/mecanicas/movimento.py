import random

from jogo.personagens.monstros.thanos import Thanos
from jogo.personagens.monstros.demogorgon import Demogorgon

import pygame

def iniciar_combate(aventureiro, inimigo):
    """
    Executa um loop infinito, que possui as seguintes etapas:
    - Calcula o dano causado pelo aventureiro
    - Monstro faz a sua defesa
    - Exibe na tela o dano causado pelo aventureiro e a vida atual do monstro
    - Se o monstro não está mais vivo, retorna True
    - Calcula o dano causado pelo monstro
    - Aventureiro faz sua defesa
    - Exibe na tela o dano causado pelo monstro e a vida atual do aventureiro
    - Se o aventureiro não está mais vivo, retorna False
    """
    while True:
        dano = aventureiro.atacar()
        inimigo.defender(dano)
        print(f"{aventureiro.nome} causa {dano} de dano! Vida de {inimigo.nome}: {inimigo.vida}")
        if not inimigo.esta_vivo():
            aventureiro.ganhar_xp(inimigo.xp)
            print(f"{inimigo.nome} foi derrotado!")
            return True

        dano = inimigo.atacar()
        aventureiro.defender(dano)
        print(f"{inimigo.nome} causa {dano} de dano! Vida de {aventureiro.nome}: {aventureiro.vida}")
        if not aventureiro.esta_vivo():
            print(f"{aventureiro.nome} foi derrotado!")
            return False

def determina_direcao(teclas):
    if teclas[pygame.K_a]:
        return "A"
    if teclas[pygame.K_w]:
        return "W"
    if teclas[pygame.K_s]:
        return "S"
    if teclas[pygame.K_d]:
        return "D"

    return ""

def verifica_barreiras(posicao, obstaculos):
    x, y = posicao
    if x == -1 or x == 10 or y == -1 or y == 10:
        return True
    for obstaculo in obstaculos:
        if posicao == obstaculo.posicao:
            return True

    return False

def movimentar(aventureiro, teclas, obstaculos):
    """
    Realiza a ação de movimento e analisa as consequências.

    Chama a função aventureiro.andar e analisa o seu resultado.

    Em seguida, analisa o efeito do movimento. Há 60% de chance de nada
    acontecer, e 40% de chance de um monstro aparecer (pesquise sobre a função
    random.choices).

    Se um monstro aparecer, inicia um novo monstro e retorna e resultado da
    função iniciar_combate.

    Se não aconteceu nada, retorna 2.
    Se houve um combate o aventureiro foi vitorioso, retorna 1.
    Se houve um combate e o aventureiro morreu, retorna 0.
    """
    direcao = determina_direcao(teclas)
    if direcao == "":
        return 2, None

    pos_futura = aventureiro.calcular_pos_futura(direcao)
    if verifica_barreiras(pos_futura, obstaculos):
        return 2, None
    aventureiro.andar(pos_futura)

    efeito = random.choices(["nada", "monstro"], [0.6, 0.4])[0]
    if efeito == "monstro":
        monstro = random.choices([Thanos, Demogorgon])[0](aventureiro.dificuldade)
        return int(iniciar_combate(aventureiro, monstro)), monstro.nome

    return 2, None
