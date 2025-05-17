import Entidade
import Local

class Evento(Entidade):
    
    def __init__(self, nome: str,horario: str,local: Local,preco: float,fotos: list):
        self.nome = nome
        self.horario = horario
        self.local = local
        self.preco = preco
        self.fotos = fotos

    def _getHorario(self):
        return self.horario
    
    def _getLocal(self):
        return self.local
    
    def _getPreco(self):
        return self.preco
    
    def _getFotos(self):
        return self.fotos
    
    def _setHorario(self,horario):
        self.horario = horario
    
    def _setLocal(self,local: Local):
        self.local = local
    
    def _setPreco(self,preco):
        self.preco = preco
    
    def _setFotos(self,fotos):
        self.fotos = fotos

