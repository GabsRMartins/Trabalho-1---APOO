import tkinter as tk
from tkhtmlview import HTMLLabel

class MapPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Página Mapa", font=("Arial", 24))
        label.pack(pady=40)
        html_code = """
        <iframe
            width="600"
            height="450"
            style="border:0"
            loading="lazy"
            allowfullscreen
            referrerpolicy="no-referrer-when-downgrade"
            src="https://www.google.com/maps/embed/v1/place?key=AIzaSyAfWpbtUjNOrUi970MYcF8wmtcfO_h-TFQ&q=Belo+Horizonte">
        </iframe>
        """
        html_label = HTMLLabel(self, html=html_code)
        html_label.pack(padx=20, pady=20)

        btn_voltar = tk.Button(self, text="Voltar para Home", command=lambda: controller.show_frame("HomePage"))
        btn_voltar.pack()
