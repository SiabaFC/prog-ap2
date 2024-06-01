class Monstro:
    def __init__(self):
        raise NotImplementedError

    def atacar(self):
        """
        Retorna o dano do monstro, igual ao seu atributo de força.
        """
        return self.forca

    def defender(self, dano):
        """
        Reduz o dano causado da vida do monstro.
        """
        self.vida -= dano

    def esta_vivo(self):
        """
        Retorna True se a vida do monstro é maior que zero.
        """
        return self.vida > 0
