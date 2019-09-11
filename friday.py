import os
import sys
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib

#using microsoft speech api
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")

    speak("Hey i am friday, what can i do for you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    print(query)
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('2017308@iiitdmj.ac.in','Raftaar@123')
    server.sendmail('2017308@iiitdmj.ac.in',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        #logic for exceuting tasks based on query
        if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Sir...")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Sir...")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening Sir...")

        elif 'play music' in query:
            music_dir = 'D:\\gannaPur\\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'email to ambuj' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "jainambuj8@gmail.com@gamil.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("sorry for truble at the moment, you can try again")
        
        elif 'quit' in query:
            exit()
