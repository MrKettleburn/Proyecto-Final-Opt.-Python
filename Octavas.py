from pydub import AudioSegment
import os

def change_octave(sound, octaves):
    # Cambia la velocidad de reproducción del sonido
    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
    return sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate}).set_frame_rate(44100)

# # Cargar archivo de sonido original
# for i in "Sonidos/":
#     if "cello" in i:
#         sound = AudioSegment.from_file(i)

#         # Generar sonido una octava más alta
#         sound_high = change_octave(sound, 1)
#         sound_high.export( f"{i}_high.mp3", format="mp3")

#         # Generar sonido una octava más baja
#         sound_low = change_octave(sound, -1)
#         sound_low.export( f"{i}_low.mp3", format="mp3")

sound_folder = "Sonidos/"

# Iterar sobre los archivos en la carpeta
for filename in os.listdir(sound_folder):
    if "cello" in filename:
        filepath = os.path.join(sound_folder, filename)
        sound = AudioSegment.from_file(filepath)

        # Generar sonido una octava más alta
        sound_high = change_octave(sound, 1)
        sound_high.export(os.path.join(sound_folder, f"{filename}_high.mp3"), format="mp3")

        # Generar sonido una octava más baja
        sound_low = change_octave(sound, -1)
        sound_low.export(os.path.join(sound_folder, f"{filename}_low.mp3"), format="mp3")