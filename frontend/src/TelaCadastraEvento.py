import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from Components.menu_lateral import MenuLateralFrame
from Components.alerta import Alerta
from Utils.validador import Validador
class Evento:
    def __init__(self, nome, horario, local, preco):
        self.nome = nome
        self.horario = horario
        self.local = local
        self.preco = preco

class EventRegister(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.api_client = controller.api_client
        self.validador = Validador()
        self.menu_lateral = None
          # Frame central
        self.frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#A7D7C5")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")


        # Abrir e redimensionar a imagem
        img = Image.open("../assets/botao_capivara.png")
        img = img.resize((60, 60), Image.Resampling.LANCZOS) 
        img_tk = ImageTk.PhotoImage(img)

        # Criar o botão com imagem
        self.menu_button = tk.Button(
            self, image=img_tk, bg="#E3F2FD", bd=0, command=self.toggle_menu_lateral
        )
        self.menu_button.image = img_tk  
        self.menu_button.place(x=10, y=10)

        # Título
        self.titulo_label = ctk.CTkLabel(
            self.frame, 
            text="Cadastrar Novo Evento", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.titulo_label.pack(pady=(20, 10))

        # Nome do Evento
        self.label_nome = ctk.CTkLabel(self.frame, text="Nome do Evento:")
        self.label_nome.pack(anchor="w", padx=20)
        self.entry_nome = ctk.CTkEntry(self.frame, width=300)
        self.entry_nome.pack(pady=(0, 10), padx=20)

        # Horário
        self.label_horario = ctk.CTkLabel(self.frame, text="Horário:")
        self.label_horario.pack(anchor="w", padx=20)
        self.entry_horario_var = ctk.StringVar()
        self.entry_horario = ctk.CTkEntry(self.frame, textvariable=self.entry_horario_var,width=300)
        self.entry_horario.pack(pady=(0, 10), padx=20)
        self.entry_horario_var.trace_add("write", lambda *args: Validador.horario_valido(self.entry_horario_var))
        

        # Local
        self.label_local = ctk.CTkLabel(self.frame, text="Local:")
        self.label_local.pack(anchor="w", padx=20)
        self.entry_local = ctk.CTkEntry(self.frame, width=300)
        self.entry_local.pack(pady=(0, 10), padx=20)

        # Preço
        self.label_preco = ctk.CTkLabel(self.frame, text="Preço (R$):")
        self.label_preco.pack(anchor="w", padx=20)
        self.entry_preco_var = ctk.StringVar()
        self.entry_preco = ctk.CTkEntry(self.frame,textvariable=self.entry_preco_var, width=300)
        self.entry_preco.pack(pady=(0, 20), padx=20)
        self.entry_preco_var.trace_add("write", lambda *args: Validador.preco_valido(self.entry_preco_var))
        

        # Botão 
        self.botao_cadastrar = ctk.CTkButton(self.frame, command=self.cadastra_evento,text="Cadastrar")
        self.botao_cadastrar.pack(pady=(0, 20))

      
   
    def cadastra_evento(self):
        nome = self.entry_nome.get().strip()
        horario = self.entry_horario.get().strip()
        local = self.entry_local.get().strip()
        preco = self.entry_preco.get().strip()
        usuarioLogado = self.api_client.getDadosLogado()
        organizadora = usuarioLogado.nome
        form_erros = self.validador.validar_cadastro_evento(nome, local, horario,organizadora,preco)
        if form_erros:
                msg_erro = "\n".join(form_erros)
                Alerta(self.frame, msg_erro, tipo="erro") 
        else:
             resultado = self.api_client.cadastrar_evento(nome, local, horario,organizadora,preco)
             if "error" in resultado:
                msg_erro = f"{resultado['error']}\n{resultado.get('details', '')}"
                Alerta(self.frame,msg_erro,tipo="erro")
             else:
                Alerta(self.frame, "Cadastro realizado com sucesso!", tipo="sucesso")


    def toggle_menu_lateral(self):
        if self.menu_lateral and self.menu_lateral.winfo_ismapped():
            self.menu_lateral.place_forget()
        else:
            if not self.menu_lateral:
                self.menu_lateral = MenuLateralFrame(self, fechar_callback=self.fechar_menu_lateral)
            self.menu_lateral.place(x=0, y=0, relheight=1)
            
    def fechar_menu_lateral(self):
        if self.menu_lateral:
            self.menu_lateral.place_forget()
