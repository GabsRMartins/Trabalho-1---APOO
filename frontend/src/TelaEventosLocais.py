import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk
from Components.detalhes_evento_frame import DetalhesEventoFrame
from Components.menu_lateral import MenuLateralFrame
from Components.lista_frame import ListaFrame
from Utils.validador import Validador


# class Evento:
#     def __init__(self, nome, horario, local, preco):
#         self.nome = nome
#         self.horario = horario
#         self.local = local
#         self.preco = preco

class EventPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#E3F2FD") 
        self.form_bg = "#4ABFB0" 
        
        self.controller = controller
        self.api_client = controller.api_client
        self.validador = Validador()
        self.menu_lateral = None
        self.usuarioLogado = None 
        self.carregado = False
        self.eventos_originais = self.api_client.getEventos()
        self.eventos_filtrados = list(self.eventos_originais)  
        self.estado_favoritos = {}
        self.estado_adicionados = {}

        self.frame = tk.Frame(self, bg=self.form_bg, padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        imagem_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        imagem_frame.pack(fill="x", pady=(10, 0))

        self.slogan = ctk.CTkImage(light_image=Image.open("../assets/TelaEventos.png"), size=(200, 200))
        ctk.CTkLabel(imagem_frame, image=self.slogan, text="").pack()

        self.controller.estado_favoritos = self.filtrar_eventos_curtidos(self.eventos_originais,self.estado_favoritos)
        self.header_frame = tk.Frame(self.frame, bg=self.form_bg)
        self.header_frame.pack(fill="x", pady=(0,10))
        controller.estado_favoritos = self.filtrar_eventos_curtidos(self.eventos_originais,self.estado_favoritos)
        self.botao_verLista = ctk.CTkButton( self.header_frame, 
           text="Imprimir Lista UAI", width=30, height=30,
           command=self.verLista,
            fg_color="#E53935",
            text_color="white",
            font=('Arial', 22, 'bold'),
            corner_radius=20,
            compound="left"
        )
        self.botao_verLista.pack(side="right", padx=(0, 5))

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

        
        self._criar_interface_filtro()
        self._criar_tabela()
        self._atualizar_tabela()

   

    def _criar_interface_filtro(self):
        validador = Validador()

        filtro_frame = ctk.CTkFrame(self.frame, corner_radius=10, fg_color="#E3F2FD")
        filtro_frame.pack(pady=(0, 10), padx=10, fill="x")

        titulo = ctk.CTkLabel(filtro_frame, text="🎯 Achar seu Rolê", font=("Arial", 16, "bold"), text_color="#0D47A1")
        titulo.grid(row=0, column=0, columnspan=9, pady=(10, 10), sticky="w", padx=10)

        # Variáveis
        self.nome_filtro = ctk.StringVar()
        self.horario_filtro = ctk.StringVar()
        self.local_filtro = ctk.StringVar()
        self.preco_filtro = ctk.StringVar()

  

        vcmd = self.register(validador.validar_numeros)  # Registrar o método externo

        campos = [
            ("Nome:", self.nome_filtro, None),
            ("Horário:", self.horario_filtro, vcmd),
            ("Local:", self.local_filtro, None),
            ("Preço Máximo:", self.preco_filtro, vcmd)
        ]

        for i, (label_text, var, val_cmd) in enumerate(campos):
            ctk.CTkLabel(filtro_frame, text=label_text, font=('Arial', 12), text_color="#0D47A1")\
                .grid(row=1, column=i*2, padx=5, pady=5, sticky="w")
            entry = ctk.CTkEntry(filtro_frame, textvariable=var, width=150)
            if val_cmd:
                entry.configure(validate="key", validatecommand=(val_cmd, "%P"))
            entry.grid(row=1, column=i*2+1, padx=5, pady=5)

        self.entry_horario_var = ctk.StringVar()
        entry_horario = ctk.CTkEntry(filtro_frame, textvariable=self.entry_horario_var, width=150)
        entry_horario.grid(row=1, column=3, padx=5, pady=5) 
        self.entry_horario_var.trace_add("write", lambda *args: Validador.horario_valido(self.entry_horario_var))

        self.entry_preco_var = ctk.StringVar()
        entry_preco = ctk.CTkEntry(filtro_frame, textvariable=self.entry_preco_var, width=150)
        entry_preco.grid(row=1, column=7, padx=5, pady=5)
        self.entry_preco_var.trace_add("write", lambda *args: Validador.preco_valido(self.entry_preco_var))
                

        ctk.CTkButton(
            filtro_frame, text="🔍 Filtrar", command=self._aplicar_filtro,
            fg_color="#2196F3", hover_color="#1976D2", text_color="white", width=100
        ).grid(row=1, column=8, padx=10, pady=5)

        ctk.CTkButton(
            filtro_frame, text="❌ Limpar Filtro", command=self._limpar_filtro,
            fg_color="#F44336", hover_color="#D32F2F", text_color="white", width=150
        ).grid(row=2, column=0, columnspan=9, pady=10)

        
    def toggle_menu_lateral(self):
        if self.menu_lateral and self.menu_lateral.winfo_ismapped():
            self.menu_lateral.place_forget()
        else:
            # Sempre cria uma nova instância com dados atualizados
            if self.menu_lateral:
                self.menu_lateral.destroy()

            self.menu_lateral = MenuLateralFrame(self, fechar_callback=self.fechar_menu_lateral)
            self.menu_lateral.place(x=0, y=0, relheight=1)

            
    def fechar_menu_lateral(self):
        if self.menu_lateral:
            self.menu_lateral.place_forget()


   


    def _criar_tabela(self):
        self.titulo_tabela = ctk.CTkLabel(
            self.frame,
            text="📋 Rolês de Hoje",
            font=('Arial', 20, 'bold'),
            text_color="#333333"
        )
        self.titulo_tabela.pack(pady=(0, 10))

        # Estilo para o Treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#FFFFFF",
                        foreground="#000000",
                        rowheight=28,
                        fieldbackground="#F9F9F9",
                        font=('Arial', 11))
        style.map('Treeview', background=[('selected', '#90CAF9')])

        colunas = ("Selecionar", "Nome", "Horário", "Local", "Preço")
        self.tree = ttk.Treeview(self.frame, columns=colunas, show="headings")

        self.tree.heading("Selecionar", text="Selecionar")
        self.tree.column("Selecionar", width=90, anchor="center")
        for coluna in colunas[1:]:
            self.tree.heading(coluna, text=coluna)
            self.tree.column(coluna, width=160, anchor="center")

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self._mostrar_detalhes_evento)

    def _atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for idx, evento in enumerate(self.eventos_filtrados):
            evento_id = (evento.nome, evento.horario, evento.local, evento.preco)
            selecionado = " "
            self.tree.insert("", tk.END, iid=idx, values=(selecionado, evento.nome, evento.horario, evento.local, f"R$ {evento.preco:.2f}"))


    def _mostrar_detalhes_evento(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        idx = int(selected_item[0])
        evento = self.eventos_filtrados[idx]
        evento_id = evento.nome  # ou evento.id, se tiver

        # Inicialize dicionários se não existirem
        if not hasattr(self, "estado_favoritos"):
            self.estado_favoritos = {}
        if not hasattr(self, "estado_adicionados"):
            self.estado_adicionados = {}

        # Recupera estado salvo ou False
        favoritado = self.estado_favoritos.get(evento_id, False)
        adicionado = self.estado_adicionados.get(evento_id, False)

        self.controller.estado_favoritos = self.filtrar_eventos_curtidos(self.eventos_originais,self.estado_favoritos)
        
        # Remove painel anterior se existir
        if hasattr(self, "painel_detalhes") and self.painel_detalhes.winfo_exists():
            self.painel_detalhes.destroy()

        # Cria novo painel com os estados e funções de salvamento
        self.painel_detalhes = DetalhesEventoFrame(
            self,
            evento,
            self.define_foto_nome,
            favoritado=favoritado,
            adicionado=adicionado,
            salvar_favorito=lambda estado: self.estado_favoritos.update({evento_id: estado}),
            salvar_adicionado=lambda estado: self.estado_adicionados.update({evento_id: estado})
        )



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
    

    def _aplicar_filtro(self):
        nome_digitado = self.nome_filtro.get().lower()
        horario_digitado = self.entry_horario_var.get()
        local_digitado = self.local_filtro.get().lower()
        preco_max_str = self.entry_preco_var.get().replace(",", ".")
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


    def verLista(self):
        if hasattr(self, 'lista_frame') and self.lista_frame.winfo_exists():
            self.lista_frame.destroy()
        eventos = self.filtrar_eventos_adicionados(self.eventos_originais,self.estado_adicionados)
        self.lista_frame = ListaFrame(self, eventos, fechar_callback=self.fechar_lista)
        self.lista_frame.pack(fill="both", expand=True, padx=20, pady=10)
  
    def filtrar_eventos_adicionados(self, eventos_originais, eventos_adicionados):
        return [evento for evento in eventos_originais if eventos_adicionados.get(evento.nome)]
    
    def filtrar_eventos_curtidos(self, eventos_originais, eventos_curtidos):
        return [evento for evento in eventos_originais if eventos_curtidos.get(evento.nome)]
     
     
    def fechar_lista(self):
        if self.lista_frame:
            self.lista_frame.place_forget()