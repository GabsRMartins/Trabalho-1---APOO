import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Variável global para controlar a visibilidade dos campos Nome e Telefone
nome_shown = False

def fazer_login():
    global nome_shown
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Se os campos Nome e Telefone estiverem visíveis, escondê-los
    if nome_shown:
        label_nome.grid_forget()
        entry_nome.grid_forget()
        label_telefone.grid_forget()
        entry_telefone.grid_forget()
        
        nome_shown = False  # Marca que os campos não estão visíveis

    messagebox.showinfo("Login", f"Usuário: {usuario}\nSenha: {senha}")

def fazer_cadastro():
    global nome_shown

    if not nome_shown:
        # Mostrar campos adicionais acima
        label_nome.grid(row=1, column=0, sticky="w", pady=(10, 0))
        entry_nome.grid(row=1, column=1, pady=5)

        label_telefone.grid(row=2, column=0, sticky="w")
        entry_telefone.grid(row=2, column=1, pady=(0, 10))

        nome_shown = True
        btn_cadastro.config(text="Finalizar Cadastro")
    else:
        nome = entry_nome.get()
        telefone = entry_telefone.get()
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        messagebox.showinfo("Cadastro Realizado", f"Nome: {nome}\nTelefone: {telefone}\nUsuário: {usuario}\nSenha: {senha}")

# Atualiza o fundo quando a janela for redimensionada
def atualizar_imagem(event):
    largura = root.winfo_width()
    altura = root.winfo_height()
    imagem_resized = original_image.resize((largura, altura), Image.LANCZOS).convert("RGBA")

    alpha = 0.3
    white_bg = Image.new("RGBA", imagem_resized.size, (255, 255, 255, int(255 * (1 - alpha))))
    imagem_opaca = Image.blend(white_bg, imagem_resized, alpha)

    global bg_photo
    bg_photo = ImageTk.PhotoImage(imagem_opaca)
    bg_label.config(image=bg_photo)

# Janela principal
root = tk.Tk()
root.title("Tela de Login / Cadastro")
root.state("zoomed")
root.attributes("-alpha", 0.97)

# Imagem de fundo
original_image = Image.open("../assets/communityIcon_5x80ha0cfj7d1.png")
bg_photo = ImageTk.PhotoImage(original_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

root.bind("<Configure>", atualizar_imagem)

# Frame do formulário
form_bg = "#F9F9F9"
frame = tk.Frame(root, bg=form_bg, padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

label_titulo = tk.Label(frame, text="Bem-vindo!", font=('Arial', 20, 'bold'), bg=form_bg, fg="#333333")
label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Campos adicionais (Nome e Telefone) ocultos inicialmente
label_nome = tk.Label(frame, text="Nome:", font=('Arial', 12), bg=form_bg)
entry_nome = tk.Entry(frame, font=('Arial', 12), width=30, bd=1, relief="solid")

label_telefone = tk.Label(frame, text="Telefone:", font=('Arial', 12), bg=form_bg)
entry_telefone = tk.Entry(frame, font=('Arial', 12), width=30, bd=1, relief="solid")

# Campos existentes (Usuário e Senha)
label_usuario = tk.Label(frame, text="Usuário:", font=('Arial', 12), bg=form_bg)
entry_usuario = tk.Entry(frame, font=('Arial', 12), width=30, bd=1, relief="solid")

label_usuario.grid(row=3, column=0, sticky="w")
entry_usuario.grid(row=3, column=1, pady=5)

label_senha = tk.Label(frame, text="Senha:", font=('Arial', 12), bg=form_bg)
label_senha.grid(row=4, column=0, sticky="w")
entry_senha = tk.Entry(frame, show="*", font=('Arial', 12), width=30, bd=1, relief="solid")
entry_senha.grid(row=4, column=1, pady=5)

# Botões
btn_login = tk.Button(
    frame, text="Login", font=('Arial', 12, 'bold'),
    bg="#4CAF50", fg="white", activebackground="#45A049",
    width=20, command=fazer_login
)

btn_cadastro = tk.Button(
    frame, text="Cadastrar", font=('Arial', 12, 'bold'),
    bg="#2196F3", fg="white", activebackground="#1976D2",
    width=20, command=fazer_cadastro
)

# Botões empacotados ao final
btn_login.grid(row=5, column=0, columnspan=2, pady=(15, 5))
btn_cadastro.grid(row=6, column=0, columnspan=2)

root.mainloop()
