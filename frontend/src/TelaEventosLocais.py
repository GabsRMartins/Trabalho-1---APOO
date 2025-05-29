import tkinter as tk
from tkinter import ttk, messagebox
from TelaInicial import HomePage
from PIL import Image, ImageTk
from ApiClient import ApiClient
from Components.logout_button import LogoutButton
import customtkinter as ctk


class Evento:
    def __init__(self, nome, horario, local, preco):
        self.nome = nome
        self.horario = horario
        self.local = local
        self.preco = preco

class EventPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.form_bg = "#F9F9F9"
        self.controller = controller
        self.api_client = controller.api_client
        self.usuarioLogado = None 
        self.carregado = False
        self.eventos_originais = self.api_client.getEventos()
        self.eventos_filtrados = list(self.eventos_originais)  
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

        LogoutButton(self.header_frame, self.api_client, self.controller)
     
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

    def on_show(self):
        self.usuarioLogado = self.api_client.getDadosLogado()
        if hasattr(self, 'bem_vindo_label'):
            self.bem_vindo_label.configure(text=f"Bem vindo(a), {self.usuarioLogado.nome}")
        else:
            self.bem_vindo_label = ctk.CTkLabel(
                self.header_frame,
                text=f"Bem vindo(a), {self.usuarioLogado.nome}",
                font=('Arial', 30, 'bold'),
                text_color="#333333",
                anchor="w"
            )
            self.bem_vindo_label.pack(side="left", padx=15, pady=10)

   

    def _criar_interface_filtro(self):
        filtro_frame = tk.LabelFrame(self.frame, text="Filtrar Eventos", font=('Arial', 12), bg=self.form_bg, fg="#333333")
        filtro_frame.pack(pady=(0, 10), padx=10, fill="x")

        tk.Label(filtro_frame, text="Nome:", font=('Arial', 10), bg=self.form_bg).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.nome_filtro = tk.StringVar()
        tk.Entry(filtro_frame, textvariable=self.nome_filtro, font=('Arial', 10), width=20).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(filtro_frame, text="Horário:", font=('Arial', 10), bg=self.form_bg).grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.horario_filtro = tk.StringVar()
        tk.Entry(filtro_frame, textvariable=self.horario_filtro, font=('Arial', 10), width=20).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(filtro_frame, text="Local:", font=('Arial', 10), bg=self.form_bg).grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.local_filtro = tk.StringVar()
        tk.Entry(filtro_frame, textvariable=self.local_filtro, font=('Arial', 10), width=20).grid(row=0, column=5, padx=5, pady=5)

        tk.Label(filtro_frame, text="Preço Máximo:", font=('Arial', 10), bg=self.form_bg).grid(row=0, column=6, padx=5, pady=5, sticky="w")
        self.preco_filtro = tk.StringVar()
        tk.Entry(filtro_frame, textvariable=self.preco_filtro, font=('Arial', 10), width=10).grid(row=0, column=7, padx=5, pady=5)

        tk.Button(filtro_frame, text="Filtrar", font=('Arial', 10, 'bold'), bg="#2196F3", fg="white",
                  command=self._aplicar_filtro).grid(row=0, column=8, padx=10, pady=5)

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
            self.tree.column(coluna, width=150, anchor="center")

        self.tree.pack(expand=True, fill="both")

        # Adiciona evento de clique duplo para selecionar/deselecionar
       # self.tree.bind("<Double-1>", self._on_treeview_double_click)
        self.tree.bind("<<TreeviewSelect>>", self._mostrar_detalhes_evento)

    def _atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for idx, evento in enumerate(self.eventos_filtrados):
            evento_id = (evento.nome, evento.horario, evento.local, evento.preco)
            selecionado = "✔" if evento_id in self.eventos_escolhidos else ""
            self.tree.insert("", tk.END, iid=idx, values=(selecionado, evento.nome, evento.horario, evento.local, f"R$ {evento.preco:.2f}"))

    """  def _on_treeview_double_click(self, event):
        item_id = self.tree.identify_row(event.y)
        if not item_id:
            return
        idx = int(item_id)
        if idx >= len(self.eventos_filtrados):
            return
        evento = self.eventos_filtrados[idx]
        evento_id = (evento.nome, evento.horario, evento.local, evento.preco)
        if evento_id in self.eventos_escolhidos:
            self.eventos_escolhidos.remove(evento_id)
        else:
            self.eventos_escolhidos.add(evento_id)
        self._atualizar_tabela() """

    def _mostrar_detalhes_evento(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        idx = int(selected_item[0])
        evento = self.eventos_filtrados[idx]

        if hasattr(self, "painel_detalhes") and self.painel_detalhes.winfo_exists():
            self.painel_detalhes.destroy()

        self.painel_detalhes = ctk.CTkFrame(self, width=300, corner_radius=10)
        self.painel_detalhes.pack(side="right", fill="y", padx=10, pady=10)
        # Barra superior com botões de ação
        top_bar = ctk.CTkFrame(self.painel_detalhes, fg_color="transparent")
        top_bar.pack(fill="x", pady=(5, 0), padx=5)

        # Botão de fechar
        botao_fechar = ctk.CTkButton(
            top_bar, text="❌", width=30, height=30, fg_color="transparent", hover_color="#eeeeee",
            command=self.painel_detalhes.destroy
        )
        botao_fechar.pack(side="right", padx=(0, 5))

        

        # Imagem no topo
        image_path = self.define_foto_nome(evento.nome)
        try:
            img = ctk.CTkImage(dark_image=Image.open(image_path), size=(280, 180))
            ctk.CTkLabel(self.painel_detalhes, image=img, text="").pack(pady=(10, 5))
            self.imagem_atual = img
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

        # Faixa de título
        titulo_frame = ctk.CTkFrame(self.painel_detalhes, fg_color="#4ABFB0", corner_radius=8)
        titulo_frame.pack(fill="x", pady=(5, 10), padx=10)

        nome_favorito_frame = ctk.CTkFrame(titulo_frame, fg_color="transparent")
        nome_favorito_frame.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(nome_favorito_frame, text=evento.nome, text_color="white", font=("Arial", 16, "bold")).pack(side="left")

        # Estado de favorito
        self.favoritado = False

        # Labels com ícones e faixas coloridas leves
        info_frame = ctk.CTkFrame(self.painel_detalhes, fg_color="#f0f0f0", corner_radius=10)
        info_frame.pack(fill="both", expand=True, padx=10, pady=5)

        ctk.CTkLabel(info_frame, text=f"🕒 Horário: {evento.horario}", anchor="w").pack(pady=4, padx=10, fill="x")
        ctk.CTkLabel(info_frame, text=f"📍 Local: {evento.local}", anchor="w").pack(pady=4, padx=10, fill="x")
        ctk.CTkLabel(info_frame, text=f"💰 Preço: R$ {evento.preco:.2f}", anchor="w").pack(pady=4, padx=10, fill="x")

        self.icone_off = ctk.CTkImage(light_image=Image.open("../assets/heart_outline.png"), size=(24, 24))
        self.icone_on = ctk.CTkImage(light_image=Image.open("../assets/heart_filled.png"), size=(24, 24))

        # Botão de favoritar
        self.botao_favoritar = ctk.CTkButton(
            nome_favorito_frame,
            image=self.icone_off,
            text="",
            width=36,
            height=36,
            fg_color="transparent",     
            hover_color="#66bb6a",
            corner_radius=18,
            command=self.toggle_favorito
        )
        self.botao_favoritar.pack(side="right", padx=5)
        
        
    def toggle_favorito(self):
        self.favoritado = not self.favoritado
        if self.favoritado:
            self.botao_favoritar.configure(image=self.icone_on, fg_color="#ff4d4d",hover_color="#ff4d4d")  # fundo vermelho
        else:
            self.botao_favoritar.configure(image=self.icone_off, fg_color="transparent",hover_color="#66bb6a",) 
    
      


    def define_foto_nome(self, nome):
     fotos = {
        "ExpoAnime BH": "../assets/Anime.png",
        "Festival de Música de BH": "../assets/FestivalMusica.jpg",
        "Festival Literário BH": "../assets/FestivalLiterario.png",
        "Feira de Tecnologia 2025": "../assets/FeiraTecnologia.jpg",
        "BH Gastrô": "../assets/BhGastro.jpeg",
        "Mostra de Cinema Mineiro": "../assets/CinemaMineiro.png",
        "Encontro de Startups": "../assets/WeWork.png",
        "Corrida da Liberdade": "../assets/CorridaLiberdade.png",
        "Congresso de Arquitetura": "../assets/Arquitetura.png",
        "Simpósio de Saúde Mental": "../assets/SaudeMental.png"

     }

     return fotos.get(nome, "../assets/default.png")


    def mostrar_eventos_escolhidos(self):
        if not self.eventos_escolhidos:
            messagebox.showinfo("Meus Eventos", "Nenhum evento selecionado.")
            return
        eventos = []
        for evento in self.eventos_originais:
            evento_id = (evento.nome, evento.horario, evento.local, evento.preco)
            if evento_id in self.eventos_escolhidos:
                eventos.append(evento)
        texto = "\n".join([f"{e.nome} - {e.horario} - {e.local} - R$ {e.preco:.2f}" for e in eventos])
        messagebox.showinfo("Meus Eventos", texto)

    def _aplicar_filtro(self):
        nome_digitado = self.nome_filtro.get().lower()
        horario_digitado = self.horario_filtro.get()
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
            horario_match = horario_digitado in evento.horario
            local_match = local_digitado in evento.local.lower()
            preco_match = evento.preco <= preco_max

            if nome_match and horario_match and local_match and preco_match:
                self.eventos_filtrados.append(evento)

        self._atualizar_tabela()

    def _limpar_filtro(self):
        self.nome_filtro.set("")
        self.horario_filtro.set("")
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
