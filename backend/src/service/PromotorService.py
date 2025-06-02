from entity.Promotor import Promotor
from entity.Mapa import Mapa
from service import EventoService
from entity.Evento import Evento
from typing import List

class PromotorService(Promotor):

    def __init__(self, promotor: Promotor):
        self.promotor = promotor

    def criarEvento(self, evento: EventoService, mapa: Mapa)->Evento:
        return self.promotor._criarEvento(evento, mapa)
    
    def removerEvento(self, evento:Evento):
        return self.promotor._removerEvento(evento)
    
def listarEventos(self) -> List[Evento]:
    return self.promotor._listarEventos()