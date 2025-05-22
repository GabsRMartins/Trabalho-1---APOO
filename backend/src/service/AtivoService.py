from entity import Ativo
from entity.Evento import Evento
from entity.Mapa import Mapa
from typing import List

class AtivoService(Ativo):

    def __init__(self, nome: str, senha: str):
        pass
    
    def acessarMapa(self, mapa: Mapa) -> Mapa:
        return super()._acessarMapa(mapa)
    
    def acessarEventos(self, evento: Evento):
        return super()._selecionaEventos(evento)
    
    def retornaEventos(self,) -> List[Evento]:
        return super()._retornaEventos()
    
    def removerEventos(self, evento: Evento):
        return super()._removerEventos(evento)
