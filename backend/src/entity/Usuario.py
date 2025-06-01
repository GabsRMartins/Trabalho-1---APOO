from enum import Enum

class tipoUsuario(Enum):

    ATIVO = 1
    PROMOTOR = 2

class Usuario:
    def __init__(self, nome:str, senha:str, email:str ,tipo:tipoUsuario):
        self.nome = nome
        self.email = email
        self.__senha = senha
        self.__tipo = self._converterTipo(tipo)
        self.idTipo = tipo

    def _converterTipo(self, tipo_codigo: int) -> tipoUsuario:
        if tipo_codigo == 1:
            return tipoUsuario.ATIVO
        elif tipo_codigo == 2:
            return tipoUsuario.PROMOTOR
        else:
            raise ValueError(f"Código de tipo de usuário inválido: {tipo_codigo}")

    def _getNome(self) -> str:
        return self.nome

    def _getSenha(self) -> str:
        return self.__senha
    
    def _setNome(self, nome ):
        self.nome = nome   

    def _getTipo(self):
        return self.__tipo

# Depois substituir por um método de cryptografar 
    def _setSenha(self, senha):
        self.__senha = senha   

    def getTipo(self):
        return self.__tipo    
