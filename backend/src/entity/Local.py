import Entidade

class Local(Entidade):
    
    def __init__(self,nome,rua,bairro,cep,horarioFuncionamento,maxPessoas):
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cep = cep
        self.horarioFuncionamento = horarioFuncionamento
        self.maxPessoas = maxPessoas

    def _getNome(self):
        
        pass