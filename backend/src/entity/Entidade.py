from abc import ABC,abstractmethod

class Entidade(ABC):
    
    @abstractmethod
    def _getNome(self):
        pass

