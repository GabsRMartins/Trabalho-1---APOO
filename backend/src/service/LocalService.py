from ..entity.Local import Local
from ....base_de_dados.base_dados import Base_Dados

class LocalService(Local):

    def __init__(self, local: Local):
        self.local = local
        

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
        return self.local._getNome()
    
    def getRua(self) -> str:
        return self.local._getRua()
    
    def getBairro(self) -> str:
        return self.local._getBairro()
    
    def getCep(self) -> str:
        return self.local._getCep()
    
    def getHorarioFuncionamento(self) -> str:
        return self.local._getHorarioFuncionamento()
    
    def getMaxPessoas(self) -> int:
        return self.local._getMaxPessoas()
    
    def setNome(self, nome: str) -> None:
        self.local._setNome(nome)

    def setRua(self, rua: str) -> None:
        self.local._setRua(rua)
    
    def setBairro(self, bairro: str) -> None:
        self.local._setBairro(bairro)
    
    def setCep(self, cep: str) -> None:
        self.local._setCep(cep)
    
    def setHorarioFuncionamento(self, horarioFuncionamento: str) -> None:
        self.local._setHorarioFuncionamento(horarioFuncionamento)
    
    def setMaxPessoas(self, maxPessoas: int) -> None:
        self.local._setMaxPessoas(maxPessoas)
