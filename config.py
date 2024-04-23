import requests
import wikipedia
import pywhatkit as kit  # to access online function like google search playyoutube
from email.message import EmailMessage
import smtplib
from decouple import config

EMAIL = "anshg7871@gmail.com"
PASSWORD = "2004"  # never use password use passkey provided


def find_my_ip():
    ip_address = requests.get("https://api.ipify.org?format=json").json()
    return ip_address["ip"]


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results


def search_on_google(query):
    kit.search(query)


def youtube(video):
    kit.playonyt(video)  # playontyt is a predefined function in pywhatkit library like search for google


def send_mail(receiver_add, subject, messege):
    try:
        email = EmailMessage()
        email['To'] = receiver_add
        email['Subject'] = subject
        email['Messege'] = messege

        email.set_content(messege)
        s = smtplib.SMTP("smpt@gmail.com", 587)  # standard port for secure messege transmission
        s.starttls()  # used for encryption of our messege
        s.login(EMAIL, PASSWORD)  # predfined function to configure our mail  id and password predefined already
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
def get_news():
    new_headlines=[]
    result=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey=39320c133d814e91a3c1688ceac8e48b").json()
    articles=result[articles]
    for article in articles:
        new_headlines.append(article["title"])
    return new_headlines[:6]
def weather_forecasting():
    res=requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m").json()
    weather=res["weather"][0]["main"]
    temp=res=["main"]["temp"]
    feels_like=res["main"]["feels_like"]
    return  weather,f"{temp}"C",f"{feels_like}"C"
