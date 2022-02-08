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
    now=datetime.datetime.now()
    speak("current time is")
    currentTime=now.strftime("%I:%M %p")
    speak(currentTime)

#Date function
def date():
    now=datetime.datetime.now()
    speak("Today's Date is")
    speak(now.day)
    speak(now.strftime("%B"))
    speak(now.strftime("%Y"))
    speak(now.strftime("%A"))

#Greet Function
def greet():
    hour=datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good morning. Welcome back sir!")
    elif hour>=12 and hour<5:
        speak("Good afternoon. Welcome back sir!")
    elif hour>=5 and hour<24:
        speak("Good evening. Welcome back sir!")
    else:
        speak("Good evening. Welcome back sir!")
    
    time()
    speak("How can i help you?")

greet()