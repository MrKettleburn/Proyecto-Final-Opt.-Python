class MusicPlayer:
    def __init__(self):
        self.current_song = None
    
    def load_song(self, file_path):
        self.current_song = Song(file_path)
        # Cargar el archivo de música usando una biblioteca como pygame o pydub
    
    def play(self):
        # Lógica para reproducir la canción
        pass
    
    def pause(self):
        # Lógica para pausar la canción
        pass
    
    def stop(self):
        # Lógica para detener la canción
        pass