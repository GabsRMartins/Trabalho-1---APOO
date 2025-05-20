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

class TabelaEventosTela(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.eventos_originais = []
        self.eventos_filtrados = list(self.eventos_originais)
        self.api_client = ApiClient()
        self.form_bg = "#F9F9F9"
        self.controller = controller
        self.eventos_escolhidos = set()  # Armazena índices dos eventos escolhidos

        try:
            self.original_image = Image.open("../assets/background_events.png")
        except FileNotFoundError:
            self.original_image = Image.new("RGB", (1, 1), "white")

        self.bg_photo = ImageTk.PhotoImage(self.original_image)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.atualizar_imagem)

        self.frame = tk.Frame(self, bg=self.form_bg, padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.header_frame = tk.Frame(self.frame, bg=self.form_bg)
        self.header_frame.pack(fill="x", pady=(0,10))

        self.bem_vindo_label = tk.Label(
            self.header_frame,
            text=f"Bem vindo(a), Usuário!",
            font=('Arial', 12, 'bold'),
            bg="#F9F9F9",
            anchor="w"
        )
        self.bem_vindo_label.pack(side="left", padx=15, pady=10)

        self.logout_button = tk.Button(
            self.header_frame,
            text="Logout",
            font=('Arial', 10, 'bold'),
            bg="#E53935",
            fg="white",
            command= lambda : controller.show_frame(HomePage(self.parent, controller)) if controller else self.parent.destroy()
        )
        self.logout_button.pack(side="right", padx=15, pady=10)

        # Botão para ver eventos escolhidos
        self.ver_eventos_button = tk.Button(
            self.header_frame,
            text="Ver Meus Eventos",
            font=('Arial', 10, 'bold'),
            bg="#43A047",
            fg="white",
            command=self.mostrar_eventos_escolhidos
        )
        self.ver_eventos_button.pack(side="right", padx=15, pady=10)

        self._criar_interface_filtro()
        self._criar_tabela()
        self._atualizar_tabela()

    def _criar_interface_filtro(self):
        filtro_frame = tk.LabelFrame(self.frame, text="Filtrar Eventos", font=('Arial', 12), bg=self.form_bg, fg="#333333")
        filtro_frame.pack(pady=(0, 10), padx=10, fill="x")

        tk.Label(filtro_frame, text="Nome:", font=('Arial', 10), bg=self.form_bg).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.nome_filtro = tk.StringVar()
        tk.Entry(filtro_frame, textvariable=self.nome_filtro, font=('Arial', 10), width=20).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(filtro_frame, text="Local:", font=('Arial', 10), bg=self.form_bg).grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.local_filtro = tk.StringVar()
        tk.Entry(filtro_frame, textvariable=self.local_filtro, font=('Arial', 10), width=20).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(filtro_frame, text="Preço Máximo:", font=('Arial', 10), bg=self.form_bg).grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.preco_filtro = tk.StringVar()
        tk.Entry(filtro_frame, textvariable=self.preco_filtro, font=('Arial', 10), width=10).grid(row=0, column=5, padx=5, pady=5)

        tk.Button(filtro_frame, text="Filtrar", font=('Arial', 10, 'bold'), bg="#2196F3", fg="white",
                  command=self._aplicar_filtro).grid(row=0, column=6, padx=10, pady=5)

        tk.Button(filtro_frame, text="Limpar Filtro", font=('Arial', 10), command=self._limpar_filtro).grid(row=1, column=0, columnspan=7, pady=5)

    def _criar_tabela(self):
        self.titulo_tabela = tk.Label(self.frame, text="Lista de Eventos", font=('Arial', 20, 'bold'),
                                     bg=self.form_bg, fg="#333333")
        self.titulo_tabela.pack(pady=(0, 10))

        colunas = ("Selecionar", "Nome", "Horário", "Local", "Preço")
        self.tree = ttk.Treeview(self.frame, columns=colunas, show="headings")

        self.tree.heading("Selecionar", text="Selecionar")
        self.tree.column("Selecionar", width=90, anchor="center")
        for coluna in colunas[1:]:
            self.tree.heading(coluna, text=coluna)
            self.tree.column(coluna, width=150)

        self.tree.pack(expand=True, fill="both")

        # Adiciona evento de clique duplo para selecionar/deselecionar
        self.tree.bind("<Double-1>", self._on_treeview_double_click)

    def _atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for idx, evento in enumerate(self.eventos_filtrados):
            selecionado = "✔" if idx in self.eventos_escolhidos else ""
            self.tree.insert("", tk.END, iid=idx, values=(selecionado, evento.nome, evento.horario, evento.local, f"R$ {evento.preco:.2f}"))

    def _on_treeview_double_click(self, event):
        item_id = self.tree.identify_row(event.y)
        if not item_id:
            return
        idx = int(item_id)
        if idx in self.eventos_escolhidos:
            self.eventos_escolhidos.remove(idx)
        else:
            self.eventos_escolhidos.add(idx)
        self._atualizar_tabela()

    def mostrar_eventos_escolhidos(self):
        if not self.eventos_escolhidos:
            messagebox.showinfo("Meus Eventos", "Nenhum evento selecionado.")
            return
        eventos = [self.eventos_filtrados[idx] for idx in self.eventos_escolhidos if idx < len(self.eventos_filtrados)]
        texto = "\n".join([f"{e.nome} - {e.horario} - {e.local} - R$ {e.preco:.2f}" for e in eventos])
        messagebox.showinfo("Meus Eventos", texto)

    def _aplicar_filtro(self):
        nome_digitado = self.nome_filtro.get().lower()
        local_digitado = self.local_filtro.get().lower()
        preco_max_str = self.preco_filtro.get()
        preco_max = float('inf')
        if preco_max_str:
            try:
                preco_max = float(preco_max_str)
            except ValueError:
                tk.messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o preço máximo.")
                return

        self.eventos_filtrados = []
        for evento in self.eventos_originais:
            nome_match = nome_digitado in evento.nome.lower()
            local_match = local_digitado in evento.local.lower()
            preco_match = evento.preco <= preco_max

            if nome_match and local_match and preco_match:
                self.eventos_filtrados.append(evento)

        self._atualizar_tabela()

    def _limpar_filtro(self):
        self.nome_filtro.set("")
        self.local_filtro.set("")
        self.preco_filtro.set("")
        self.eventos_filtrados = list(self.eventos_originais)
        self._atualizar_tabela()

    def atualizar_imagem(self, event):
        largura = self.winfo_width()
        altura = self.winfo_height()
        imagem_resized = self.original_image.resize((largura, altura), Image.LANCZOS).convert("RGBA")

        alpha = 0.3
        white_bg = Image.new("RGBA", imagem_resized.size, (255, 255, 255, int(255 * (1 - alpha))))
        imagem_opaca = Image.blend(white_bg, imagem_resized, alpha)

        self.bg_photo = ImageTk.PhotoImage(imagem_opaca)
        self.bg_label.config(image=self.bg_photo)

    # Essa função é apenas para simular a inserção de eventos. Usuários ativos não criam novos eventos.
    def inserir_evento(self, evento):
        self.eventos_originais.append(evento)
        self.eventos_filtrados.append(evento)
        self._atualizar_tabela()

    # def logout(self):
    #     # Definir o comportamento do logout (ir para a tela de login e cadastro)
    #     self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tabela de Eventos com Filtro")
    eventos_exemplo = [
        Evento("Show de Rock Indie", "20:00", "Mineirão", 85.00),
        Evento("Palestra sobre IA Avançada", "14:30", "UFMG - Auditório Principal", 0.00),
        Evento("Feira de Artesanato Local", "09:00", "Praça da Liberdade", 15.00),
        Evento("Cinema ao Ar Livre com Pipoca", "19:00", "Parque das Mangabeiras", 30.00),
        Evento("Noite de Jazz", "21:00", "Café Central", 40.00),
        Evento("Workshop de Robótica", "10:00", "SENAI", 50.00)
    ]

    controller = None

    app = TabelaEventosTela(root, controller)

    for evento in eventos_exemplo:

        app.inserir_evento(evento)

    app.pack(fill="both", expand=True)
    root.mainloop()