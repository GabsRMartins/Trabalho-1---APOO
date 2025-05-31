import customtkinter as ctk

class Alerta(ctk.CTkFrame):
    def __init__(self, master, mensagem, tipo="erro", duracao=3000):
        super().__init__(master, corner_radius=10, bg_color="transparent")
        
        # Define cor e ícone
        if tipo == "erro":
            cor = "#ff4d4d"
            icone = "⚠"
        else:  # tipo == "sucesso"
            cor = "#4CAF50"
            icone = "✓"

        self.configure(fg_color=cor)

        # Frame interno com ícone + mensagem
        self.container = ctk.CTkFrame(self, fg_color="transparent", bg_color="transparent")
        self.container.pack(padx=10, pady=5)

        # Ícone
        self.icon_label = ctk.CTkLabel(self.container, text=icone, text_color="white", font=("Arial", 16, "bold"))
        self.icon_label.grid(row=0, column=0, padx=(0, 10))

        # Mensagem
        self.text_label = ctk.CTkLabel(self.container, text=mensagem, text_color="white", font=("Arial", 12))
        self.text_label.grid(row=0, column=1)

        # Posiciona o alerta
        self.place(relx=0.5, rely=0.05, anchor="n")

        # Auto-destruição após X ms
        self.after(duracao, self.destroy)
