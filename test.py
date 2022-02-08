from multiprocessing.connection import Listener
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb

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

#wikipedia function
def wikipediaSearch(query):
    speak("Searching...")
    query=query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=3)
    speak(result)

#mail function
def sendMail(reciever,message):
    portNumber=587
    mailId="yourmail.gmail.com"
    password="yourPassword"
    recieverMailID="reciever@gmail.com"
    server=smtplib.SMTP('smtp.gmail.com', portNumber)
    server.echo()
    server.starttls()
    server.login(mailId, password)
    server.sendmail(mailId, recieverMailID, message)
    server.close()


#email main function
def callSendMail():
    try:
        speak("What is the message?")
        message=takeCommand()
        reciever=takeCommand()
        sendMail(reciever, message)
    except Exception as error:
        speak(error)
        speak("Unable to send the message. please contact the developer.!")

#main function
if __name__ == "__main__":
    greet()

    while True:
        query=takeCommand().lower()
        #print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            wikipediaSearch(query)
        elif "send email" in query:
            callSendMail()
        elif "chrome browser" in query:
            speak("What should i search for?")
            chromePath="C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search=takeCommand().lower()
            wb.get(chromePath).open_new(search + ".com")
        elif "power off" in query:
            quit()