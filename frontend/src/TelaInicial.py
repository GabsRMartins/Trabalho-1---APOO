import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from ApiClient import ApiClient
from tkinter import ttk
import customtkinter as ctk
from Utils.validador import Validador
from Components.alerta import Alerta



class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.nome_shown = False
        self.api_client = controller.api_client
        self.validador = Validador()

        self.form_bg = "#F9F9F9"
        self.original_image = Image.open("../assets/communityIcon_5x80ha0cfj7d1.png")

        # Configuração inicial da imagem de fundo
        self.bg_photo = ImageTk.PhotoImage(self.original_image)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.lower()  # Garante que o frame fique acima

        self.bind("<Configure>", self.atualizar_imagem)

        """ # Frame central com tamanho fixo
        self.frame = ctk.CTkFrame(
            self,
            fg_color=self.form_bg,
            corner_radius=15,
            width=800,  # Ajuste conforme necessário
            height=300
        )
        self.frame.place(relx=0.5, rely=0.5, anchor="center") """

        self.frame = ctk.CTkFrame(self, corner_radius=15)
        self.frame.pack(expand=True, pady=40, padx=20)


        self.build_form()

    def atualizar_imagem(self, event):
        """Redimensiona a imagem de fundo dinamicamente."""
        resized_image = self.original_image.resize((event.width, event.height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_image)
        self.bg_label.config(image=self.bg_photo)

    def build_form(self):
        self.label_bem_vindo = ctk.CTkLabel(
            self.frame,
            text="Bem Vindo de Volta! Acessar Conta" if self.nome_shown else "Bem vindo! Criar Conta",
            font=('Arial', 20, 'bold'),
            text_color="#333333"
        )
        self.label_bem_vindo.grid(row=0, column=0, columnspan=2, padx=60, pady=(20, 10))


        # Labels e campos do formulário
        self.label_nome = ctk.CTkLabel(self.frame, text="Nome:", font=('Arial', 12))
        self.entry_nome = ctk.CTkEntry(self.frame, font=('Arial', 12), width=250)

        self.label_email = ctk.CTkLabel(self.frame, text="Email:", font=('Arial', 12))
        self.entry_email = ctk.CTkEntry(self.frame, font=('Arial', 12), width=250)

        self.label_tipo = ctk.CTkLabel(self.frame, text="Tipo de Usuário:", font=('Arial', 12))

        self.tipo_var = tk.StringVar(value="Ativo")
        self.combo_tipo = ctk.CTkComboBox(
            self.frame,
            variable=self.tipo_var,
            values=["Ativo", "Promotor"],
            font=('Arial', 12),
            width=250
        )
        self.combo_tipo.set("Ativo")  # valor inicial

        self.label_usuario = ctk.CTkLabel(self.frame, text="Usuário:",anchor="w")
        self.entry_usuario = ctk.CTkEntry(self.frame, font=('Arial', 12), width=250)

        self.label_senha = ctk.CTkLabel(self.frame, text="Senha:", anchor="w")
        self.entry_senha = ctk.CTkEntry(self.frame, font=('Arial', 12), width=250, show="*")

        self.frame.grid_columnconfigure(0, weight=1)

        self.label_usuario.grid(row=3, column=0, pady=(5, 0), sticky="w")
        self.entry_usuario.grid(row=4, column=0, pady=(0, 5))
        self.label_senha.grid(row=5, column=0, pady=(10, 0), sticky="w")
        self.entry_senha.grid(row=6, column=0, pady=(0, 10))


        self.btn_login = ctk.CTkButton(
            master=self.frame,
            text="Login",
            font=('Arial', 12, 'bold'),
            fg_color="#4CAF50",
            hover_color="#45A049",
            text_color="white",
            width=200,
            height=40,
            corner_radius=10,
            command=self.fazer_login
        )
        self.btn_login.grid(row=7, column=0, columnspan=2, pady=(15, 5))

        self.btn_cadastro = ctk.CTkButton(
            master=self.frame,
            text="Cadastrar",
            font=('Arial', 12, 'bold'),
            fg_color="#2196F3",
            hover_color="#1976D2",
            text_color="white",
            width=200,
            height=40,
            corner_radius=10,
            command=self.fazer_cadastro
        )

        

        self.btn_redirecionamento_cadastro = ctk.CTkButton(
            master=self.frame,
            text="Primeiro Acesso? Cadastrar",
            cursor="hand2",
            border_width=0,
            fg_color="light grey",
            hover_color="light grey",
            text_color="blue",
            command=self.mostrar_formulario_cadastro
        )

        self.btn_redirecionamento_login = ctk.CTkButton(
            master=self.frame,
            text="Ja possui conta? Login",
            cursor="hand2",
            border_width=0,
            fg_color="light grey",
            hover_color="light grey",
            text_color="blue",
            command=self.mostrar_formulario_login
        )

        self.btn_redirecionamento_cadastro.grid(row=8, column=0, columnspan=2)
        
        self.nome_shown = False

    def mostrar_formulario_login(self):
        self.label_nome.grid_forget()
        self.entry_nome.grid_forget()
        self.label_email.grid_forget()
        self.entry_email.grid_forget()
        self.label_tipo.grid_forget()
        self.combo_tipo.grid_forget()

      
        self.frame.grid_columnconfigure(0, weight=1)

        self.label_usuario.grid(row=3, column=0)
        self.entry_usuario.grid(row=4, column=0, pady=(0, 5))
        self.label_senha.grid(row=5, column=0)
        self.entry_senha.grid(row=6, column=0, pady=(0, 10))



        self.btn_cadastro.grid_forget()
        self.btn_redirecionamento_login.grid_forget()

        self.btn_login.grid(row=7, column=0, columnspan=2, pady=(15, 5))
        self.btn_redirecionamento_cadastro.grid(row=8, column=0, columnspan=2)
    
        self.nome_shown = False
        novo_texto = "Bem Vindo de Volta! Acessar Conta"
        self.label_bem_vindo.configure(text=novo_texto)



    def mostrar_formulario_cadastro(self):
        self.label_nome.grid(row=1, column=0)
        self.entry_nome.grid(row=1, column=1, pady=5)

        self.label_email.grid(row=2, column=0)
        self.entry_email.grid(row=2, column=1, pady=(0, 10))

        self.label_tipo.grid(row=3, column=0, sticky="w")
        self.combo_tipo.grid(row=3, column=1, pady=5)

        self.label_senha.grid(row=4, column=0, sticky="s")
        self.entry_senha.grid(row=4, column=1, pady=(10,0))

        self.label_usuario.grid_forget()
        self.entry_usuario.grid_forget()

        self.btn_login.grid_forget()
        self.btn_redirecionamento_cadastro.grid_forget()

        self.btn_cadastro.grid(row=7, column=0, columnspan=2, pady=(15, 5))
        self.btn_redirecionamento_login.grid(row=8, column=0, columnspan=2)

        self.nome_shown = True
        novo_texto = "Bem vindo! Criar Conta" 
        self.label_bem_vindo.configure(text=novo_texto)


    def fazer_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        form_erros = self.validador.validar_login(usuario,senha)
        if form_erros:
            msg_erro = "\n".join(form_erros)
            Alerta(self.frame, msg_erro, tipo="erro") 
        else:
         resultado = self.api_client.login(usuario, senha)
        if "error" in resultado:
                msg_erro = f"{resultado['error']}\n{resultado.get('details', '')}"
                Alerta(self.frame,msg_erro,tipo="erro")
        else:
            token = resultado.get("access_token")
            if token:
                Alerta(self.frame, "Login realizado com sucesso!", tipo="sucesso")
                self.api_client.token = token
                dadosUsuario = self.api_client.getDadosLogado()
                if( dadosUsuario.tipo == 1):
                 self.controller.show_frame("EventPage")
                else:
                 self.controller.show_frame("TelaCadastro")   
            else:
                msg_erro =  "Token de acesso não encontrado na resposta."
                Alerta(self.frame, msg_erro, tipo="erro") 



    def fazer_cadastro(self):
            nome = self.entry_nome.get()
            email = self.entry_email.get()
            senha = self.entry_senha.get()
            tipo = self.tipo_var.get()
            usuario = 1 if tipo == "Ativo" else 2
            form_erros = self.validador.validar_cadastro(nome, email, senha, tipo)
            if form_erros:
                msg_erro = "\n".join(form_erros)
                Alerta(self.frame, msg_erro, tipo="erro") 
            else:
             resultado = self.api_client.cadastrar_usuario(nome, email, senha, usuario)
             if "error" in resultado:
                msg_erro = f"{resultado['error']}\n{resultado.get('details', '')}"
                Alerta(self.frame,msg_erro,tipo="erro")
             else:
                Alerta(self.frame, "Cadastro realizado com sucesso!", tipo="sucesso")
                self.mostrar_formulario_login()


    def atualizar_imagem(self, event):
        largura = self.winfo_width()
        altura = self.winfo_height()
        imagem_resized = self.original_image.resize((largura, altura), Image.LANCZOS).convert("RGBA")

        alpha = 0.3
        white_bg = Image.new("RGBA", imagem_resized.size, (255, 255, 255, int(255 * (1 - alpha))))
        imagem_opaca = Image.blend(white_bg, imagem_resized, alpha)

        self.bg_photo = ImageTk.PhotoImage(imagem_opaca)
        self.bg_label.config(image=self.bg_photo)
        
