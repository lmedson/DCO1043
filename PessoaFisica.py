#PessoaFisica.py
from Pessoa import Pessoa

class PessoaFisica(Pessoa):
    cpf = 0
    rg = 0
    def __init__(self, nome, endereco ,renda, cpf, rg, telefone):
        self.cpf = cpf
        self.rg = rg
        Pessoa.__init__(self,nome,endereco,renda,telefone) 

    def exibe(self):
        Pessoa.exibe(self)
        print("RG:", self.rg)
        print("CPF", self.cpf)
        # print("Nome: {} \nEndereco: {} \nRenda: {} \nRG: {} \nTelefone: {}".format(self.nome,self.endereco,self.renda,self.rg,self.telefone))

        
f = PessoaFisica("Juliana Clara", "Rua do Rio 234", "50.000.00","9999","1234567", "84 99999-9999")
f.exibe()
