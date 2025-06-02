from entity.Mapa import Mapa
from entity.Entidade import Entidade

class MapaService(Mapa):

    def __init__(self, mapa: Mapa):
        self.mapa = mapa

    def adicionarEntidade(self, entidade: Entidade):
        self.mapa._adicionarEntidade(entidade)

    def removerEntidade(self, entidade: Entidade):
        self.mapa._removerEntidade(entidade)

    def retornarMapa(self):
        self.mapa._retornarMapa()
