#PessoaJuridica.py
from Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    cnpj = 0
    def __init__(self, nome, endereco ,renda, cnpj):
        self.cnpj = cnpj
        Pessoa.__init__(self,nome,endereco,renda,cnpj) 

    def exibe(self):
        Pessoa.exibe(self)
        print("cpnj", self.cnpj)


        
f = PessoaJuridica("Juliana Clara", "Rua do Rio 234", "90.000.00","999.999.990")
f.exibe()
