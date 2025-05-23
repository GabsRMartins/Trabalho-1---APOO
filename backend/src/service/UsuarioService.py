from entity.Usuario import Usuario
from base_de_dados.base_dados import Base_Dados

class UsuarioService(Usuario):

    def __init__(self):
        pass
    
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
        return super()._getNome()
    
    def getSenha(self):
        return super()._getSenha()
    
    def mudarSenhaUsuario(self, senha):
        super().setSenha(senha)

    def mudarNomeUsuario(self, nome):
        super().setNome(nome)

