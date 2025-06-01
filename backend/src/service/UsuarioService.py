from ..entity.Usuario import Usuario
from ....base_de_dados.base_dados import Base_Dados

class UsuarioService(Usuario):

    def __init__(self, usuario: Usuario):
        self.usuario = usuario
    
    def buscarUsuario(self, base: Base_Dados):
        try:
            nome_usuario = base.get_nome_usuario()
            if nome_usuario:
                return Usuario(nome_usuario)
            else:
                return None  # Nenhum usuário encontrado
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None

    def getNome(self):
        return self.usuario._getNome()
    
    def getSenha(self):
        return self.usuario._getSenha()
    
    def getTipo(self):
        return self.usuario._getTipo()

    def mudarSenhaUsuario(self, senha):
        self.usuario._setSenha(senha)

    def mudarNomeUsuario(self, nome):
        self.usuario._setNome(nome)
