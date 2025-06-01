from entity.Usuario import Usuario
from base_de_dados.base_dados import Base_Dados

class UsuarioService(Usuario):

    def __init__(self, usuario: Usuario):
        self.usuario = usuario
    
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
        return self.usuario._getNome()
    
    def getSenha(self) -> str:
        return self.usuario._getSenha()
    
    def getEmail(self) -> str:
        return self.usuario._getEmail()

    def getTipo(self):
        return self.usuario._getTipo()

    def mudarSenhaUsuario(self, senha):
        self.usuario.setSenha(senha)

    def mudarNomeUsuario(self, nome):
        self.usuario.setNome(nome)

