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


class UserEvent(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.api_client = controller.api_client
        self.usuarioLogado = None
        self.estado_favoritos = controller.estado_favoritos
        self.menu_lateral = None
        

        self.frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#A7D7C5")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título inicial (será atualizado em on_show)
        self.titulo_label = ctk.CTkLabel(
            self.frame,
            text="...",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.titulo_label.pack(pady=(20, 10))

        self.lista_frame = ctk.CTkFrame(self.frame)
        self.lista_frame.pack(fill="both", expand=True, pady=(10,0))

        # Botão do menu (capivara)
        self._configurar_botao_menu()

        
       

    def _configurar_botao_menu(self):
        img = Image.open("../assets/botao_capivara.png").resize((60, 60), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        self.menu_button = tk.Button(
            self, image=img_tk, bg="#E3F2FD", bd=0, command=self.toggle_menu_lateral
        )
        self.menu_button.image = img_tk
        self.menu_button.place(x=10, y=10)

    def on_show(self):
        self.estado_favoritos = self.controller.estado_favoritos 
        if self.menu_lateral:
            self.menu_lateral.destroy()
            self.menu_lateral = None
        self.usuarioLogado = self.api_client.getDadosLogado()
        
        if self.usuarioLogado.tipo == 1:
            mensagem = "Rolês Curtidos"
        else:
            mensagem = "Eventos Cadastrados"

       
        self.titulo_label.configure(text=mensagem)

        self.eventos = self.define_eventos()
        self._criar_lista()

    def define_eventos(self):
        if (self.usuarioLogado.tipo == 1):
            return self.estado_favoritos
        else:
             return self.api_client.getEventosByName(self.usuarioLogado.nome)


    def _criar_lista(self):
    # Remove itens antigos só da lista de eventos
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        if not self.eventos:
            ctk.CTkLabel(self.lista_frame, text="Nenhum rolê adicionado ainda :C").pack(pady=10)
            return

        for evento in self.eventos:
            self.criar_item_evento(evento)

    def criar_item_evento(self, evento):
        item = ctk.CTkFrame(
            self.lista_frame,
            fg_color="#ffffff",
            corner_radius=12,
            border_color="#4ABFB0",
            border_width=2
        )
        item.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(item, text=evento.nome, font=("Sofia Sans", 18, "bold"), text_color="#333F48").pack(
            fill="x", padx=15, pady=(10, 2), anchor="w"
        )
        ctk.CTkLabel(
            item,
            text=f"🕒 {evento.horario}  |  📍 {evento.local}  |  💰 R$ {evento.preco:.2f}",
            font=("Sofia Sans", 14),
            text_color="#555"
        ).pack(fill="x", padx=15, pady=(0, 10), anchor="w")

        if self.usuarioLogado.tipo == 1:
            self._adicionar_avaliacao(item)

    def _adicionar_avaliacao(self, parent):
        nota_label = ctk.CTkLabel(
            parent,
            text="Avalie este rolê:",
            font=("Sofia Sans", 14, "bold"),
            text_color="#333F48"
        )
        nota_label.pack(padx=10, pady=(0, 5), anchor="w")

        nota_frame = ctk.CTkFrame(parent, fg_color="transparent")
        nota_frame.pack(padx=10, pady=(0, 5), anchor="w")

        # Rótulo com nota à direita das estrelas
        nota_exibida = ctk.CTkLabel(
            nota_frame,
            text="Nota atual: -",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#555"
        )
        nota_exibida.pack(side="right", padx=(10, 0))

        estrelas_frame = ctk.CTkFrame(nota_frame, fg_color="transparent")
        estrelas_frame.pack(side="left")

        for i in range(1, 6):
            estrela = ctk.CTkButton(
                estrelas_frame,
                text="★",
                width=30,
                height=30,
                fg_color="#FFD700",
                hover_color="#FFC107",
                text_color="#333",
                corner_radius=8,
                command=lambda nota=i: self._enviar_avaliacao(nota, nota_exibida)
            )
            estrela.pack(side="left", padx=2)

   
    def _enviar_avaliacao(self, nota, label_nota):
        label_nota.configure(text=f"Nota atual: {nota} / 5")
        Alerta(self, "Obrigado pela sua avaliação!", "success")


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
