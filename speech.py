import speech_recognition as sr
import text

def speech():
    r = sr.Recognizer()

    from pydub import AudioSegment

    m4a_file = 'uploads/audio.wav'
    wav_filename = 'output.wav'

    sound = AudioSegment.from_file(m4a_file, format='m4a')
    file_handle = sound.export(wav_filename, format='wav')

    with sr.AudioFile(wav_filename) as source:
        audio = r.record(source)
    response = r.recognize_google(audio)

    print(response)
    return text.run(response)
