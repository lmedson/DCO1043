#Pessoa.py
class Pessoa:
    """Classe Pessoa"""
    #Definição dos atributos da Classe   
    nome = ""
    endereco = ""
    renda = 0.0
    #Definição dos Métodos da Classe
    def __init__(self, nome, endereco, renda, telefone = None):
        self.nome = nome
        self.endereco = endereco
        self.renda = renda
        self.telefone = telefone
    def exibe(self):
        print("Nome: ", self.nome)
        print("Endereço: ", self.endereco)
        print("Renda: ", self.renda)
        print("Telefone: ", self.telefone)
