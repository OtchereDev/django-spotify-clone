from mutagen.mp3 import MP3

def get_audio_length(file):
    audio = MP3(file)
    return audio.info.length
    