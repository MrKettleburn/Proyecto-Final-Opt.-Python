import tkinter as tk
from tkinter import ttk
from MainScreen import MainScreen
from PlayScreen import PlayScreen
from NoteKeyboardScreen import NoteKeyboardScreen

class MusicPlayerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Music Player")
        self.current_screen = None
        self.show_main_screen()
    
    def show_main_screen(self):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = MainScreen(self.root, self)
    
    def show_play_screen(self):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = PlayScreen(self.root, self)
    
    def show_note_keyboard_screen(self):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = NoteKeyboardScreen(self.root, self)
    
    def run(self):
        self.root.mainloop()