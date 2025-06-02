import tkinter as tk
from TelaInicial import HomePage  
from TelaMapa import MapPage
from TelaEventosLocais import EventPage
from ApiClient import ApiClient
from TelaCadastraEvento import EventRegister
from TelaEventoUsuario import UserEvent

class AppRouter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.api_client = ApiClient()
        self.title("Role do Dia")
        self.state("zoomed")  # Maximiza a janela
        self.attributes("-alpha", 1)

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, MapPage, EventPage, EventRegister,UserEvent):  # Adicione novas páginas aqui
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")
       

    def show_frame(self, page_name):
     frame = self.frames[page_name]
     frame.tkraise()
     if hasattr(frame, 'on_show'):
        frame.on_show()

