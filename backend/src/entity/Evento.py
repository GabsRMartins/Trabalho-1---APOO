from .Entidade import Entidade
from .Local import Local

class Evento(Entidade):
    
    def __init__(self, nome: str, horario: str, local: Local, preco: float, fotos: list[str]):
        self.__nome = nome
        self.__horario = horario
        self.__local = local
        self.__preco = preco
        self.__fotos = fotos

    def _getNome(self):
        return self.__nome
    
    def _getHorario(self):
        return self.__horario
    
    def _getLocal(self):
        return self.__local
    
    def _getPreco(self):
        return self.__preco
    
    def _getFotos(self):
        return self.__fotos
    
    def _setNome(self, nome: str):
        self.__nome = nome

    def _setHorario(self,horario: str):
        self.__horario = horario
    
    def _setLocal(self,local: str):
        self.__local = local
    
    def _setPreco(self,preco: float):
        self.__preco = preco
    
    def _setFotos(self,fotos: list[str]):
        self.__fotos = fotos

