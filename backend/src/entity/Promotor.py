import Usuario
import Mapa
from service import EventoService
from service import MapaService

class Promotor(Usuario):

    def __init__(self,nome: str, senha: str):
        super.__init__(nome,senha)
        self.eventos = []

    def _criarEvento(self, evento: EventoService, mapa: Mapa):
        evento.adicionarEvento(mapa)
        return evento

    def _removerEvento(self, evento):            
