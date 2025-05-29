# detalhes_evento_frame.py
import customtkinter as ctk
from PIL import Image

class DetalhesEventoFrame(ctk.CTkFrame):
    def __init__(self, master, evento, define_foto_nome, *args, **kwargs):
        super().__init__(master, width=300, corner_radius=10, *args, **kwargs)
        self.pack(side="right", fill="y", padx=10, pady=10)

        self.favoritado = False
        self.icone_off = ctk.CTkImage(light_image=Image.open("../assets/heart_outline.png"), size=(24, 24))
        self.icone_on = ctk.CTkImage(light_image=Image.open("../assets/heart_filled.png"), size=(24, 24))

        # Barra superior
        top_bar = ctk.CTkFrame(self, fg_color="transparent")
        top_bar.pack(fill="x", pady=(5, 0), padx=5)
        ctk.CTkButton(
            top_bar, text="❌", width=30, height=30, fg_color="transparent",
            hover_color="#eeeeee", command=self.destroy
        ).pack(side="right", padx=(0, 5))

        # Imagem
        try:
            img = ctk.CTkImage(dark_image=Image.open(define_foto_nome(evento.nome)), size=(280, 180))
            ctk.CTkLabel(self, image=img, text="").pack(pady=(10, 5))
            self.imagem_atual = img
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

        # Título
        titulo_frame = ctk.CTkFrame(self, fg_color="#4ABFB0", corner_radius=8)
        titulo_frame.pack(fill="x", pady=(5, 10), padx=10)
        nome_favorito_frame = ctk.CTkFrame(titulo_frame, fg_color="transparent")
        nome_favorito_frame.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(nome_favorito_frame, text=evento.nome, text_color="white", font=("Arial", 16, "bold")).pack(side="left")

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

        # Informações
        info_frame = ctk.CTkFrame(self, fg_color="#f0f0f0", corner_radius=10)
        info_frame.pack(fill="both", expand=True, padx=10, pady=5)

        ctk.CTkLabel(info_frame, text=f"🕒 Horário: {evento.horario}", anchor="w", font=("Arial", 14, "bold")).pack(pady=4, padx=10, fill="x")
        ctk.CTkLabel(info_frame, text=f"📍 Local: {evento.local}", anchor="w", font=("Arial", 14, "bold") ).pack(pady=4, padx=10, fill="x")
        ctk.CTkLabel(info_frame, text=f"💰 Preço: R$ {evento.preco:.2f}", anchor="w",  font=("Arial", 14, "bold")).pack(pady=4, padx=10, fill="x")

        # Botão Adicionar na lista
        ctk.CTkButton(
            self, text="➕ Adicionar evento na lista", command=self.adicionar_evento_lista,
            fg_color="#F44336", hover_color="#D32F2F", text_color="white", width=150
        ).pack(pady=4, padx=10, fill="x")


    def toggle_favorito(self):
        self.favoritado = not self.favoritado
        if self.favoritado:
            self.botao_favoritar.configure(image=self.icone_on, fg_color="#ff4d4d", hover_color="#ff4d4d")
        else:
            self.botao_favoritar.configure(image=self.icone_off, fg_color="transparent", hover_color="#66bb6a")

    def adicionar_evento_lista(self):
        print("Adicionou")