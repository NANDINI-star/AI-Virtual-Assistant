import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import wolframalpha
import json
import requests
from urllib.request import urlopen


engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("the currnt time is")
    speak(Time)
def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak('the current date is')
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("hello sir. welcome back !")
    time_()
    date_()

    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("good morning sir!")
    elif hour >=12 and hour<18:
        speak(" good afteroon sir!")
    elif hour >=18 and hour<20:
        speak("good evening sir!")
    elif hour>=20 and hour<24:
        speak("sir its time to go to sleep. you may go to sleep")
    else:
        speak("sir its very late you should sleep.")

    speak(". what we will be doing now sir!")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Sir i cant get it, please say it again")
        return
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


    wishme()

    while True:
        query=takeCommand()
        if 'time ' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak('Searching.....')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=5)
            speak('According to wikipedia, ')
            print(result)
            speak(result)
        elif 'send Email' in query:
            try:
                speak("what should i write ?")
                content=takeCommand()
                speak("please enter the recivers email_id")
                reciver=input('enter email id:')
                to=reciver
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
