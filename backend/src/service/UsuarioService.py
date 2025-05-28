from entity.Usuario import Usuario
from base_de_dados.base_dados import Base_Dados

class UsuarioService(Usuario):

    def __init__(self):
        pass
    
    def buscarUsuario(self, nome,base: Base_Dados) -> Usuario:
        try:
            nome_usuario = base.get_usuario(nome)
            if nome_usuario:
                return Usuario(nome_usuario)
            else:
                return None  # Nenhum usuário encontrado
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
        
    def buscarUsuarioId(self, id,base: Base_Dados) -> Usuario:
        try:
            id_usuario = base.get_usuario_id(id)
            if id_usuario:
                tupla = id_usuario[0]
                return Usuario(tupla[1], tupla[2], tupla[3], tupla[4])
            else:
                return None  # Nenhum usuário encontrado
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None    

    def getNome(self) -> str:
        return super()._getNome()
    
    def getSenha(self) -> str:
        return super()._getSenha()
    
    def mudarSenhaUsuario(self, senha):
        super().setSenha(senha)

    def mudarNomeUsuario(self, nome):
        super().setNome(nome)

