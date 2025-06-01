from .Usuario import Usuario
from ..service.MapaService import MapaService
from .Mapa import Mapa
from .Evento import Evento
from typing import List

class Ativo(Usuario):

    def __init__(self, nome: str, senha: str, email: str):
        super().__init__(nome, senha, email, tipo=1)

        self.__listaEventos = []

   
    def _acessarMapa(self, mapa: MapaService)-> Mapa:
        return mapa._retornarMapa()

    def _selecionaEventos(self, evento: Evento):

        if evento not in self.listaEventos:
            self.__listaEventos.append(evento)      

    def _retornaEventos(self) -> List[Evento]:
        return self.__listaEventos
    
    def _removerEventos(self, evento: Evento):
        self.__listaEventos.remove(evento)


