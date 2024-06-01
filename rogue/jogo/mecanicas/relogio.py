import time

tempo = 0
tempo_save = 0

def iniciar_tempo():
    global tempo
    tempo = time.time()

def tempo_decorrido():
    total = time.time() - tempo + tempo_save
    minutos = int(total / 60)
    segundos = int(total - minutos * 60)
    return f"{minutos:02d}:{segundos:02d}"

def exportar():
    return {"tempo": time.time() - tempo}

def importar(dados):
    global tempo_save, tempo
    tempo_save = dados["tempo"]
    tempo = time.time()
