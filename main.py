# for audio to text conversion and vice vers
import os
import subprocess as sp
# for date time .
from datetime import datetime
from random import choice

import keyboard
import pyttsx3
# to recognize speech from both side
import speech_recognition as sr
# decouple helps you to organize your settings so that you can change parameters without having to redeploy your app.
# It also makes it easy for you to: store parameters in ini or.env files; define comprehensive default values;
# properly convert values to the correct data type;
from decouple import config

from config import find_my_ip
from config import search_on_google
from config import search_on_wikipedia
from config import send_mail
from config import youtube
from conv import random_text

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1)
# to set Volume of your virtual assistant
engine.setProperty('rate', 205)
# to set speaking rate limit of your virtual assistant
voices: object = engine.getProperty('voices')
# to set voice of your virtual assistant
engine.setProperty('voice', voices[0].id)  # 1 -> to set jarvis voice to female voice 0 -> for male audio

# for speaking of text by the virtual assistant
USER = config('USER')  # pip install python-decouple->
HOSTNAME = config('BOT')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good Afternoon {USER}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening{USER}")
    speak(f" i am {HOSTNAME}. how  may i help you? ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing....')
        queri = r.recognize_google(audio, language='en-in')
        print(queri)
        if not 'stop' in queri or 'bye' in queri:
            speak(choice(random_text))
        else:
            hour = datetime.now().hour
            if hour < 21:
                speak("bye")
            else:
                speak("Good night sir, sleep well")
            exit()

    except Exception:
        speak("Sorry i count understand what you said , Can you please repeat it again,")
        speak("Thank you")
        queri = 'None'
    return queri


listening = False


def start_Listening():
    global listening
    listening = True
    print("Start Listening")


def pause_Listening():
    global listening
    listening = False
    print("Stopped listening")


keyboard.add_hotkey('ctrl+alt+k', start_Listening)
keyboard.add_hotkey('ctrl+alt+l', pause_Listening)

if __name__ == '__main__':
    greet_me()
    # speak('Hi, I am your virtual assistant')
    #
    # print('Hi , I am your Virtual Assistant')

    while True:
        if listening:
            query = takeCommand().lower()
            if "how are you" in query:
                speak("I am fine. How about you")
            elif "open command prompt" in query:
                speak("Opening Command Prompt")
                # command to open command prompt
                os.system('start cmd')
            elif "open camera" in query:
                speak("Opening camera")
                command = 'start microsoft.windows.camera:'
                # Command to open camera in your system
                sp.run(command, shell=True)
            elif "open notepad" in query:
                speak("Opening notepad for you sir")
                # Command to open notepad++ in your system
                notepad_path = "C:\\Program Files\\Notepad++\\notepad++.exe"
                os.startfile(notepad_path)
            elif "open Discord" in query:
                speak("Opening the discord for you")
                discord_path = "C:\\Program Files\\Discord Inc\\Discord.exe "
                os.startfile(discord_path)
            elif "open browser" in query:
                speak("Opening Browser ")
                edge_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.exe"
                os.startfile(edge_path)
            elif "ip address" in query:
                ip_address = find_my_ip()
                speak(f"Your ip address is{ip_address}")
                print(f"Your ip address is{ip_address}")
            elif "open youtube " in query:
                speak("What do you want to see on youtube sir")
                video = takeCommand().lower()
                youtube(video)
            elif "open google " in query:
                speak("What do you want to search on google")
                query = takeCommand().lower()
                search_on_google(query)
            elif "open wikipedia" in query:
                speak("What or Whom do you want to search on wikipedia")
                search = takeCommand().lower()
                results = search_on_wikipedia(search)
                speak(f"According to wikipedia,{results}")
                speak(" I am displaying it on the terminal  ")
                print(results)
            elif "send an email " in query:
                speak("On what email address you want to send the mail, Please write in th terminal")
                receiver_add = input("Email Address:")
                speak("What should be the subject sir?")
                subject = takeCommand().capitalize()
                speak("What is the message")
                message = takeCommand().capitalize()
                if send_mail(receiver_add, subject, message):
                    speak("I have send the mail sir")
                    print("I have send the mail sir")
                else:
                    speak("Error  in sending the mail")
# resume from 27:22 min in the video
            elif "give me news " in query:
                speak("I am reading out headling of today,sir")
