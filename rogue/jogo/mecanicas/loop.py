import time

from jogo.gui.tela import Tela

from . import movimento
from . import inputbox
from . import buttonbox
from . import arquivo

from jogo.personagens.monstros.boss import Boss
from jogo.personagens.aventureiro.aventureiro import Aventureiro
from jogo.personagens.aventureiro.guerreiro import Guerreiro
from jogo.personagens.aventureiro.tank import Tank
from jogo.personagens.tesouro import Tesouro
from jogo.personagens.obstaculo import Obstaculo

import pygame

def jogo():
    tesouro = Tesouro()

    nome = inputbox.ler_texto("Informe o seu nome:")
    classe = buttonbox.selecionar_classe("Clique na classe desejada:")

    match classe:
        case "Aventureiro":
            jogador = Aventureiro(nome)
        case "Guerreiro":
            jogador = Guerreiro(nome)
        case "Tank":
            jogador = Tank(nome)

    print(f"Saudações, {jogador.nome}! Boa sorte!")

    obstaculos = []
    for _ in range(5):
        obstaculos.append(Obstaculo(tesouro, obstaculos))

    tela = Tela()

    mensagem_combate = ""
    jogo_acabou = False
    while not jogo_acabou:
        # Controlar os eventos
        teclas = pygame.key.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYUP:
                if teclas[pygame.K_q]:
                    print("Já correndo?")
                    jogo_acabou = True

                if teclas[pygame.K_p]:
                    arquivo.salvar(jogador, tesouro, obstaculos)
                elif teclas[pygame.K_o]:
                    if arquivo.save_existe():
                        jogador, tesouro, obstaculos = arquivo.carregar()
                elif teclas[pygame.K_z]:
                    jogador.mudar_cor()
                elif teclas[pygame.K_x]:
                    jogador.mudar_char()
                elif teclas[pygame.K_KP_PLUS]:
                    jogador.aumentar_dificuldade()
                elif teclas[pygame.K_KP_MINUS]:
                    jogador.diminuir_dificuldade()
                else:
                    # Executar as ações do jogo
                    resultado, nome_monstro = movimento.movimentar(jogador, teclas, obstaculos)
                    if resultado == 0:
                        mensagem_combate = f"Você foi derrotado por {nome_monstro}..."
                        jogo_acabou = True
                    elif resultado == 1:
                        mensagem_combate = f"{nome_monstro} foi derrotado!"
                    else:
                        mensagem_combate = "Você não encontrou nada"

                    if jogador.posicao == tesouro.posicao:
                        boss = Boss(jogador.dificuldade)
                        if movimento.iniciar_combate(jogador, boss):
                            mensagem_combate = f"Parabéns, {jogador.nome}, você encontrou o tesouro!"
                        else:
                            mensagem_combate = f"Você foi derrotado pelo chefão... =("

                        jogo_acabou = True

        # Desenho na tela
        tela.renderizar(jogador, tesouro, mensagem_combate, obstaculos)

        # Chamar o relógio interno do jogo
        pygame.time.Clock().tick(60)

    time.sleep(2)
