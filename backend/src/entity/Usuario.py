class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def _getNome(self):
        return self.nome

    def _getSenha(self):
        return self.senha
    
    def _setNome(self, nome):
        self.nome = nome   

# Depois substituir por um método de cryptografar 
    def setSenha(self, senha):
        self.senha = senha   
