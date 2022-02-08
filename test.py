import pyttsx3

engine=pyttsx3.init()

#Voice and Speech rate
assistantVoice=engine.getProperty('voices')
engine.setProperty('voice', assistantVoice[0].id)

newSpeechRate=180
engine.setProperty('rate', newSpeechRate)

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello World! My name is Jarvis.")