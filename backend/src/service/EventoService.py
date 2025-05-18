from entity.Evento import Evento
from base_de_dados.base_dados import Base_Dados

class EventoService(Evento):

    def __init__(self, horario, local, preco, fotos):
        pass

    def buscarEvento(self, base: Base_Dados):
        try:
            nome_evento = base.get_nome_evento()
            if nome_evento:
                return Evento(nome_evento)
            else:
                return None  # Nenhum usuário encontrado
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None

    def getHorario(self):
        return super()._getHorario()
    
    def getLocal(self):
        return super()._getLocal()
    
    def getPreco(self):
        return super()._getPreco()
    
    def getFotos(self):
        return super()._getFotos()
    
    def setHorario(self, horario):
        super()._setHorario(horario)

    def setLocal(self, local):
        super()._setLocal(local)
    
    def setPreco(self, preco):
        super()._setPreco(preco)
    
    def setFotos(self, fotos):
        super()._setFotos(fotos)
    
    