# menu_lateral.py
import customtkinter as ctk
from PIL import Image
from Components.logout_button import LogoutButton
class MenuLateralFrame(ctk.CTkFrame):
    def __init__(self, parent, fechar_callback=None, **kwargs):
        super().__init__(parent, width=250, fg_color="#B2EBF2", **kwargs)
        self.fechar_callback = fechar_callback
        self.api_client = parent.api_client
        self.controller = parent.controller

        # Barra superior
        top_bar = ctk.CTkFrame(self, fg_color="transparent")
        top_bar.pack(fill="x", pady=(5, 0), padx=5) 
        ctk.CTkButton(
            top_bar, text="❌", width=30, height=30, fg_color="transparent",
            hover_color="#eeeeee", command=self._fechar
        ).pack(side="right", padx=(0, 5))

        frame_usuario = ctk.CTkFrame(self, fg_color="#4ABFB0", corner_radius=20)
        frame_usuario.pack(fill="x", pady=(5, 0), padx=5)

        self.icone_capivara = ctk.CTkImage(light_image=Image.open("../assets/botao_capivara.png"), size=(32, 32))    

        self.usuarioLogado = self.api_client.getDadosLogado()

        # Ícone no fundo escuro
        ctk.CTkLabel(frame_usuario, image=self.icone_capivara, text="").pack(side="left", padx=10, pady=10)

        # Frame externo com cor da borda
        borda_frame = ctk.CTkFrame(frame_usuario, fg_color="#00796B", corner_radius=22)  # cor da borda
        borda_frame.pack(side="left", padx=10, pady=10)

        # Frame interno com fundo claro e cantos menores para parecer uma borda
        mensagem_frame = ctk.CTkFrame(borda_frame, fg_color="#B2DFDB", corner_radius=20)
        mensagem_frame.pack(padx=2, pady=2)  # Espaçamento pequeno para mostrar a borda

        # Texto de boas-vindas
        if hasattr(self, 'bem_vindo_label'):
            self.bem_vindo_label.configure(text=f"Bem vindo(a), {self.usuarioLogado.nome}")
        else:
            self.bem_vindo_label = ctk.CTkLabel(
                mensagem_frame,
                text=f"Bem vindo(a), {self.usuarioLogado.nome}",
                font=('Arial', 26, 'bold'),
                text_color="#333333"
            )
            self.bem_vindo_label.pack(padx=15, pady=10)

        self.logout_frame = ctk.CTkFrame(self, fg_color="#929797", corner_radius=20)    
        self.logout_frame.pack(padx=50, pady=50)
        LogoutButton(self.logout_frame, self.api_client, self.controller)
        
          
    

        

    def _fechar(self):
        if self.fechar_callback:
            self.fechar_callback()
        self.place_forget()  # Oculta o frame lateral
