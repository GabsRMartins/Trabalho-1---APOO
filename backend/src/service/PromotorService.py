from entity import Promotor
from entity import Mapa
from service import EventoService
from entity import Evento
from typing import List

class PromotorService(Promotor):

    def __init__(self):
        pass

    def criarEvento(self, evento: EventoService, mapa: Mapa)->Evento:
        return super()._criarEvento(evento, mapa)
    
    def removerEvento(self, evento:Evento):
        return super()._removerEvento(evento)
    
def listarEventos(self) -> List[Evento]:
    return super()._listarEventos()