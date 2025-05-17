import Entidade

class Local(Entidade):
    def __init__(self,rua,bairro,cep,horarioFuncionamento,proximoEvento,maxPessoas,):
        self.rua = rua
        self.bairro = bairro
        self.cep = cep
        self.horarioFuncionamento = horarioFuncionamento
        self.proximoEvento = proximoEvento
        self.maxPessoas = maxPessoas