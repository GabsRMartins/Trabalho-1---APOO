from .Entidade import Entidade

class Local(Entidade):
    
    def __init__(self, nome: str, rua: str, bairro: str, cep: str, horarioFuncionamento: str, maxPessoas: int):
        self.__nome = nome
        self.__rua = rua
        self.__bairro = bairro
        self.__cep = cep
        self.__horarioFuncionamento = horarioFuncionamento
        self.__maxPessoas = maxPessoas

    def _getNome(self):
        return self.__nome
    
    def _getRua(self):
        return self.__rua
    
    def _getBairro(self):
        return self.__bairro
    
    def _getCep(self):
        return self.__cep
    
    def _getHorarioFuncionamento(self):
        return self.__horarioFuncionamento
    
    def _getMaxPessoas(self):
        return self.__maxPessoas


    def _setNome(self, nome: str):
        self.__nome = nome

    def _setRua(self, rua: str):
        self.__rua = rua

    def _setBairro(self, bairro: str):
        self.__bairro = bairro

    def _setCep(self, cep: str):
        self.__cep = cep

    def _setHorarioFuncionamento(self, horarioFuncionamento: str):
        self.__horarioFuncionamento = horarioFuncionamento

    def _setMaxPessoas(self, maxPessoas: int):
        self.__maxPessoas = maxPessoas

