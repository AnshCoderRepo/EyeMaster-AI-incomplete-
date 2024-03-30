# for audio to text conversion and vice vers
import pyttsx3
#decouple helps you to organize your settings so that you can change parameters without having to redeploy your app. It also makes it easy for you to: store parameters in ini or.env files; define comprehensive default values; properly convert values to the correct data type;
from decouple import config
# for date time .
from  datetime import datetime

from conv import  random_text

# to recoginize speech from both side
import speech_recognition as sr
from random import choice

engine=pyttsx3.init('sapi5')
engine.setProperty('volume',1)
# to set Volume of your virtual assitant
engine.setProperty('rate',205)
# to set speaking rate limit of your virtual assistant
voices=engine.getProperty('voices')
# to set voice of your vitual assiatnt
engine.setProperty('voice',voices[1].id)# 1 -> to set jarvis voice to female voice 0 -> for male audio

# for speaking of text by the virtual assistanat
USER = config('USER')# pip install python-decouple->
HOSTNAME = config('BOT')
def speak (text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour=datetime.now().hour
    if(hour>=6) and (hour<12):
        speak(f"Good moring {USER}")
    elif(hour>=12) and(hour<=16):
        speak(f"Good Afer noon {USER}")
    elif(hour>=16) and (hour<19):
        speak(f"Good Evening{USER}")
    speak(f" i am {HOSTNAME}. how  may i assiatnt you? ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print('Recoginizing....')
        queri=r.recognize_google_cloud(audio,language='en-in')
        print(queri)
        if not 'stop' in queri or 'exit ' in queri:
            speak(choice(random_text))
        else:
            hour=datetime.now().hour
            if hour>=21 and hour<6:
                speak("Good night sir, sleep well")
            else:
                speak("Have a good dat")
            exit()
    except Exception:
        speak("Sorry i count understand what you said , Can you plaese repeat it again,")
        speak("Thank you")
        queri='None'
    return queri
if __name__ == '__main__':
    speak('Hi, I am your virtual assistant')
    print('Hi , I am your Virtual Assistant')
    greet_me()
    while True:
        query=takeCommand().lower()
        if "how are you " in query:
            speak("I am fine. How about you")
# resume from 18:40 min in the video

