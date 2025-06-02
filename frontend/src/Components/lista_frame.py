import customtkinter as ctk
from fpdf import FPDF
from datetime import datetime
from PIL import Image, ImageTk
from Components.alerta import Alerta
from Components.pdf_custom import CustomPDF

class ListaFrame(ctk.CTkFrame):
    def __init__(self, parent, eventos,fechar_callback=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.fechar_callback = fechar_callback
        self.eventos = sorted(eventos, key=lambda e: datetime.strptime(e.horario, "%H:%M"))
        # PIL image
        self.original_image = Image.open("../assets/botao_capivara.png")

        # Converta para CTkImage
        ctk_image = ctk.CTkImage(light_image=self.original_image)

        # Use no label
        self.bg_label = ctk.CTkLabel(self, image=ctk_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.lower()  # Garante que o frame fique acima

        # Barra superior
        self.top_bar = ctk.CTkFrame(self, fg_color="transparent")
        self.top_bar.pack(fill="x", pady=(5, 0), padx=5) 
        ctk.CTkButton(
            self.top_bar, text="❌", width=30, height=30, fg_color="transparent",
            hover_color="#eeeeee", command=self._fechar
        ).pack(side="right", padx=(0, 5))

        self._verificapreenchimento()
        

    def _criar_lista(self):
        if not self.eventos:
            ctk.CTkLabel(self, text="Nenhum rolê adicionado ainda :C").pack(pady=10)
            return

        for evento in self.eventos:
            item = ctk.CTkFrame(self, fg_color="#f0f0f0", corner_radius=10)
            item.pack(fill="x", padx=10, pady=5)

            ctk.CTkLabel(item, text=evento.nome, font=("Arial", 16, "bold"), anchor="w").pack(fill="x", padx=10, pady=2)
            ctk.CTkLabel(item, text=f"🕒 {evento.horario}  |  📍 {evento.local}  |  💰 R$ {evento.preco:.2f}",
                        anchor="w", font=("Arial", 14)).pack(fill="x", padx=10, pady=2)


    def _criar_botao_pdf(self):
        ctk.CTkButton(
            self,
            text="📄 Baixar PDF",
            command=self.gerar_pdf,
            fg_color="#4CAF50",
            text_color="white"
        ).pack(pady=10)

    def gerar_pdf(self):
        bg_path = "../assets/botao_capivara.png"  # caminho da imagem de fundo

        pdf = CustomPDF(bg_path)
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", "B", 20)
        pdf.set_fill_color(74, 191, 176)  # Cor de fundo (ex: verde água)
        pdf.set_text_color(255, 255, 255)  # Cor do texto (branco)
        pdf.set_draw_color(64, 160, 150)  # Cor da borda (um tom mais escuro do fundo)
        pdf.set_line_width(0.8)

        x = 10
        y = pdf.get_y()
        w = 190
        h = 15

        # Caixa com fundo e borda para o título
        pdf.rect(x, y, w, h, style='DF')

        # Texto do título, centralizado e em negrito
        pdf.set_xy(x, y + 4)
        pdf.set_font("Arial", "B", 16)
        pdf.cell(w, 6, "Lista de Rolês", border=0, align="C")

        # Ajusta o cursor para o próximo conteúdo, com um espaço extra
        pdf.ln(h + 5)

        # Volta à cor de texto normal preta para os eventos
        pdf.set_text_color(0, 0, 0)

        pdf.ln(10)

        for evento in self.eventos:
            pdf.add_event_card(
                nome=evento.nome,
                horario=evento.horario,
                local=evento.local,
                preco=evento.preco
            )

        pdf.output("eventos.pdf")
        Alerta(self.top_bar, "PDF gerado com sucesso.", tipo="sucesso")



    def _fechar(self):
        if self.fechar_callback:
            self.fechar_callback()
        self.destroy()  

    def _verificapreenchimento(self):
        if not self.eventos:
            label = ctk.CTkLabel(
                self,
                text="Nenhum rolê adicionado ainda :C",
                font=("Arial", 16, "bold"))
            label.place(relx=0.5, rely=0.5, anchor="center")
            return
        else:
            self._criar_lista()
            self._criar_botao_pdf()