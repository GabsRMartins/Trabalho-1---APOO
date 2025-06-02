from .Entidade import Entidade


class Evento(Entidade):
    def __init__(self, id: int, nome: str, local_evento: str, horario: str, organizadora: str,
                 preco: float, usuario: int, criado_em: str):
        self.id = id
        self.__nome = nome
        self.__local = local_evento  # Se ainda for string. Se for objeto, você converte aqui.
        self.__horario = horario
        self.organizadora = organizadora
        self.__preco = preco
        self.__usuario = usuario
        self.criado_em = criado_em

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.__nome,
            "local": self.__local,
            "horario": self.__horario,
            "organizadora": self.organizadora,
            "preco": self.__preco,
            "usuario": self.__usuario,
            "criado_em": self.criado_em
        }
    
    def _getNome(self) ->str:
        return self.__nome    
    
    def _getLocal(self):
        return self.__local

    def _getHorario(self):
        return self.__horario
    
    def _getPreco(self):
        return self.__preco
    
    def _getFotos(self):
        return self.__fotos
    
    def _getUsuario(self):
        return self.__usuario
    
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

    def _setUsuario(self,usuario: int):
        self.__usuario = usuario

    def print(self):
        print(self.__nome)    

