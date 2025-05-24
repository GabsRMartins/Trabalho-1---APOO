from .Usuario import Usuario
from .Mapa import Mapa
from ..service.EventoService import EventoService
from ..service.MapaService import MapaService

class Promotor(Usuario):

    def __init__(self, nome: str, senha: str):
        super.__init__(nome,senha)
        self.eventos = []

    def _criarEvento(self, evento: EventoService, mapa: Mapa):
        evento.adicionarEvento(mapa)
        return evento

    def _removerEvento(self, evento):            
        evento.removerEvento()

        