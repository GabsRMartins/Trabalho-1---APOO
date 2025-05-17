from entity import Promotor
from entity import Mapa
from service import EventoService

class PromotorService(Promotor):

    def __init__(self):
        pass

    def criarEvento(self, evento: EventoService, mapa: Mapa):
        return super()._criarEvento(evento, mapa)
    
    def removerEvento(self, evento):
        return super()._removerEvento(evento)
    
    def listarEventos(self):
        return super()._listarEventos()
    