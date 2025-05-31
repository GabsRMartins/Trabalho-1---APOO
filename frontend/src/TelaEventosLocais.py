import tkinter as tk
from tkinter import ttk, messagebox
from TelaInicial import HomePage
from PIL import Image, ImageTk
from ApiClient import ApiClient
from Components.logout_button import LogoutButton
import customtkinter as ctk
from Components.detalhes_evento_frame import DetalhesEventoFrame
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
        self.usuarioLogado = None 
        self.carregado = False
        self.eventos_originais = self.api_client.getEventos()
        self.eventos_filtrados = list(self.eventos_originais)  
        self.eventos_escolhidos = set()  # Armazena índices dos eventos escolhidos


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
        validador = Validador()

        filtro_frame = ctk.CTkFrame(self.frame, corner_radius=10, fg_color="#E3F2FD")
        filtro_frame.pack(pady=(0, 10), padx=10, fill="x")

        titulo = ctk.CTkLabel(filtro_frame, text="🎯 Filtrar Eventos", font=("Arial", 16, "bold"), text_color="#0D47A1")
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

        entry_horario = ctk.CTkEntry(filtro_frame, textvariable=self.horario_filtro, width=150)
        entry_horario.grid(row=1, column=3, padx=5, pady=5)
        entry_horario.bind("<KeyRelease>", lambda e: self.mascarar_horario_valido(self.horario_filtro)) 

        entry_preco = ctk.CTkEntry(filtro_frame, textvariable=self.preco_filtro, width=150)
        entry_preco.grid(row=1, column=7, padx=5, pady=5)
        entry_preco.bind("<KeyRelease>", lambda e: self.mascarar_preco_valido(self.preco_filtro))
                

        ctk.CTkButton(
            filtro_frame, text="🔍 Filtrar", command=self._aplicar_filtro,
            fg_color="#2196F3", hover_color="#1976D2", text_color="white", width=100
        ).grid(row=1, column=8, padx=10, pady=5)

        ctk.CTkButton(
            filtro_frame, text="❌ Limpar Filtro", command=self._limpar_filtro,
            fg_color="#F44336", hover_color="#D32F2F", text_color="white", width=150
        ).grid(row=2, column=0, columnspan=9, pady=10)


    def mascarar_horario_valido(self,var: ctk.StringVar):
        valor = var.get()
        apenas_digitos = ''.join(filter(str.isdigit, valor))[:4]  # pega só os primeiros 4 dígitos

        if len(apenas_digitos) == 0:
            resultado = ""
        elif len(apenas_digitos) == 1:
            # Aceita 0 a 2 no primeiro dígito
            if apenas_digitos[0] > '2':
                resultado = "2"
            else:
                resultado = apenas_digitos
        elif len(apenas_digitos) == 2:
            # Valida as horas de 00 a 23
            horas = int(apenas_digitos)
            if horas > 23:
                resultado = "23"
            else:
                resultado = f"{horas:02d}"
        elif len(apenas_digitos) == 3:
            # Formato: HH:M, minuto incompleto, completa com 0
            horas = int(apenas_digitos[:2])
            minutos_1 = int(apenas_digitos[2])
            if horas > 23:
                horas = 23
            if minutos_1 > 5:  # minutos não podem começar com >5
                minutos_1 = 5
            resultado = f"{horas:02d}:{minutos_1}0"
        else:  # 4 dígitos completos HHMM
            horas = int(apenas_digitos[:2])
            minutos = int(apenas_digitos[2:])
            if horas > 23:
                horas = 23
            if minutos > 59:
                minutos = 59
            resultado = f"{horas:02d}:{minutos:02d}"

        var.set(resultado)

    def mascarar_preco_valido(self,var: ctk.StringVar):
        valor = var.get()

        # Remove caracteres inválidos (só números e vírgula ou ponto)
        valor = valor.replace(",", ".")  # aceita vírgula como ponto
        permitido = ''.join(c for c in valor if c.isdigit() or c == '.')

        # Divide em parte inteira e decimal
        if '.' in permitido:
            partes = permitido.split('.', 1)
            inteiro = partes[0]
            decimal = partes[1][:2]  # apenas 2 casas decimais
            resultado = f"{inteiro}.{decimal}"
        else:
            resultado = permitido

        var.set(resultado)



    def _criar_tabela(self):
        self.titulo_tabela = ctk.CTkLabel(
            self.frame,
            text="📋 Lista de Eventos",
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
            selecionado = "✔" if evento_id in self.eventos_escolhidos else ""
            self.tree.insert("", tk.END, iid=idx, values=(selecionado, evento.nome, evento.horario, evento.local, f"R$ {evento.preco:.2f}"))


    def _mostrar_detalhes_evento(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        idx = int(selected_item[0])
        evento = self.eventos_filtrados[idx]

        if hasattr(self, "painel_detalhes") and self.painel_detalhes.winfo_exists():
            self.painel_detalhes.destroy()

        self.painel_detalhes = DetalhesEventoFrame(self, evento, self.define_foto_nome)


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
        preco_max_str = self.preco_filtro.get().replace(",", ".")
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


    # Essa função é apenas para simular a inserção de eventos. Usuários ativos não criam novos eventos.
    def inserir_evento(self, evento):
        self.eventos_originais.append(evento)
        self.eventos_filtrados.append(evento)
        self._atualizar_tabela()

  
