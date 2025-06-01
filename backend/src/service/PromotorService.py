from ..entity.Promotor import Promotor
from ..entity.Mapa import Mapa
from ..service.EventoService import EventoService

class PromotorService(Promotor):

    def __init__(self, promotor: Promotor):        
        self.promotor = promotor


    def criarEvento(self, evento: EventoService, mapa: Mapa):
        return self.promotor._criarEvento(evento, mapa)
    
    def removerEvento(self, evento):
        return self.promotor._removerEvento(evento)
    
    def listarEventos(self):
        return self.promotor._listarEventos()
    