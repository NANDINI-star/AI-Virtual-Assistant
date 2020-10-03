import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from selenium import webdriver
import time
<<<<<<< HEAD
import webbrowser as wb
import psutil
import pyjokes
import pyautogui
import os
import wolframalpha
import json
import requests
from urllib.request import urlopen
=======
>>>>>>> parent of 90944df... Merge branch 'master' of https://github.com/NANDINI-star/AI-Virtual-Assistant

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class GUicloudbot:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.base_url = "https://gu.icloudems.com/corecampus/student/attendance"

    def login(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get("https://gu.icloudems.com/corecampus/index.php")
        self.driver.find_element_by_name('userid').send_keys(self.username)
        self.driver.find_element_by_name('pass_word').send_keys(self.password)
        
        self.driver.find_element_by_xpath("//button[contains(text(), 'LOGIN')]").click()

    def attendance(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/myattendance.php')]").click()
        
        self.driver.find_element_by_xpath('//*[@id="select2-users-rc-results"]').click()
                                            
        self.driver.find_element_by_xpath('//*[@id="select2-users-rc-result-zvgd-9"]').click()
        # self.driver.find_element_by_xpath("//b[contains(text(), 'September 2020-2021')]").click()


# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour< 12:
#         speak("Good morning!")
#     elif hour >= 12 and hour <18:
#         speak("Good afternoon")
#     else:
#         speak("Good evening")

<<<<<<< HEAD
#     speak("How can I help you")

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
=======
    speak("How can I help you")
>>>>>>> parent of 90944df... Merge branch 'master' of https://github.com/NANDINI-star/AI-Virtual-Assistant

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

<<<<<<< HEAD
def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is")
    speak(Time)
def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak('the current date is')
    speak(date)
    speak(month)
    speak(year)


def wishMe():
    
    time_()
    date_()

    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("good morning mam!")
    elif hour >=12 and hour<18:
        speak(" good afteroon mam!")
    elif hour >=18 and hour<20:
        speak("good evening mam!")
    elif hour>=20 and hour<24:
        speak("mam its time to go to sleep. you may go to sleep")
    else:
        speak("mam its very late you should sleep.")

    speak("How can I help you?")

=======
>>>>>>> parent of 90944df... Merge branch 'master' of https://github.com/NANDINI-star/AI-Virtual-Assistant
def takeCommand():
    #It takes microscope input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
<<<<<<< HEAD
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print("mam i cant get it, please say it again")
        return "None"
    return query
=======
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query    
>>>>>>> parent of 90944df... Merge branch 'master' of https://github.com/NANDINI-star/AI-Virtual-Assistant

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
<<<<<<< HEAD
    server.login('username@gmail.com','password')
    server.sendmail('sender_mail',to,content)
    server.close()

def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery=psutil.sensors_battery()
    speak('battery is')
    speak(battery.percent +'charged')

def joke():
    speak(py.jokes.get_joke())

def screenshot():
    img=pyautogui.screenshot()
    img.save('C:/Users/Public/Pictures/screenshotAI.png')
=======
    server.login('youremailid', 'password')
    server.sendmail('youremailid',to, content)
    server.close()
>>>>>>> parent of 90944df... Merge branch 'master' of https://github.com/NANDINI-star/AI-Virtual-Assistant

    

if __name__ == "__main__":
    bot = GUicloudbot('18SCSE1180008','GU@12345')
    wishMe()
    while True:
    # if 1:
        query = takeCommand()
        #logic for executing tasks based on query
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
            speak("opening University icloud")
            bot.login()
            speak("What would you like to know")
            command = takeCommand()
            if 'open attendance' in command:
                try:
                    speak("opening attendance")
                    bot.attendance()

                    # speak("would you like to see today's attendance")
                    

                except Exception as e:
                    print(e)
                    speak("Sorry I'm unable to open attendance")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")

        elif 'open code' in query:
            codePath ="C:\\Users\\varun\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak("What should I say")
                content  = takeCommand()
                to = "youremailid"
                sendEmail(to,content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry my friend nandini. I am not able to send this email")