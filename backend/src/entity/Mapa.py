class Mapa:

    # Array de entidades, que podem ser Locais ou Eventos ou Usuários
    def __init__(self):
        self.entidades = []

    # Adiciona uma entidade ao array de entidades
    def _adicionarEntidade(self,entidade):
        self.entidades.append(entidade)

    # Remove entidade do array de entidades
    def _removerEntidade(self, entidade):
        self.entidades.remove(entidade)

    def _retornarMapa(self):
        return self.entidades
