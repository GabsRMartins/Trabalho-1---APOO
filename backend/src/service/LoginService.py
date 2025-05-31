from ....base_de_dados.base_dados import Base_Dados

class LoginService:
    def __init__(self, db: Base_Dados):
        self.db = db

    def autenticar(self, username: str, password: str) -> bool:
        usuarios = self.db.get_usuario(username)
        if not usuarios:
            print("Usuário não encontrado.")
            return False

        usuario = usuarios[0]  # pega o primeiro usuário com aquele nome
        senha_correta = usuario[3]  # índice 3 = senha (ajuste conforme sua tabela)

        if senha_correta == password:
            print("Usuário válido")
            return True
        else:
            print("Senha incorreta.")
            return False


    def cadastrar(self, username: str, email: str, password: str, tipo: int) -> bool:
        try:
            self.db.cadastrar(username ,email, password,  tipo)
            print("Usuário cadastrado com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao cadastrar usuário: {e}")
            return False