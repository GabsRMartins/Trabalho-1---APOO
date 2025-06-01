from ..entity.Evento import Evento
from ....base_de_dados.base_dados import Base_Dados

class EventoService(Evento):

    def __init__(self, evento: Evento):
        self.evento = evento

    def buscarEvento(self, base: Base_Dados):
        try:
            nome_evento = base.get_nome_evento()
            if nome_evento:
                return Evento(nome_evento)
            else:
                return None  # Nenhum evento encontrado
        except Exception as e:
            print(f"Erro ao buscar evento: {e}")
            return None

    def getNome(self):
        return self.evento._getNome()

    def getHorario(self):
        return self.evento._getHorario()
    
    def getLocal(self):
        return self.evento._getLocal()
    
    def getPreco(self):
        return self.evento._getPreco()
    
    def getFotos(self):
        return self.evento._getFotos()
    
    def setNome(self, nome: str):
        self.evento._setNome(nome)

    def setHorario(self, horario: str):
        self.evento._setHorario(horario)

    def setLocal(self, local: str):
        self.evento._setLocal(local)
    
    def setPreco(self, preco: float):
        self.evento._setPreco(preco)
    
    def setFotos(self, fotos: list[str]):
        self.evento._setFotos(fotos)
    
    