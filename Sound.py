
import pygame

pygame.init()
pygame.mixer.init()

# Diccionario de sonidos
sounds = {
    'a': pygame.mixer.Sound("Sonidos\pianoDO.mp3"),
    's': pygame.mixer.Sound("Sonidos\pianoRE.mp3"),
    'd': pygame.mixer.Sound("Sonidos\pianoMI.mp3"),
    'f': pygame.mixer.Sound("Sonidos\pianoFA.mp3"),
    'g': pygame.mixer.Sound("Sonidos\pianoSOL.mp3"),
    'h': pygame.mixer.Sound("Sonidos\pianoLA.mp3"),
    'j': pygame.mixer.Sound("Sonidos\pianoSI.mp3"),

    'q': pygame.mixer.Sound("Sonidos\piano_DO_high.mp3"),
    'w': pygame.mixer.Sound("Sonidos\piano_RE_high.mp3"),
    'e': pygame.mixer.Sound("Sonidos\piano_MI_high.mp3"),
    'r': pygame.mixer.Sound("Sonidos\piano_FA_high.mp3"),
    't': pygame.mixer.Sound("Sonidos\piano_SOL_high.mp3"),
    'y': pygame.mixer.Sound("Sonidos\piano_LA_high.mp3"),
    'u': pygame.mixer.Sound("Sonidos\piano_SI_high.mp3"),

    'z': pygame.mixer.Sound("Sonidos\piano_DO_low.mp3"),
    'x': pygame.mixer.Sound("Sonidos\piano_RE_low.mp3"),
    'c': pygame.mixer.Sound("Sonidos\piano_MI_low.mp3"),
    'v': pygame.mixer.Sound("Sonidos\piano_FA_low.mp3"),
    'b': pygame.mixer.Sound("Sonidos\piano_SOL_low.mp3"),
    'n': pygame.mixer.Sound("Sonidos\piano_LA_low.mp3"),
    'm': pygame.mixer.Sound("Sonidos\piano_SI_low.mp3"),
}

# Función para reproducir sonido
def play_sound(key):
    if key in sounds:
        sounds[key].play()

def play_initial_sound():
    pygame.mixer.Sound("Sonidos\piano_SI_low.mp3").play()

# Salir de Pygame al cerrar la interfaz
pygame.quit()