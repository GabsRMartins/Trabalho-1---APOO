import tkinter as tk
import webbrowser

class MapPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Página Mapa", font=("Arial", 24))
        label.pack(pady=40)

        btn_mapa = tk.Button(self, text="Abrir Mapa", command=self.abrir_mapa)
        btn_mapa.pack(pady=10)

        btn_voltar = tk.Button(self, text="Voltar para Home", command=lambda: controller.show_frame("HomePage"))
        btn_voltar.pack()

    def abrir_mapa(self):
        url = "https://www.google.com/maps/place/Belo+Horizonte"
        webbrowser.open(url)
