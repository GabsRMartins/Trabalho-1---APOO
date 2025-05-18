from entity import Local
from base_de_dados.base_dados import Base_Dados

class LocalService(Local):

    def __init__(self):
        pass

    def buscarLocal(self, base: Base_Dados):
        try:
            nome_local = base.get_nome_local()
            if nome_local:
                return Local(nome_local)
            else:
                return None  # Nenhum usuário encontrado
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
        
    def getNome(self):
        return super()._getNome()
    
    def getRua(self):
        return super()._getRua()
    
    def getBairro(self):
        return super()._getBairro()
    
    def getCep(self):
        return super()._getCep()
    
    def getHorarioFuncionamento(self):
        return super()._getHorarioFuncionamento()
    
    def getMaxPessoas(self):
        return super()._getMaxPessoas()
    
    def setNome(self, nome):
        super()._setNome(nome)
    
