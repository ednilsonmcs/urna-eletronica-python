class Candidato:
    def __init__(self, id, nome, cargo, numero, partido):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.numero = numero
        self.partido = partido

    def saudacao(self):
        print("Olá, meu nome é", self.nome)
