import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os  
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good Night")
               
    speak("Hello I am your Assistant .How can i help u?")



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio , language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please....")

        return "None"
    return query

def sendmail(to ,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("Youremail@gmail.com")
    server.sendEmail("Youremail@gmail.com",to ,content)

def screenshot():
    img =pyautogui.screenshot()
    img.save("screenshot.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at "+ usage)   

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent) 

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":

    wishme()

    while True:
        query = takecommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching.....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences=2)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should I say?")
                content = takecommand()
                to ="Receiveremail@gmail.com"
                sendmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search in chrome" in query:
            speak("what should i search?...")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search +".com")

        elif "logout" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shoutdown /s /t l")

        elif "restart" in query:
            os.system("shoutdown /r/t l")

        elif "play songs" in query:
            songs_dir = "c:\music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
            
        elif "remember that" in query:
            speak("what should I Remember?..")
            data = takecommand()
            speak("You said me to remember" +data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt")
            speak("You said to me remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done!")

        elif "cpu" in query:
            cpu()
        
        elif "joke" in query:
            jokes()
        

        

        
        