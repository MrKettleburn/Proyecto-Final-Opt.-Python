import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageResampling
import pygame 

pygame.mixer.init()

class MainScreen(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.pack()
        self.create_widgets()
        self.play_open_sound()
    
    def create_widgets(self):
        self.master.geometry("640x964")
        
        self.set_background("FondoMusicApp.jpg")   
        
        play_button = tk.Button(self, text="Play Music", command=self.app.show_play_screen)
        play_button.config(font=("Helvetica", 16), bg="blue", fg="white")
        play_button.pack(pady=20)
           
        note_button = tk.Button(self, text="Play Notes", command=self.app.show_note_keyboard_screen)
        note_button.config(font=("Helvetica", 16), bg="green", fg="white")
        note_button.pack(pady=20)
    
    def set_background(self, image_path):
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((640, 964), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        
        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def play_open_sound(self):
        # Cargar y reproducir el sonido de apertura
        pygame.mixer.music.load("Sonidos\Ambient-piano-logo-165357.mp3")
        pygame.mixer.music.play()

