import tkinter as tk
from TelaInicial import HomePage  
from TelaMapa import MapPage

class AppRouter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicação com Router")
        self.state("zoomed")  # Maximiza a janela
        self.attributes("-alpha", 0.97)

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, MapPage):  # Adicione novas páginas aqui
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")
       

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

