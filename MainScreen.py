import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pygame 

pygame.mixer.init()

class MainScreen(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.pack(expand=True, fill='both')
        self.create_widgets()
        self.play_open_sound()
    
    def create_widgets(self):
        self.master.geometry("640x704")
        
        self.set_background("Photos\FondoMusicApp.jpg")   
        
        self.create_button_with_label("Play Music", "Photos\Play.jpg", self.app.show_play_screen, 180, 80)
        self.create_button_with_label("Play Notes", "Photos\MusicNote.jpg", self.app.show_note_keyboard_screen, 180, 400)

    def create_button_with_label(self, text, image_path, command, x_position ,y_position):
        
        button_image = Image.open(image_path)
        button_image = button_image.resize((250, 250), Image.LANCZOS)
        button_photo = ImageTk.PhotoImage(button_image)
        
        button = tk.Button(self, image=button_photo, command=command, width=250, height=250, bd=0, highlightthickness=0)
        button.image = button_photo  
        button.place(x=x_position, y=y_position)
        
        label = tk.Label(self, text=text, font=("Helvetica", 15, "bold"), fg="purple", bg="black")
        label.place(x=x_position + 60, y=y_position + 210)

    
    def set_background(self, image_path):
        bg_image = Image.open(image_path)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        
        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def play_open_sound(self):
        pygame.mixer.music.load("Sonidos\Ambient-piano-logo-165357.mp3")
        pygame.mixer.music.play()

