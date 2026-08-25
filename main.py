import customtkinter as ctk
from app.ui import App
from app.fonts import load_fonts

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
load_fonts()
app = App()
app.mainloop()
