from Entidade import Entidade

class Mapa:

    # Array de entidades, que podem ser Locais ou Eventos ou Usuários
    def __init__(self):
        self.__entidades = []

    def _getEntidades(self):
        return self.__entidades

    # Adiciona uma entidade ao array de entidades
    def _adicionarEntidade(self, entidade: Entidade):
        self.__entidades.append(entidade)

    # Remove entidade do array de entidades
    def _removerEntidade(self, entidade: Entidade):
        self.__entidades.remove(entidade)

    def _retornarMapa(self):
        return self.__entidades
