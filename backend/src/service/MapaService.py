from ..entity.Mapa import Mapa
from ..entity.Entidade import Entidade

class MapaService(Mapa):

    def __init__(self):
        pass

    def adicionarEntidade(self, entidade: Entidade):
        super()._adicionarEntidade(entidade)

    def removerEntidade(self, entidade: Entidade):
        super()._removerEntidade(entidade)

    def retornarMapa(self):
        super()._retornarMapa()
