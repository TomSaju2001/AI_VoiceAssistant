import pyttsx3
import datetime
engine=pyttsx3.init()

#Voice and Speech rate
assistantVoice=engine.getProperty('voices')
engine.setProperty('voice', assistantVoice[0].id)

newSpeechRate=180
engine.setProperty('rate', newSpeechRate)

#Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Time function
def time():
    currentTime=datetime.datetime.now().strftime("%I:%M %p")
    speak(currentTime)

time()