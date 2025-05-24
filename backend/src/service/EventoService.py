from entity.Evento import Evento
from base_de_dados.base_dados import Base_Dados
from typing import List

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
        

    def obterEventos(self, base: Base_Dados) -> List[Evento]:
     try:
        lista_eventos_tuplas = base.get_eventos()
        eventos = [
            Evento(*tupla) for tupla in lista_eventos_tuplas
        ]
        return eventos
     except Exception as e:
        print(f"Erro ao obter lista de eventos: {e}")
        return [] 

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
    
    