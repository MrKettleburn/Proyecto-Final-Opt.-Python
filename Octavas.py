from pydub import AudioSegment

def change_octave(sound, octaves):
    # Cambia la velocidad de reproducción del sonido
    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
    return sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate}).set_frame_rate(44100)

# Cargar archivo de sonido original
sound = AudioSegment.from_file("pianoSI.mp3")

# Generar sonido una octava más alta
sound_high = change_octave(sound, 1)
sound_high.export("piano_SI_high.mp3", format="mp3")

# Generar sonido una octava más baja
sound_low = change_octave(sound, -1)
sound_low.export("piano_SI_low.mp3", format="mp3")