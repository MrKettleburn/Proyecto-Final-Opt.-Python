import tkinter as tk
from tkinter import ttk

class PlayScreen(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        # Aquí irán los controles de reproducción de música
        pass