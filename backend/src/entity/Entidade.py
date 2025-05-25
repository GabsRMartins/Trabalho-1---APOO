from abc import ABC,abstractmethod

class Entidade(ABC):

    def __init__(self):
        pass
    
    @abstractmethod
    def print(self):
        pass

