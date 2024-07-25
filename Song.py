class Song:
    def __init__(self, file_path):
        self.file_path = file_path
        self.name = self.extract_name(file_path)
        # Otras propiedades como duración, etc.
    
    def extract_name(self, file_path):
        # Lógica para extraer el nombre del archivo
        pass