from entity import Ativo
from entity.Evento import Evento
from entity.Mapa import Mapa
from typing import List

class AtivoService(Ativo):

    def __init__(self):
        pass
    
    def acessarMapa(self, mapa: Mapa) -> Mapa:
        return super()._acessarMapa(mapa)
    
    def acessarEventos(self, evento: Evento):
        return super()._selecionaEventos(evento)
    
    def retornaEventos(self,) -> List[Evento]:
        return super()._retornaEventos()
    
    def removerEventos(self, evento: Evento):
        return super()._removerEventos(evento)

if __name__ == "__main__":

    from ..entity.Local import Local

    usuario1 = Ativo("João", "ABC1234")

    atvService = AtivoService()

    mapa = Mapa() 

    locais = [Local("Barzinho do Zé", "Rua 1", "Centro", "0123-456", "8:00", 50), Local("Restaurante da Maria", "Rua 2", "Barreiro", "0321-654", "12:00", 100)
            , Local("Hall de Eventos", "Rua 3", "Santa Amélia", "0456-789", "20:00", 200)]
    
    for local in locais:
        mapa._adicionarEntidade(local)

    mapa1 = atvService.acessarMapa(mapa)
    print("Locais cadastrados no mapa: ")
    print(mapa1)