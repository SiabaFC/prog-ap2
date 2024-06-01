import os
import json
import os.path

from . import relogio

from ..personagens.aventureiro.aventureiro import Aventureiro
from ..personagens.aventureiro.guerreiro import Guerreiro
from ..personagens.aventureiro.tank import Tank
from ..personagens.tesouro import Tesouro
from ..personagens.obstaculo import Obstaculo

CAMINHO = os.path.join(os.getcwd(), "out", "save.json")

def save_existe():
    return os.path.isfile(CAMINHO)

def salvar(aventureiro, tesouro, obstaculos):
    dados = {
        "aventureiro": aventureiro.exportar(),
        "tesouro": tesouro.exportar(),
        "tempo": relogio.exportar(),
        "obstaculos": [obstaculo.exportar() for obstaculo in obstaculos]
    }
    with open(CAMINHO, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def carregar():
    with open(CAMINHO, "r") as arquivo:
        dados = json.load(arquivo)

    relogio.importar(dados["tempo"])

    tesouro = Tesouro()
    tesouro.importar(dados["tesouro"])

    obstaculos = []
    for dado in dados["obstaculos"]:
        obstaculos.append(Obstaculo(tesouro, obstaculos))
        obstaculos[-1].importar(dado)

    classe = dados["aventureiro"]["classe"]
    match classe:
        case "Guerreiro":
            aventureiro = Guerreiro(dados["aventureiro"]["nome"])
        case "Tank":
            aventureiro = Tank(dados["aventureiro"]["nome"])
        case _:
            aventureiro = Aventureiro(dados["aventureiro"]["nome"])
    aventureiro.importar(dados["aventureiro"])

    return aventureiro, tesouro, obstaculos
