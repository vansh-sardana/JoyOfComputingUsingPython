import speech_recognition as sr

AUDIO_FILE = "harvard.wav"
r= sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio= r.record(source)

try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google could not understand the audio")
except sr.RequestError:
    print("Could not get results")