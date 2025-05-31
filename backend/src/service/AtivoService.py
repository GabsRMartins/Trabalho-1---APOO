from ..entity.Ativo import Ativo
from ..entity.Evento import Evento
from ..entity.Mapa import Mapa
from .MapaService import MapaService
from .LocalService import LocalService

class AtivoService(Ativo):

    def __init__(self, ativo: Ativo):

        self.ativo = ativo
        
    
    def acessarMapa(self, mapa: Mapa):
        return self.ativo._acessarMapa(mapa)
    
    def acessarEventos(self, evento: Evento):
        return self.ativo._selecionaEventos(evento)
    
    def retornaEventos(self):
        return self.ativo._retornaEventos()
    
    def removerEventos(self, evento: Evento):
        return self.ativo._removerEventos(evento)

if __name__ == "__main__":

    from ..entity.Local import Local

    usuario1 = Ativo("João", "ABC1234")

    atvService = AtivoService(usuario1)

    mapa = Mapa()
    mapaService = MapaService(mapa)

    locais = [Local("Barzinho do Zé", "Rua 1", "Centro", "0123-456", "8:00", 50), Local("Restaurante da Maria", "Rua 2", "Barreiro", "0321-654", "12:00", 100)
            , Local("Hall de Eventos", "Rua 3", "Santa Amélia", "0456-789", "20:00", 200)]
    
    for local in locais:
        mapaService.adicionarEntidade(local)

    mapa1 = atvService.acessarMapa(mapa)

    print("Locais cadastrados no mapa: ")
    
    for local in locais:
        localService = LocalService(local)
        print(localService.getNome(), localService.getRua(), localService.getBairro(), localService.getCep(), localService.getHorarioFuncionamento(), localService.getMaxPessoas())
    