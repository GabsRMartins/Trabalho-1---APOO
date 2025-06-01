from entity.Evento import Evento
from base_de_dados.base_dados import Base_Dados
from typing import List

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
        

    def obterEventos(self, base: Base_Dados) -> List[Evento]:
     try:
        lista_eventos_tuplas = base.get_eventos()
        eventos = [
            Evento(*tupla) for tupla in lista_eventos_tuplas
        ]
        print(eventos)
        return eventos
     except Exception as e:
        print(f"Erro ao obter lista de eventos: {e}")
        return [] 

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

    def setHorario(self, horario):
        self.evento._setHorario(horario)

    def setLocal(self, local):
        self.evento._setLocal(local)
    
    def setPreco(self, preco):
        self.evento._setPreco(preco)
    
    def setFotos(self, fotos):
        self.evento._setFotos(fotos)
    
    