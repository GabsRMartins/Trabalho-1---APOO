import Usuario
from service.MapaService import MapaService
from entity import Mapa
from entity import Evento
from typing import List
class Ativo(Usuario):

    def __init__(self, nome: str, senha: str):
        super().__init__(nome, senha, tipo=1)

        self.listaEventos = []

   
    def _acessarMapa(self, mapa: MapaService)-> Mapa:
        return mapa._retornarMapa()

    def _selecionaEventos(self, evento: Evento):

        if evento not in self.listaEventos:
            self.listaEventos.append(evento)      

    def _retornaEventos(self) -> List[Evento]:
        return self.listaEventos
    
    def _removerEventos(self, evento: Evento):
        self.listaEventos.remove(evento)


