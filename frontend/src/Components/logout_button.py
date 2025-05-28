import customtkinter as ctk

class LogoutButton(ctk.CTkButton):
    def __init__(self, parent,command,controller):
        super().__init__(
            master=parent,
            text="Logout",
            command=self.fazerLogout,
            fg_color="#E53935",
            text_color="white",
            font=('Arial', 10, 'bold'),
            corner_radius=20
        )
        self.controller = controller
        self.api_client = controller.api_client
        self.pack(side="right", padx=15, pady=10)

    def fazerLogout(self):
        self.api_client.logout()
        self.controller.show_frame("HomePage")
