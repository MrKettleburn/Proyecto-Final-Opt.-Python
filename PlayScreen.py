import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import pygame
import os

class PlayScreen(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.pack(expand=True, fill='both')
        self.song_list = []
        self.current_song_index = None
        self.is_paused = False
        self.create_widgets()
        self.load_songs()
    
    def create_widgets(self):
        self.master.geometry("640x704")
        
        self.set_background("Photos/FondoMusicApp.jpg")
        
        self.create_song_list()
        
        self.create_button("Photos/Play.jpg", self.play_pause_song, 310, 590, 100, 100)
        self.create_button("Photos/Pause.jpg", self.pause_song, 420, 590, 100, 100)
        self.create_button("Photos/Previous.jpg", self.play_previous_song, 220, 600, 80,80)
        self.create_button("Photos/Next.jpg", self.play_next_song, 530, 600,80,80)
        
        self.create_button("Photos/Add.jpg", self.select_song, 120, 0, 50, 50)

        self.create_button("Photos/Back.jpg", self.app.show_main_screen, 0, 0, 50, 50)

        label_image = Image.open("Photos/MusicNote.jpg")
        label_image = label_image.resize((400, 400), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        center_label = tk.Label(self, image=label_photo, bg="black")
        center_label.image = label_photo 
        center_label.place(x=200, y=100)

        self.song_name_label = tk.Label(self, text="", font=("Helvetica", 10, "bold"), fg="white", bg="black")
        self.song_name_label.place( x=210, y=470)



    def create_button(self, image_path, command, x_position, y_position, x_photo_size, y_photo_size):
        
        button_image = Image.open(image_path)
        button_image = button_image.resize((x_photo_size, y_photo_size), Image.LANCZOS)
        button_photo = ImageTk.PhotoImage(button_image)
        
        button = tk.Button(self, image=button_photo, command=command, width=x_photo_size, height=y_photo_size, bd=0, highlightthickness=0)
        button.image = button_photo  
        button.place(x=x_position, y=y_position)
    
    def set_background(self, image_path):
       
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((640, 704), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        
        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.lower()
    
    def create_song_list(self):
        list_frame = tk.Frame(self, bg="")
        list_frame.place(x=0, y=50, width=170, height=654)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.song_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, bg="black", font=("Helvetica", 12), fg="white")
        self.song_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.song_listbox.bind('<Double-1>', self.play_selected_song)
        scrollbar.config(command=self.song_listbox.yview)
    
    
    def create_file_select_button(self):
        select_button = tk.Button(self, text="Select Song", command=self.select_song, width=20)
        select_button.place(x=600, y=50)
    
    def load_songs(self):
        music_dir = "music/"
        if not os.path.exists(music_dir):
            os.makedirs(music_dir)
        
        for file in os.listdir(music_dir):
            if file.endswith(".mp3"):
                self.song_list.append(os.path.join(music_dir, file))
                self.song_listbox.insert(tk.END, file)
    
    def play_selected_song(self, event):
        selection = event.widget.curselection()
        if selection:
            self.current_song_index = selection[0]
            self.play_song(self.song_list[self.current_song_index])
    
    def play_song(self, song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        self.is_paused = False
        self.update_song_name_label(song_path)

    def update_song_name_label(self, song_path):
        self.song_name_label.config(text=song_path)
    
    def play_pause_song(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            pygame.mixer.music.pause()
            self.is_paused = True
    
    def pause_song(self):
        pygame.mixer.music.pause()
        self.is_paused = True
    
    def play_previous_song(self):
        if self.current_song_index is not None:
            self.current_song_index = (self.current_song_index - 1) % len(self.song_list)
            self.play_song(self.song_list[self.current_song_index])
    
    def play_next_song(self):
        if self.current_song_index is not None:
            self.current_song_index = (self.current_song_index + 1) % len(self.song_list)
            self.play_song(self.song_list[self.current_song_index])
    
    def select_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.song_list.append(file_path)
            self.song_listbox.insert(tk.END, os.path.basename(file_path))