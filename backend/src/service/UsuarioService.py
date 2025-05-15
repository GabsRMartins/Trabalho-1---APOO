from entity.Usuario import Usuario


class UsuarioService(Usuario):

    def __init__(self):
        pass
    
    def buscarUsuario(self, usuario: Usuario):
        
        #usuario == busca
        
        #try catch

        #busca no banco de dados o 'usuario'
        # def get_nome_usuario(self) -> str:
        #     self.__cursor.execute("SELECT nome FROM usuario ")
        #     return self.__cursor.fetchone()
        pass

        # se não der erro, return usuario

    def mudarNomeUsuario(self, nome):
        super().setNome(nome)

