from entity.Local import Local
from base_de_dados.base_dados import Base_Dados

class LocalService(Local):

    def __init__(self):
        pass

    def buscarLocal(self, base: Base_Dados) -> Local:
        try:
            nome_local = base.get_nome_local()
            if nome_local:
                return Local(nome_local)
            else:
                return None  # Nenhum local encontrado
        except Exception as e:
            print(f"Erro ao buscar local: {e}")
            return None
        
    def getNome(self) -> str:
        return super()._getNome()
    
    def getRua(self) -> str:
        return super()._getRua()
    
    def getBairro(self) -> str:
        return super()._getBairro()
    
    def getCep(self) -> str:
        return super()._getCep()
    
    def getHorarioFuncionamento(self) -> str:
        return super()._getHorarioFuncionamento()
    
    def getMaxPessoas(self) -> int:
        return super()._getMaxPessoas()
    
    def setNome(self, nome: str) -> None:
        super()._setNome(nome)

    def setRua(self, rua: str) -> None:
        super()._setRua(rua)
    
    def setBairro(self, bairro: str) -> None:
        super()._setBairro(bairro)
    
    def setCep(self, cep: str) -> None:
        super()._setCep(cep)
    
    def setHorarioFuncionamento(self, horarioFuncionamento: str) -> None:
        super()._setHorarioFuncionamento(horarioFuncionamento)
    
    def setMaxPessoas(self, maxPessoas: int) -> None:
        super()._setMaxPessoas(maxPessoas)
