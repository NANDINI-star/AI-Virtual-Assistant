import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
from selenium import webdriver
import time
import webbrowser as wb
import psutil
import pyjokes
import pyautogui
import os
import wolframalpha
import json
import requests
from urllib.request import urlopen


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

#     speak("How can I help you")

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print("mam i cant get it, please say it again")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
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
                speak(content)
                speak('email is sent to')
            except Exception as e:
                print(e)
                speak("mail cant be send")
        elif 'open website' in query:
            speak('which website to open?')
            chromepath = 'c:/Program files (x86)/Google/Application/chrome.exe %s'
            search=takeCommand()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search youtube' in query:
            speak("what do you want to play on youtube?")
            search_Term=takeCommand()
            speak("this is youtube related")
            wb.open('http://www.youtube.com/result?search_query='+search_Term)

        elif 'cpu'in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go to sleep' in query:
            speak('have a good day sir. BYe sir')
            quit()

        elif 'Word' in query:
            speak('opening MS word...')
            ms_word= r'C:\Program Files (x86)\Microsoft Office\Office12\WINWORD'
            os.startfile(ms_word)

        elif 'Powerpoint' or 'ppt' in query:
            speak('opening MS powerpoint presentation ...')
            ms_ppt= r'C:\Program Files (x86)\Microsoft Office\Office12\POWERPNT'
            os.startfile(ms_ppt)

        elif 'Excel' in query:
            speak('opening MS excel...')
            ms_excel= r'C:\Program Files (x86)\Microsoft Office\Office12\EXCEL'
            os.startfile(ms_excel)

        elif 'Write a note' in search_query:
            speak('what should i write, sir?')
            notes =takeCommand()
            file =open('notes.txt','w')#create your own file in your system where you save this file
            speak('Sir should i include Date and Time? ')
            ans=takeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime=datetime.datetime.now().strftime('%H:%M:%S')
                file.write(strTime)
                file.write(":-")
                file.write(notes)
                speak('done taking notes sir.')
            else:
                file.write(notes)
        elif 'Show notes' in query:
            speak('showing notes')
            file=open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'Screenshot' in query:
            screenshot()

        #elif 'Play music' in query:

        elif 'what is' in query or 'who is' in query:
            client=wolframalpha.Client('8EW922-36E8QQYRJT')
            res = client.query(query)

            try:
                print(next(res.result).text)
                speak(next(res.result).text)
            except:
                print("not found")
        elif 'Make a reminder' in query:
            speak("what should i remind you , sir!")
            memory=takeCommand()
            speak("i made reminder"+memory)
            reminder=open('memory.txt','w')
            reminder.write(memory)
            reminder.close()

        #setting a reminder
        elif 'News' in query:
            try:
                jsonObj=urlopen("http://newsapi.org/v2/top-headlines?country=india&category=entertainment&apiKey=32c7d7ec660744669c2719430e560f8f")
                i=1
                speak('here are some top hadline from the entertainmemnt industry')
                print('***************TOP HEADLINE***************'+'\n')
                for item in data['article']:
                    print(str(i)+'.'+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i+=1

            except Exception as e:
                    print(str(e))
