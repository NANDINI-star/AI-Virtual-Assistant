import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour< 12:
        speak("Good morning!")
    elif hour >= 12 and hour <18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Jarvis Mam, Please tell me how may I help you")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microscope input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremailid', 'password')
    server.sendmail('youremailid',to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        #logic for executing taska based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open icloud' in query:
            webbrowser.open("https://gu.icloudems.com/corecampus/index.php")
            speak("Login to your icloud account to proceed")
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")

        elif 'open code' in query:
            codePath ="C:\\Users\\varun\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak("What shoul I say")
                content  = takeCommand()
                to = "youremailid"
                sendEmail(to,content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry my friend nandini. I am not able to send this email")