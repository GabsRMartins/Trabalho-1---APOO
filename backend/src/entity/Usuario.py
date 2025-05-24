from enum import Enum

class tipoUsuario(Enum):

    ATIVO = 1
    PROMOTOR = 2

class Usuario:
    def __init__(self, nome, senha, tipo):
        self.__nome = nome
        self.__senha = senha
        self.__tipo = self._converterTipo(tipo)

    def _converterTipo(self, tipo_codigo: int) -> tipoUsuario:
        if tipo_codigo == 1:
            return tipoUsuario.ATIVO
        elif tipo_codigo == 2:
            return tipoUsuario.PROMOTOR
        else:
            raise ValueError(f"Código de tipo de usuário inválido: {tipo_codigo}")

    def _getNome(self):
        return self.__nome

    def _getSenha(self):
        return self.__senha
    
    def _setNome(self, nome):
        self.nome = nome   

    def _getTipo(self):
        return self.__tipo

# Depois substituir por um método de cryptografar 
    def setSenha(self, senha):
        self.senha = senha   
