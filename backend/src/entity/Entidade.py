from abc import ABC,abstractmethod

class Entidade(ABC):

    def __init__(self):
        pass
    
    @abstractmethod
    def _getNome(self):
        pass

