import tkinter as tk
from tkinter import ttk
import pygame
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Sounds import instruments
from PIL import Image, ImageTk
import wave
from pydub import AudioSegment

class NoteKeyboardScreen(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.pack(expand=True, fill='both')
        pygame.mixer.init()
        self.current_instrument = None
        self.create_widgets()
    
    def create_widgets(self):
       
        self.master.geometry("640x704")
      
        self.set_background("Photos/FondoMusicApp.jpg")
        
        instruction_label = tk.Label(self, text="Instruments: ", font=("Helvetica", 15), fg="white", bg="black")
        instruction_label.place(x=200, y=50, anchor='center')

        self.note_labels()

        self.instrument_combobox = ttk.Combobox(self, values=list(instruments.keys()), state="readonly", font=("Helvetica", 15, "bold"))
        self.instrument_combobox.bind("<<ComboboxSelected>>", self.change_instrument)
        self.instrument_combobox.place(x=370, y=50, anchor='center')
      
        instruction_label = tk.Label(self, text="Select an instrument and play notes using the keyboard", font=("Helvetica", 15, "bold"), fg="purple", bg="black")
        instruction_label.place(x=330, y=100, anchor='center')
       
        self.master.bind("<KeyPress>", self.play_note)

        self.graph_frame = tk.Frame(self, bg="black")
        self.graph_frame.place(x=2, y=150, width=700, height=300)

        button_image = Image.open("Photos/Back.jpg")
        button_image = button_image.resize((50, 50), Image.LANCZOS)
        button_photo = ImageTk.PhotoImage(button_image)
        
        button = tk.Button(self, image=button_photo, command=self.app.show_main_screen, width=50, height=50, bd=0, highlightthickness=0)
        button.image = button_photo  
        button.place(x=0, y=0)

    def note_labels(self):

        #NOTAS ALTAS

        label_image = Image.open("Photos/DO_high.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=40, y=480)

        label_image = Image.open("Photos/RE_high.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=115, y=480)

        label_image = Image.open("Photos/MI_high.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=190, y=480)

        label_image = Image.open("Photos/FA_high.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=265, y=480)

        label_image = Image.open("Photos/SOL_high.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=340, y=480)

        label_image = Image.open("Photos/LA_high.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=415, y=480)

        label_image = Image.open("Photos/SI_high.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=490, y=480)

        #NOTAS NORMAL
        
        label_image = Image.open("Photos/DO.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=50, y=555)

        label_image = Image.open("Photos/RE.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=125, y=555)

        label_image = Image.open("Photos/MI.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=200, y=555)

        label_image = Image.open("Photos/FA.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=275, y=555)

        label_image = Image.open("Photos/SOL.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=350, y=555)

        label_image = Image.open("Photos/LA.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=425, y=555)

        label_image = Image.open("Photos/SI.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=500, y=555)

        #NOTAS BAJAS
        
        label_image = Image.open("Photos/DO_low.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=60, y=630)

        label_image = Image.open("Photos/RE_low.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=135, y=630)

        label_image = Image.open("Photos/MI_low.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=210, y=630)

        label_image = Image.open("Photos/FA_low.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=285, y=630)

        label_image = Image.open("Photos/SOL_low.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=360, y=630)

        label_image = Image.open("Photos/LA_low.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=435, y=630)

        label_image = Image.open("Photos/SI_low.jpg")
        label_image = label_image.resize((65, 65), Image.LANCZOS)
        label_photo = ImageTk.PhotoImage(label_image)
        
        button_label = tk.Label(self, image=label_photo, bd=0, highlightthickness=0)
        button_label.image = label_photo  
        button_label.place(x=510, y=630)


    def set_background(self, image_path):
      
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((640, 704), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        
        
        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.lower()
    
    def change_instrument(self, event):
        selected_instrument = self.instrument_combobox.get()
        if selected_instrument in instruments:
            self.current_instrument = instruments[selected_instrument]
    
    def play_note(self, event):
        if self.current_instrument and event.char in self.current_instrument:
            sound_path = self.current_instrument[event.char]
            pygame.mixer.Sound(sound_path).play()
            self.display_waveform(sound_path)
    
    def display_waveform(self, sound_path):
    
        audio = AudioSegment.from_mp3(sound_path)
        audio = audio.set_channels(1) 
        audio = audio.set_frame_rate(44100)  
        
     
        wav_data = audio.export(format="wav")
        
     
        wav_data.seek(0)
        wf = wave.open(wav_data, 'rb')
        frames = wf.readframes(-1)
        sound_info = np.frombuffer(frames, dtype=np.int16)
        wf.close()
        plt.close()
      
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(sound_info)
        ax.set_title("Waveform")
      
        line, = ax.plot([], [], color='cyan') 

       
        fig.patch.set_facecolor('#602A91') 
        ax.patch.set_facecolor('purple') 
        ax.xaxis.label.set_color('white') 
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')  
        ax.tick_params(axis='y', colors='white') 
        ax.spines['bottom'].set_color('white') 
        ax.spines['top'].set_color('white')  
        ax.spines['left'].set_color('white')  
        ax.spines['right'].set_color('white') 

       
        ax.set_title("Waveform", color='white') 
     
        line.set_data(np.arange(len(sound_info)), sound_info)
        
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

