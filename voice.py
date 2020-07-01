import calendar
import datetime
import os
import random
import smtplib
import warnings
import webbrowser
from time import sleep

import pyaudio
import pyttsx3
import speech_recognition as sr
import wikipedia
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',160)
engine.setProperty('volume',1)

master = "Ashok.."
input_greet = ['hi', 'hello', 'wassup', 'hey', 'hey there', 'dude', 'bro']
response_greet = ['hey, how are you?', 'hi bro', 'hello, how is the day?',
                  'howdy', 'wassup dude', 'hey dude, how is going on?', 'hey there, how are you?']
friend = {"Ashok Nick": "ashoknicky561@gmail.com", "Ashok": "ashokshesha1998@gmail.com", "Anusha": "anushavanu670@gmail.com", "Jo": "niranjanjo1997@gmail.com", "Shekar": "shekar00528@gmail.com", "Arun": "aviji533@gmail.com",
          "Arun Sir": "arunkumardr1987@gmail.com", "Nanditha": "nanditha_pokuri@yahoo.com", "Raghul": "raghultkp1998@gmail.com", "Keerthan": "keer.busy@gmail.com", "Meghan": "megbhujang@gmail.com", "Mithun": "mithunrgowda3@gmail.com"}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Initializing system")
    speak("I\'m Maha")
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    if hour >= 0 and hour < 12:
        speak("Good Morning "+master+f" the time is {strTime}")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon "+master+f" the time is {strTime}")

    else:
        speak("Good Evening "+master+f" the time is {strTime}")

    speak("Please tell me how may I help you")





def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        #r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None "
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aifriend561@gmail.com', 'maha561@')
    server.sendmail('aifriend561@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'what\'s your name' in query:
            speak("I am Maha sir!")

        elif 'created you' in query:
            speak("His name is Ashok..")

        elif 'named you' in query:
            speak("His name is Ashok..")

        elif query in input_greet:
            speak(random.choice(response_greet)+'.')

        elif 'open youtube' in query:
            chromedriver = "C:/Users/ashok/Desktop/coding practice/AI_Friend/chromedriver/chromedriver"
            driver = webdriver.Chrome(chromedriver)
            driver.get("https:youtube.com")

        elif 'close youtube' in query:
            driver.close()

        elif 'open stackoverflow' in query:
            chromedriver = "C:/Users/ashok/Desktop/coding practice/AI_Friend/chromedriver/chromedriver"
            driver = webdriver.Chrome(chromedriver)
            driver.get("https:stackoverflow.com")

        elif 'close stackoverflow' in query:
            driver.close()

        elif 'open google' in query:
            chromedriver = "C:/Users/ashok/Desktop/coding practice/AI_Friend/chromedriver/chromedriver"
            driver = webdriver.Chrome(chromedriver)
            driver.get("https:google.com")

        elif 'close google' in query:
            driver.close()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send mail' in query:
            try:
                speak("To whom i should send mail sir?")
                ToFriend = takeCommand()
                if ToFriend in friend:
                    speak("what should I say sir?")
                    content = takeCommand()
                    to = friend[ToFriend]
                    sendEmail(to, content)
                    speak("Email has been sent successfull sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir, i am not able to send this mail")

        # elif 'exit' in query:
         #   quit()
