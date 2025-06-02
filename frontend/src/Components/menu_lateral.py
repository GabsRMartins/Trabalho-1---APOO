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

        self.configure(corner_radius=15)  # borda arredondada geral

        # === Barra superior ===
        top_bar = ctk.CTkFrame(self, fg_color="transparent")
        top_bar.pack(fill="x", pady=(5, 0), padx=5)

        ctk.CTkButton(
            top_bar,
            text="❌",
            width=30,
            height=30,
            fg_color="transparent",
            hover_color="#D9F3F2",
            command=self._fechar
        ).pack(side="right", padx=(0, 5))

        # === Bloco do usuário ===
        frame_usuario = ctk.CTkFrame(
            self,
            fg_color="#4ABFB0",
            corner_radius=20,
            height=100
        )
        frame_usuario.pack(fill="x", padx=10, pady=(10, 0))

        self.icone_capivara = ctk.CTkImage(light_image=Image.open("../assets/botao_capivara.png"), size=(32, 32))
        self.usuarioLogado = self.api_client.getDadosLogado()
        print(self.usuarioLogado)

        # Ícone
        ctk.CTkLabel(frame_usuario, image=self.icone_capivara, text="").pack(side="left", padx=10)
        
        # === Moldura com efeito de borda ===
        borda_frame = ctk.CTkFrame(frame_usuario, fg_color="#00796B", corner_radius=22)
        borda_frame.pack(side="left", padx=5, pady=10)

        mensagem_frame = ctk.CTkFrame(borda_frame, fg_color="#B2DFDB", corner_radius=20)
        mensagem_frame.pack(padx=2, pady=2)

        self.bem_vindo_label = ctk.CTkLabel(
            mensagem_frame,
            text=f"Bem vindo(a), {self.usuarioLogado.nome}",
            font=('Arial', 20, 'bold'),
            text_color="#333333"
        )
        self.bem_vindo_label.pack(padx=15, pady=10)


        self.middle_frame = ctk.CTkFrame(self, fg_color="#A7D7C5", corner_radius=15, height=180)
        self.middle_frame.pack(fill="x", padx=15, pady=20)
        self.middle_frame.pack_propagate(False)
        self.avaliaTipo()

        # === Espaço expansível ===
        ctk.CTkFrame(self, fg_color="transparent").pack(expand=True)

        # === Botão de Logout fixado embaixo ===
        self.logout_frame = ctk.CTkFrame(self, fg_color="#C8D7D8", corner_radius=15)
        self.logout_frame.pack(side="bottom", fill="x", padx=15, pady=20)

        LogoutButton(self.logout_frame, self.api_client, self.controller)
          
    

    
       def _fechar(self):
            if self.fechar_callback:
                self.fechar_callback()
            self.place_forget()  # Oculta o frame lateral

       def avaliaTipo(self):
        if self.usuarioLogado.tipo == 1:
            texto_usuario = "Ver Rolês Curtidos"
            texto_voltar = "Tela de Rolês"
        else:
            texto_usuario = "Ver Eventos Registrados"
            texto_voltar = "Tela de Cadastrar Eventos"

        # Usar grid para centralizar verticalmente os botões no middle_frame
        self.middle_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.middle_frame.grid_columnconfigure(0, weight=1)

        self.botaoVoltar = ctk.CTkButton(
            self.middle_frame,
            text=texto_voltar,
            font=('Arial', 20, 'bold'),
            corner_radius=15,
            fg_color="#81D4FA",         # Azul suave
            hover_color="#4FC3F7",      # Azul mais forte no hover
            text_color="#ffffff",
            height=45,
            width=200,
            command=self.voltar
        )
        self.botaoVoltar.grid(row=0, column=0, pady=(20, 10))

        self.botaoUsuario = ctk.CTkButton(
            self.middle_frame,
            text=texto_usuario,
            font=('Arial', 20, 'bold'),
            corner_radius=15,
            fg_color="#4DB6AC",         # Verde água suave
            hover_color="#00897B",      # Verde escuro no hover
            text_color="#ffffff",
            height=45,
            width=200,
            command=self.redirecionaEventosUsuario
        )
        self.botaoUsuario.grid(row=1, column=0, pady=(10, 20))


       def redirecionaEventosUsuario(self):
               self.controller.show_frame("UserEvent")
        

       def voltar(self):
            if(self.usuarioLogado.tipo == 1):
               self.controller.show_frame("EventPage")
            else:
                self.controller.show_frame("EventRegister") 