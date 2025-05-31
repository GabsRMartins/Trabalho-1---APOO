from ..entity.Evento import Evento
from ....base_de_dados.base_dados import Base_Dados

class EventoService(Evento):

    def __init__(self):
        pass

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
        return super()._getNome()

    def getHorario(self):
        return super()._getHorario()
    
    def getLocal(self):
        return super()._getLocal()
    
    def getPreco(self):
        return super()._getPreco()
    
    def getFotos(self):
        return super()._getFotos()
    
    def setNome(self, nome: str):
        super()._setNome(nome)

    def setHorario(self, horario: str):
        super()._setHorario(horario)

    def setLocal(self, local: str):
        super()._setLocal(local)
    
    def setPreco(self, preco: float):
        super()._setPreco(preco)
    
    def setFotos(self, fotos: list[str]):
        super()._setFotos(fotos)
    
    