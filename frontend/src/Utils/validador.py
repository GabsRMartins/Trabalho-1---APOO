import re
import customtkinter as ctk

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
    
    def validar_cadastro_evento(self, nome,local, horario,organizadora, preco):
        erros = []
        if not self.validar_nome(nome):
            erros.append("Nome deve ter pelo menos 2 caracteres.")
        if not self.validar_nome(local):
            erros.append("Local deve ter pelo menos 2 caracteres.")
        if not self.horario_valido_forms(horario):
            erros.append("Horário informado inválido.")
        if not self.validar_nome(organizadora):
            erros.append("O nome da organizadora deve ter pelo menos 2 caracteres.")
        if not self.validar_decimal(preco):
            erros.append("É necessário preencher o Preço")    
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
    
    def validar_numeros(self, valor: str) -> bool:
        return valor.isdigit() or valor == ""

    def validar_decimal(self, valor: str) -> bool:
        try:
            if valor == "":
                return True
            float(valor.replace(",", "."))
            return True
        except ValueError:
            return False
        

    

    def horario_valido_forms(self,horario: str) -> bool:
        if not horario or len(horario) != 5 or ':' not in horario:
            return False
        partes = horario.split(":")
        if len(partes) != 2:
            return False
        try:
            horas = int(partes[0])
            minutos = int(partes[1])
            return 0 <= horas <= 23 and 0 <= minutos <= 59
        except ValueError:
            return False    



    def horario_valido(var: ctk.StringVar):
        valor = var.get()
        apenas_digitos = ''.join(filter(str.isdigit, valor))[:4]  # apenas 4 dígitos

        if len(apenas_digitos) == 0:
            resultado = ""
        elif len(apenas_digitos) == 1:
            resultado = "2" if apenas_digitos[0] > '2' else apenas_digitos
        elif len(apenas_digitos) == 2:
            horas = int(apenas_digitos)
            resultado = "23" if horas > 23 else f"{horas:02d}"
        elif len(apenas_digitos) == 3:
            horas = int(apenas_digitos[:2])
            minutos_1 = int(apenas_digitos[2])
            horas = min(horas, 23)
            minutos_1 = min(minutos_1, 5)
            resultado = f"{horas:02d}:{minutos_1}0"
        else:
            horas = int(apenas_digitos[:2])
            minutos = int(apenas_digitos[2:])
            horas = min(horas, 23)
            minutos = min(minutos, 59)
            resultado = f"{horas:02d}:{minutos:02d}"

        var.set(resultado)

    
    def preco_valido(var: ctk.StringVar):
        valor = var.get().replace(",", ".")
        permitido = ''.join(c for c in valor if c.isdigit() or c == '.')

        if '.' in permitido:
            inteiro, decimal = permitido.split('.', 1)
            decimal = decimal[:2]
            resultado = f"{inteiro}.{decimal}"
        else:
            resultado = permitido

        var.set(resultado)
   