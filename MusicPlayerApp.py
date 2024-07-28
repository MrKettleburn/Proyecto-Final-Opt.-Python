import tkinter as tk
from tkinter import ttk
from MainScreen import MainScreen
from PlayScreen import PlayScreen
from NoteKeyboardScreen import NoteKeyboardScreen
import pygame 

pygame.mixer.init()

class MusicPlayerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Music Player")
        self.current_screen = None
        self.show_main_screen()
        self.play_open_sound()
    
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

    def play_open_sound(self):
        pygame.mixer.music.load("Sonidos\Ambient-piano-logo-165357.mp3")
        pygame.mixer.music.play()

    
    def run(self):
        self.root.mainloop()