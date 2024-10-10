import soundfile
import speech_recognition as sr
import pyttsx3
import wave
from moviepy.editor import AudioFileClip

def convert_to_to_wav(input_file, output_file):
    try:
        # Load the WAV audio file
        clip = AudioFileClip(input_file)

        # Write the audio clip to an MP3 file
        clip.write_audiofile(output_file, codec='pcm_mulaw')

        print(f"Conversion successful! MP3 file saved as: {output_file}")

    except Exception as e:
        print(f"Error: {e}")


def test():
    r = sr.Recognizer()

    from pydub import AudioSegment

    m4a_file = 'uploads/audio.wav'  # I have downloaded sample audio from this link https://getsamplefiles.com/sample-audio-files/m4a
    wav_filename = 'output.wav'

    sound = AudioSegment.from_file(m4a_file, format='m4a')
    file_handle = sound.export(wav_filename, format='wav')

    #convert_to_to_wav(input_file, output_file)


    with sr.AudioFile(wav_filename) as source:
        audio = r.record(source)
    response = r.recognize_google(audio)

    print(response)

if __name__ == "__main__":
    test()