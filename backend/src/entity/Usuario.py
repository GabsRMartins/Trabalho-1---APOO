from enum import Enum

class tipoUsuario(Enum):

    COMUM = 1
    PROMOTOR = 2

class Usuario:
    def __init__(self, nome, senha, tipo):
        self.nome = nome
        self.senha = senha
        self.__tipo = self._converter_tipo(tipo)

    def _converter_tipo(self, tipo_codigo: int) -> tipoUsuario:
        if tipo_codigo == 1:
            return tipoUsuario.COMUM
        elif tipo_codigo == 2:
            return tipoUsuario.PROMOTOR
        else:
            raise ValueError(f"Código de tipo de usuário inválido: {tipo_codigo}")

    def _getNome(self):
        return self.nome

    def _getSenha(self):
        return self.senha
    
    def _setNome(self, nome):
        self.nome = nome   

# Depois substituir por um método de cryptografar 
    def setSenha(self, senha):
        self.senha = senha   
