import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from ApiClient import ApiClient
from tkinter import ttk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.nome_shown = False
        self.api_client = ApiClient()

        self.form_bg = "#F9F9F9"
        self.original_image = Image.open("../assets/communityIcon_5x80ha0cfj7d1.png")

        self.bg_photo = ImageTk.PhotoImage(self.original_image)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.atualizar_imagem)

        self.frame = tk.Frame(self, bg=self.form_bg, padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.build_form()

    def build_form(self):
        tk.Label(self.frame, text="Bem-vindo!", font=('Arial', 20, 'bold'),
             bg=self.form_bg, fg="#333333").grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Campos que devem aparecer somente no cadastro:
        self.label_nome = tk.Label(self.frame, text="Nome:", font=('Arial', 12), bg=self.form_bg)
        self.entry_nome = tk.Entry(self.frame, font=('Arial', 12), width=30, bd=1, relief="solid")

        self.label_email = tk.Label(self.frame, text="Email:", font=('Arial', 12), bg=self.form_bg)
        self.entry_email = tk.Entry(self.frame, font=('Arial', 12), width=30, bd=1, relief="solid")

        self.label_tipo = tk.Label(self.frame, text="Tipo de Usuário:", font=('Arial', 12), bg=self.form_bg)
        self.tipo_var = tk.StringVar()
        self.combo_tipo = ttk.Combobox(self.frame, textvariable=self.tipo_var, font=('Arial', 12), width=28, state="readonly")
        self.combo_tipo['values'] = ("Ativo", "Promotor")
        self.combo_tipo.current(0)

        # Campos comuns ao login:
        self.label_usuario = tk.Label(self.frame, text="Usuário:", font=('Arial', 12), bg=self.form_bg)
        self.entry_usuario = tk.Entry(self.frame, font=('Arial', 12), width=30, bd=1, relief="solid")
        self.label_usuario.grid(row=3, column=0, sticky="w")
        self.entry_usuario.grid(row=3, column=1, pady=5)

        tk.Label(self.frame, text="Senha:", font=('Arial', 12), bg=self.form_bg).grid(row=4, column=0, sticky="w")
        self.entry_senha = tk.Entry(self.frame, show="*", font=('Arial', 12), width=30, bd=1, relief="solid")
        self.entry_senha.grid(row=4, column=1, pady=5)

        btn_login = tk.Button(
            self.frame, text="Login", font=('Arial', 12, 'bold'),
            bg="#4CAF50", fg="white", activebackground="#45A049",
            width=20, command=self.fazer_login
        )
        btn_login.grid(row=5, column=0, columnspan=2, pady=(15, 5))

        self.btn_cadastro = tk.Button(
            self.frame, text="Cadastrar", font=('Arial', 12, 'bold'),
            bg="#2196F3", fg="white", activebackground="#1976D2",
            width=20, command=self.fazer_cadastro
        )
        self.btn_cadastro.grid(row=6, column=0, columnspan=2)


        self.nome_shown = False

    def mostrar_formulario_login(self):
        self.label_nome.grid_forget()
        self.entry_nome.grid_forget()
        self.label_email.grid_forget()
        self.entry_email.grid_forget()
        self.label_tipo.grid_forget()
        self.combo_tipo.grid_forget()

        self.label_usuario.grid(row=1, column=0, sticky="w", pady=(10, 0))
        self.entry_usuario.grid(row=1, column=1, pady=5)

        self.btn_cadastro.config(text="Cadastrar")
        self.nome_shown = False


    def mostrar_formulario_cadastro(self):
        self.label_nome.grid(row=1, column=0, sticky="w", pady=(10, 0))
        self.entry_nome.grid(row=1, column=1, pady=5)

        self.label_email.grid(row=2, column=0, sticky="w")
        self.entry_email.grid(row=2, column=1, pady=(0, 10))

        self.label_tipo.grid(row=3, column=0, sticky="w")
        self.combo_tipo.grid(row=3, column=1, pady=5)

        self.label_usuario.grid_forget()
        self.entry_usuario.grid_forget()

        self.btn_cadastro.config(text="Finalizar Cadastro")
        self.nome_shown = True


    def fazer_login(self):
        if self.nome_shown:
            self.mostrar_formulario_login()

        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        resultado = self.api_client.login(usuario, senha)

        if "error" in resultado:
            messagebox.showerror("Erro", f"{resultado['error']}\n{resultado.get('details', '')}")
        else:
            token = resultado.get("token", "Token não fornecido")
            messagebox.showinfo("Sucesso", f"Login realizado com sucesso!\nToken: {token}")
            self.controller.show_frame("EventPage")  


    def fazer_cadastro(self):
        if not self.nome_shown:
            self.mostrar_formulario_cadastro()
        else:
            nome = self.entry_nome.get()
            email = self.entry_email.get()
            senha = self.entry_senha.get()

            tipo = self.tipo_var.get()
            usuario = 1 if tipo == "Ativo" else 2

            resultado = self.api_client.cadastrar_usuario(nome, email, senha, usuario)

            if "error" in resultado:
                messagebox.showerror("Erro", f"{resultado['error']}\n{resultado.get('details', '')}")
            else:
                messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
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
        
