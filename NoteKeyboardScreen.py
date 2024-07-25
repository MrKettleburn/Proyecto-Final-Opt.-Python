import tkinter as tk
from tkinter import ttk

class NoteKeyboardScreen(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.pack()
        self.create_widgets(master)
    
    def create_widgets(self, root):
       pass