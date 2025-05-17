class Mapa:

    # Array de entidades, que podem ser Locais ou Eventos ou Usuários
    def __init__(self):
        self.entidades = []

    # Adiciona uma entidade ao array de entidades
    def _adicionar_entidade(self,entidade):
        self.entidades.append(entidade)

    # Remove entidade do array de entidades
    def _remover_entidade(self, entidade):
        self.entidades.remove(entidade)

    def _retornar_mapa(self):
        return self.entidades
