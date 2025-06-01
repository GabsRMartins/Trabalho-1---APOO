from entity.Entidade import Entidade
from entity.Local import Local


class Evento(Entidade):
    def __init__(self, id: int, nome: str, local_evento: str, horario: str, organizadora: str,
                 preco: float, usuario: int, criado_em: str):
        self.id = id
        self.nome = nome
        self.local = local_evento  # Se ainda for string. Se for objeto, você converte aqui.
        self.horario = horario
        self.organizadora = organizadora
        self.preco = preco
        self.__usuario = usuario
        self.criado_em = criado_em

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "local": self.local,
            "horario": self.horario,
            "organizadora": self.organizadora,
            "preco": self.preco,
            "usuario": self.__usuario,
            "criado_em": self.criado_em
        }
    def _getNome(self) -> str:
        return self.nome
    def _getHorario(self):
        return self.__horario
    
    def _getLocal(self):
        return self.__local
    
    def _getPreco(self):
        return self.__preco
    
    def _getFotos(self):
        return self.__fotos
    
    def _setNome(self, nome: str):
        self.__nome = nome

    def _setHorario(self,horario: str):
        self.__horario = horario
    
    def _setLocal(self,local: str):
        self.__local = local
    
    def _setPreco(self,preco: float):
        self.__preco = preco
    
    def _setFotos(self,fotos: list[str]):
        self.__fotos = fotos

    def print(self):
        print(self.nome)    

