import pyttsx3                                                #pip install pyttsx3
import datetime
import speech_recognition as sr                               #py -m pip install SpeechRecognition
import wikipedia                                              #py -m pip install wikipedia
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("Hi, This is JARVIS! Hello, Everyone!")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)

#time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)

#date()

def wishme():
    speak("Welcome back, Sir!")
    #speak("The current time is ")
    #time()
    #speak("The current date is ")
    #date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour<17:
        speak("Good Afternoon Sir!")
    elif hour >=17 and hour<20:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!") 
    speak("Jarvis at your service, Tell me How can i help you?")

#wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query

#takeCommand()

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sender_email@gmail.com','password_for_the_same')
    server.sendmail('sender_email@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = 'recipient@gmail.com'
                sendEmail(to,content)
                speak("Email has been Sent")
            except Exception as e:
                print(e)
                speak("Unable to send email")

        elif 'search in chrome' in query:
            speak("what should i search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'play songs' in query:
            songs_dir = 'C:/ABHINABA/Songs'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'offline' in query:
            quit()
