import pyttsx3, subprocess
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('API_CLIENT')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning! Yudi!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon! Yudi!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening! Yudi!')

greetMe()

speak('Hello Yudi! I am AUDI, I am a digital assistant !. Nice to meet you! Yudi')
speak('What can I do for you?')

class BotKu:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Firefox()

    def Masuk(self):
        bot_yudi = self.driver
        bot_yudi.get('http://akademik.unsera.ac.id/')

        user = bot_yudi.find_element_by_name('user')
        user.send_keys(self.username)

        time.sleep(3)

        pasS = bot_yudi.find_element_by_name('password')
        pasS.send_keys(self.password)

        time.sleep(2.5)
        pasS.send_keys(Keys.RETURN)


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ready to take orders ...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('Yudi: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry, Yudi! I do not understand! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.id')

        elif 'open word' in query:
            speak('okay')
            subprocess.call(r'C:\Program Files (x86)\Microsoft Office\Office12\WINWORD.EXE')

        elif 'open job' in query:
            speak('okay')
            speak('I will open the work!')
            subprocess.call(r'C:\Users\Yudi Faturohman\AppData\Local\atom\atom.exe')
            speak('Atom is open!')
            subprocess.call(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
            speak('Firefox is open!')

        elif 'open bot' in query:
            speak('okay')
            speak('open BOT!')
            bot1 = BotKu('user', 'password')
            bot1.Masuk()

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Thank you! I hope you will be given convenience! in carrying out activities !.')
            speak('Bye!')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Thank you! I hope you will be given convenience! in carrying out activities !.')
            speak('Bye!')
            sys.exit()

        elif 'musik' in query:
            music_folder = 'D:\\musik\\'
            music = ['H', 'S', 'U']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            speak('Okay, here is your music! Enjoy!')


        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak('WOLFRAM-ALPHA says - ')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                speak('umm')
                speak('Sorry!. Maybe Google is smarter than me')
                webbrowser.open('www.google.com')

        speak('There are more?')
