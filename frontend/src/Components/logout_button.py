import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
class LogoutButton(ctk.CTkButton):
    def __init__(self, parent, api_client, controller):
        pil_image = Image.open("../assets/logout_icon_white.png").resize((42, 42), Image.Resampling.LANCZOS)
        ctk_image = ctk.CTkImage(light_image=pil_image, size=(42, 42))
        
        super().__init__(
            master=parent,
            text="Logout",
            command=self.fazerLogout,
            fg_color="#E53935",
            text_color="white",
            font=('Arial', 22, 'bold'),
            corner_radius=20,
            image=ctk_image,
            compound="left"
        )

        self.api_client = api_client
        self.controller = controller
        self.pack(side="right", padx=15, pady=10)

    def fazerLogout(self):
        self.api_client.logout()
        self.controller.show_frame("HomePage")

