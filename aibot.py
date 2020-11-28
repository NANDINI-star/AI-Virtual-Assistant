import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from selenium import webdriver
import psutil
import pyjokes
import pyautogui
from urllib.request import urlopen
import json
import requests
import wolframalpha

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
        
        # self.driver.find_element_by_xpath('//*[@id="select2-users-rc-results"]').click()
                                            
        # self.driver.find_element_by_xpath('//*[@id="select2-users-rc-result-zvgd-9"]').click()
        # self.driver.find_element_by_xpath("//b[contains(text(), 'September 2020-2021')]").click()

    def timetable(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/div/div[15]/a").click()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour< 12:
        speak("Good morning!")
    elif hour >= 12 and hour <18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("Elsa is online now. How may I help you")

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

def cpu():
   usage=str(psutil.cpu_percent())
   speak('CPU is at'+usage)
   print('CPU is at'+usage)
   battery=psutil.sensors_battery()
   speak('battery is')
   speak(battery.percent )
   print('battery is')
   print(battery.percent)

def joke():
    speak(pyjokes.get_joke())
    

# def screenshot():
#     img=pyautogui.screenshot()
#     img.save('C:/Users/Public/Pictures/screenshotAI.png')

if __name__ == "__main__":
    bot = GUicloudbot('18SCSE1180008','GU@12345')
    wishMe()
    while True:
    # if 1:
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

            elif 'time table' in command:
                try:
                    speak("opening timetable")
                    bot.timetable()

                    

                except Exception as e:
                    print(e)
                    speak("Sorry I'm unable to open timetable")

            else:
                speak('I dont understand you')

        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")

        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)

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
                speak("Sorry my friend palak. I am not able to send this email")

        # elif 'search in chrome' in query:
        #     speak("what should i search?")
        #     chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' #Add the Location of the chrome browser

        #     r = sr.Recognizer()

        #     with sr.Microphone() as source:
        #         print('say something!')
        #         print('Listening...')
        #         audio = r.listen(source)
        #         print("done")
        #     try:
        #         text = r.recognize_google(audio)
        #         print('google think you said:\n' +text)
        #         webbrowser.get(chrome_path).open(text)
        #     except Exception as e:
        #         print(e)

        elif 'cpu'in query:
           cpu()

        elif 'joke' in query:
            joke()

        # elif 'Screenshot' in query:
        #     speak("Taking a screenshot now")
        #     screenshot()

        elif 'where is ' in query:
            query=query.replace('where is','')
            location=query
            speak("on map "+location+'is here')
            driver = webdriver.Chrome('./chromedriver.exe')
            driver.get("https://www.google.com/maps/place/"+location)
            driver.find_element_by_xpath("//button[@id='searchbox-searchbutton']").click()

            # webbrowser.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'news' in query:
            try:
                jsonObj=urlopen("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=32c7d7ec660744669c2719430e560f8f")
                data=json.load(jsonObj)
                i=1
                speak('here are some top hadline from the business industry')
                print('***************TOP HEADLINE***************'+'\n')
                for item in data['articles']:
                    print(str(i)+'.'+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i+=1

            except Exception as e:
                    print(str(e))

        # elif 'what is' in query or 'who is' in query:
        #     client=wolframalpha.Client('8EW922-36E8QQYRJT')
        #     res = client.query(query)

        #     try:
        #         print(next(res.result).text)
        #         speak(next(res.result).text)
        #     except:
        #         print("not found")

        elif 'university programs' in query:
           speak("There are total 6 types of programs offered by galgotias university. The programs offered by GU are under graduate programs, post graduate programs, diploma programs, certificate programs, integrated programs, doctoral programs , which program do you want to know about?")
           program=takeCommand()
           if 'under graduate programs' in program:
               speak("In this program we have all the bachelors degree courses available in different schools. we have school of Electrical Electronics and communication engineering, school of Computing Science & Engineering, School of Civil Engineering, School of Mechanical Engineering, School of Biosciences and Biomedical Engineering, School of Architecture & Design, School of Business, School of Finance & Commerce, School of Liberal Education, School of Basic & Applied Sciences,School of Medical & Allied Sciences, School of Nursing,School of Hospitality & Tourism, School of Media & Communication Studies, School of Education, School of Agriculture, School of Law  ")
           elif 'Post Graduate Programs' in program:
               speak("In this program we have all the masters degree courses available in different schools. we have school of Computing Science & Engineering, School of Electrical, Electronics & Communication Engineering, School of Civil Engineering, School of Mechanical Engineering, School of Biosciences and Biomedical Engineering, School of Architecture & Design, School of Business,School of Finance & Commerce,School of Liberal Education, School of Basic & Applied Sciences, School of Law, School of Medical & Allied Sciences, School of Hospitality & Tourism, School of Media & Communication Studies, School of Education, School of Agriculture")    
           elif 'diploma programs' in program:
               speak("we have multiple diploma courses available in feilds of University Polytechnic,School of Business, School of Hospitality & Tourism, School of Medical and Allied Sciences and in School of Ayurveda Science.")    
           elif 'certificate programs' in program:
               speak("certificate program includes certificte degree in courses available under School of Hospitality & Tourism only")
           elif 'integrated programs' in program:
               speak("So, School of Computing Science & Engineering offers integrated BCA + MCA, School of Law offers Five year Integrated B.A LL.B.(Hons.) and Five year Integrated B.B.A LL.B.(Hons.) , School of Business offers Integrated MBA (BBA+MBA)")
           elif 'Doctoral Programs' in program:
               speak("doctoral courses are available by School of Electrical, Electronics & Communication Engineering, School of Computing Science & Engineering, School of Civil Engineering, School of Mechanical Engineering, School of Business, School of Biosciences and Biomedical Engineering, School of Liberal Education, School of Basic & Applied Sciences, School of Law, School of Medical & Allied Sciences, School of Media & Communication Studies, School of Education ")    
           else:
               print("not found")


        elif 'clubs and societies' in query:
           speak("At Galgotias University, students are encouraged to become a member of different clubs and committees. With over 40 different clubs, Galgotias University connects students to a platform where they can exchange knowledge, build awareness, and receive recognition. the Vision is to Promote fellowship, share India’s rich cultural diversity and promote brotherhood and the Mission is to Inform, inspire and connect students on a platform where they can exchange knowledge, build awareness, generate interest and receive recognition.The society list includes mainly Cultural Society, Sports Society, Technical Society, Management Society, Literary Society and Story Society. which society do you want to know about") 
           society = takeCommand()
           if 'Cultural society' in society:
               speak("The clubs in cultural society are Galgotias Studio D - The Dance Club Galgotias Note Veda - The Music club Galgotias The Actor's Hub-Dramatics Club Galgotias Scintillations - The Fashion Club Galgotias Spic Macay Club Galgotias The Fine arts club Galgotias CamCircle - The Photography Club")
           elif 'sports society' in society:
               speak("the club in sports society are Galgotias Sports Society")    
           elif 'technical society' in society:
               speak("the clubs in technical society are Galgotias Gaming Club - F.R.A.G. Galgotias The Creative club Galgotias Quizita Mavens - Quiz Club Galgotias Mechelites: Motorsports Club")    
           elif 'management society' in society:
               speak("the club in management society are Galgotias GU Management Club ")    
           elif 'literary society' in society:
               speak("the clubs are Lingo Freaks - The Literary club Galgotias Youth Parliament-NIRMAAN")   
           elif 'story society' in society:
               speak("the clubs are Galgotias Humans Of Galgotias - Every Story Matters galgotias APES Club Galgotias Grace Club")  
           else:
               print("couldn't get that input, try again")           
        
        
        elif 'student council' in query:
            speak("galgotias univerity student council comparises of the core members from senior year who take responsibilities of every happening in and out side of the campus.")    


        elif 'go offline' in query:
            speak("ok mam shutting down the system")
            quit()