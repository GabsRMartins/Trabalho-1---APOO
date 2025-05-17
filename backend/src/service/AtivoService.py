from entity import Ativo
from entity.Evento import Evento
from entity.Mapa import Mapa

class AtivoService(Ativo):

    def __init__(self, nome: str, senha: str):
        pass
    
    def acessarMapa(self, mapa: Mapa):
        return super()._acessarMapa(mapa)
    
    def acessarEventos(self, evento: Evento):
        return super()._selecionaEventos(evento)
    
    def retornaEventos(self):
        return super()._retornaEventos()
    
    def removerEventos(self, evento: Evento):
        return super()._removerEventos(evento)
