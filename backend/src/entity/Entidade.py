from abc import ABC,abstractmethod

class Entidade(ABC):
    
    @abstractmethod
    def print(self):
        pass

