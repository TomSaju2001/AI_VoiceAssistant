import pyttsx3

engine=pyttsx3.init()

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Tom Saju")