import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Evento:
    def __init__(self, nome, horario, local, preco):
        self.nome = nome
        self.horario = horario
        self.local = local
        self.preco = preco

class TabelaEventosTela(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.eventos = []
        self.form_bg = "#F9F9F9"

        try:
            self.original_image = Image.open("../assets/communityIcon_5x80ha0cfj7d1.png") # Ajuste o caminho da imagem
        except FileNotFoundError:
            self.original_image = Image.new("RGB", (1, 1), "white")

        self.bg_photo = ImageTk.PhotoImage(self.original_image)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.atualizar_imagem)

        self.frame = tk.Frame(self, bg=self.form_bg, padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self._criar_tabela()

    def _criar_tabela(self):
        tk.Label(self.frame, text="Lista de Eventos", font=('Arial', 20, 'bold'),
                 bg=self.form_bg, fg="#333333").pack(pady=(0, 20))

        colunas = ("Nome", "Horário", "Local", "Preço")
        self.tree = ttk.Treeview(self.frame, columns=colunas, show="headings")

        for coluna in colunas:
            self.tree.heading(coluna, text=coluna)
            self.tree.column(coluna, width=150) # Ajuste a largura conforme necessário

        for evento in self.eventos:
            self.tree.insert("", tk.END, values=(evento.nome, evento.horario, evento.local, f"R$ {evento.preco:.2f}"))

        self.tree.pack(expand=True, fill="both")

    def atualizar_imagem(self, event):
        largura = self.winfo_width()
        altura = self.winfo_height()
        imagem_resized = self.original_image.resize((largura, altura), Image.LANCZOS).convert("RGBA")

        alpha = 0.3
        white_bg = Image.new("RGBA", imagem_resized.size, (255, 255, 255, int(255 * (1 - alpha))))
        imagem_opaca = Image.blend(white_bg, imagem_resized, alpha)

        self.bg_photo = ImageTk.PhotoImage(imagem_opaca)
        self.bg_label.config(image=self.bg_photo)

# Para executar esta tela individualmente (opcional)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tabela de Eventos")
    eventos_exemplo = [
        Evento("Show de Rock", "20:00", "Mineirão", 80.00),
        Evento("Palestra sobre IA", "14:30", "UFMG", 0.00),
        Evento("Feira de Artesanato", "09:00", "Praça da Liberdade", 10.00),
        Evento("Cinema ao Ar Livre", "19:00", "Parque das Mangabeiras", 25.50)
    ]
    app = TabelaEventosTela(root, eventos_exemplo)
    app.pack(fill="both", expand=True)
    root.mainloop()