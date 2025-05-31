from .Usuario import Usuario
from .Evento import Evento
from ..service.MapaService import MapaService

class Ativo(Usuario):

    def __init__(self, nome: str, senha: str):
        super().__init__(nome, senha, tipo=1)

        self.listaEventos = []

    def _acessarMapa(self, mapa: MapaService):
        return mapa._retornarMapa()

    def _selecionaEvento(self, evento: Evento):

        if evento not in self.listaEventos:
            self.listaEventos.append(evento)      

    def _retornaEvento(self):
        return self.listaEventos
    
    def _removerEvento(self, evento: Evento):
        self.listaEventos.remove(evento)


