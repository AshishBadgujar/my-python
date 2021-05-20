import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from random import choice

# webbrowser = webbrowser.Chrome('Chrome')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

# print(voices)
# print(voices[0].id)
# print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def jarvis(text):
    print(text)
    speak(text)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        jarvis("Good Morning!")
    elif hour >= 12 and hour < 18:
        jarvis("Good Afternoon!")
    else:
        jarvis("Good Evevning!")
    jarvis("I am jarvis sir ! How may i help you ?")


def takeCommand():
    # it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")
    except Exception as e:
        print(e)
        jarvis("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("ashishbadgujar124@gmail.com", "Ashish@124")
    server.sendmail("ashishbadgujar124@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            jarvis("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            jarvis("According to wikipedia")
            jarvis(results)

        elif"open youtube" in query:
            jarvis("oppening youtube...")
            webbrowser.open("youtube.com")

        elif"open google" in query:
            jarvis("oppening google...")
            webbrowser.open("google.com")

        elif"open stackoverflow" in query:
            jarvis("oppening stackoverflow...")
            webbrowser.open("stackoverflow.com")

        elif"play music" or "play songs" in query:
            music_dir = 'C:\\Users\\badgu\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif"the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif "open code" in query:
            jarvis("oppening code...")
            codePath = "C:\\Users\\badgu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif"send email to ashish" in query:
            try:
                jarvis("What should I say?")
                content = takeCommand()
                to = "badgujarash12@gmail.com"
                sendEmail(to, content)
                jarvis("Email has been sent !")
            except Exception as e:
                print(e)
                jarvis("Sorry,I am not able to send this email !")

        elif "play games" in query:
            jarvis("I can play stone paper scissor,would you like to play ?")
            while True:
                content = takeCommand()
                if "yes" in content:
                    jarvis("let's start !")
                    jarvis("one...")
                    jarvis("two...")
                    jarvis("three...")
                    array = ["stone", "paper", "scissor"]
                    jarvis(choice(array))
                    jarvis("want to play again ?")
                    continue
                if "no" in content:
                    jarvis("okay")
                    break

        elif "quit" in query:
            jarvis("quitting sir, have a nice day !")
            exit()
