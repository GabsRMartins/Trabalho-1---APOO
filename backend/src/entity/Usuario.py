class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def getNome(self):
        return self.nome

    def getSenha(self):
        return self.senha
    
    def setNome(self, nome):
         self.nome = nome   

# Depois substituir por um método de cryptografar 
    def setSenha(self, senha):
         self.senha = senha   
