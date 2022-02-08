from multiprocessing.connection import Listener
import pyttsx3
import datetime
import speech_recognition as sr

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
    
    speak("How can i help you?")

#Function to take command from user
def takeCommand():
    listener=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.pause_threshold=1
        audio=listener.listen(source)

    try:
        print("Recognizing..")
        query = listener.recognize_google(audio, language='en-US')
        print(query)
    except Exception as error:
        print(error)
        speak("Say it again...")
        return "None"

    return query

if __name__ == "__main__":

    greet()

    while True:
        query=takeCommand().lower()
        #print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "power off" in query:
            quit()