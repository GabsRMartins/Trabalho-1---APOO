import re

class Validador:
    def __init__(self):
        pass
        

    def validar_cadastro(self, nome, email, senha, tipo):
        erros = []
        if not self.validar_nome(nome):
            erros.append("Nome deve ter pelo menos 2 caracteres.")
        if not self.validar_email(email):
            erros.append("Email inválido.")
        if not self.validar_senha(senha):
            erros.append("Senha deve ter pelo menos 6 caracteres.")
        if not self.validar_tipo(tipo):
            erros.append("Tipo inválido.")
        return erros if erros else None


    def validar_nome(self,nome):
        return len(nome) >= 2  # mínimo 2 caracteres

    def validar_email(self,email):
        # Regex simples para validar email
        padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(padrao_email, email) is not None

    def validar_senha(self,senha):
        return len(senha) >= 6  # mínimo 6 caracteres

    def validar_tipo(self,tipo):
        return tipo in ("Ativo", "Promotor")  # ou seus valores válidos
    
    def validar_login(self,nome,senha):
        erros = []
        if not self.validar_nome(nome):
            erros.append("Nome deve ter pelo menos 2 caracteres.")
        if not self.validar_senha(senha):
            erros.append("Senha deve ter pelo menos 6 caracteres.")
        return erros if erros else None    

   