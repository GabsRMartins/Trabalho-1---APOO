import Usuario
from service.MapaService import MapaService
from entity import Mapa
from entity import Evento
from typing import List
class Ativo(Usuario):

    def __init__(self,nome,senha):
        super.__init__(nome,senha)

        self.listaEventos = []

    def _acessarMapa(self, mapa: MapaService)-> Mapa:
        return mapa.retornaMapa()

    def _selecionaEventos(self, evento):

        # evento = buscarEvento(evento)
        self.listaEventos.append(evento)        

    def _retornaEventos(self) -> List[Evento]:
        return self.listaEventos
    
    def _removerEventos(self, evento):
        self.listaEventos.remove(evento)



