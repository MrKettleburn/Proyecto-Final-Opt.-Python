from pydub import AudioSegment
import os

def change_octave(sound, octaves):

    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
    return sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate}).set_frame_rate(44100)

sound_folder = "Sonidos/"


for filename in os.listdir(sound_folder):
    if "cello" in filename:
        filepath = os.path.join(sound_folder, filename)
        sound = AudioSegment.from_file(filepath)

       
        sound_high = change_octave(sound, 1)
        sound_high.export(os.path.join(sound_folder, f"{filename}_high.mp3"), format="mp3")

        sound_low = change_octave(sound, -1)
        sound_low.export(os.path.join(sound_folder, f"{filename}_low.mp3"), format="mp3")