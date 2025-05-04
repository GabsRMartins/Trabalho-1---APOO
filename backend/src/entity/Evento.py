import Entidade

class Evento(Entidade):
    def __init__(self,horario,local,preco,fotos):
        self.horario = horario
        self.local = local
        self.preco = preco
        self.fotos = fotos