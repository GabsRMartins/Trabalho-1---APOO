import tkinter as tk
from tkinter import ttk, messagebox
from TelaInicial import HomePage
from PIL import Image, ImageTk
from ApiClient import ApiClient

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

        self.form_bg = "#F9F9F9"
        self.original_image = Image.new("RGB", (1, 1), "white")
        self.bg_photo = ImageTk.PhotoImage(self.original_image)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.atualizar_imagem)

        self.frame = tk.Frame(self, bg=self.form_bg, padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título da página
        self.titulo_label = tk.Label(
            self.frame,
            text="Cadastrar Novo Evento",
            font=('Arial', 20, 'bold'),
            bg=self.form_bg,
            fg="#333333"
        )
        self.titulo_label.pack(pady=(0, 20))

        # Campos do formulário
        self.label_nome = tk.Label(self.frame, text="Nome do Evento:", bg=self.form_bg, font=('Arial', 12))
        self.label_nome.pack(fill="x", pady=(5, 5))
        self.entry_nome = tk.Entry(self.frame, font=('Arial', 12))
        self.entry_nome.pack(fill="x", pady=(5, 10))

        self.label_horario = tk.Label(self.frame, text="Horário:", bg=self.form_bg, font=('Arial', 12))
        self.label_horario.pack(fill="x", pady=(5, 5))
        self.entry_horario = tk.Entry(self.frame, font=('Arial', 12))
        self.entry_horario.pack(fill="x", pady=(5, 10))

        self.label_local = tk.Label(self.frame, text="Local:", bg=self.form_bg, font=('Arial', 12))
        self.label_local.pack(fill="x", pady=(5, 5))
        self.entry_local = tk.Entry(self.frame, font=('Arial', 12))
        self.entry_local.pack(fill="x", pady=(5, 10))

        self.label_preco = tk.Label(self.frame, text="Preço (R$):", bg=self.form_bg, font=('Arial', 12))
        self.label_preco.pack(fill="x", pady=(5, 5))
        self.entry_preco = tk.Entry(self.frame, font=('Arial', 12))
        self.entry_preco.pack(fill="x", pady=(5, 10))

        # Botão de salvar
        self.button_salvar = tk.Button(
            self.frame,
            text="Salvar Evento",
            bg="#4CAF50",
            fg="white",
            font=('Arial', 12, 'bold'),
            command=self.salvar_evento
        )
        self.button_salvar.pack(pady=(20, 10))

        # Botão de voltar
        self.button_voltar = tk.Button(
            self.frame,
            text="Voltar",
            bg="#E53935",
            fg="white",
            font=('Arial', 12),
            command=lambda: controller.show_frame(EventPage)
        )
        self.button_voltar.pack()

    def atualizar_imagem(self, event):
        largura = self.winfo_width()
        altura = self.winfo_height()
        imagem_resized = self.original_image.resize((largura, altura), Image.LANCZOS).convert("RGBA")

        alpha = 0.3
        white_bg = Image.new("RGBA", imagem_resized.size, (255, 255, 255, int(255 * (1 - alpha))))
        imagem_opaca = Image.blend(white_bg, imagem_resized, alpha)

        self.bg_photo = ImageTk.PhotoImage(imagem_opaca)
        self.bg_label.config(image=self.bg_photo)

    def salvar_evento(self):
        nome = self.entry_nome.get().strip()
        horario = self.entry_horario.get().strip()
        local = self.entry_local.get().strip()
        preco = self.entry_preco.get().strip()

        if not nome or not horario or not local or not preco:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        try:
            preco = float(preco)
        except ValueError:
            messagebox.showerror("Erro", "O preço deve ser um número válido!")
            return

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tabela de Eventos com Filtro")
    controller = None
    app = EventRegister(root, controller)
    app.pack(fill="both", expand=True)
    root.mainloop()
