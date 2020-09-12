import pyttsx3 #pip install pyttsx3 
import speech_recognition as sr #pip install speechRecognition
import datetime #pip install datetime
import wikipedia #pip install wikipedia
import webbrowser #pip install pipwin
import os #pipwin install pyaudio
import smtplib

MASTER = "Sir"   
#print("Initiallizing Jarvis")
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[-0].id)  
#number in [] corresponds to speech settings voices  
# Voice Options [-3, -2, -2, -1, 0, -0, 1, 2] pick one

# Speak function will speak the string which is passed 
def speak(text):

    engine.say(text)
  
    engine.runAndWait()

#This function will wish you as per the current time 
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else: 
        speak("Good Evening" + MASTER)
    #speak("I am Jarvis. How may I help you sir?")         
#This function will take the command from microphone

def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-us' )
        print(f"user said: {query}\n")

    except Exception:
         print("Say that again sir") 
         query = None 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smptp.gmail.com', 587)  
    server.ehlo()
    server.starttls()
    server.login('youremail@gamil.com', 'yourpassword')
    server.sendmail("recipient@gmail.com", to, content)
    server.close
#Main program starts here...
def main():
    #speak("Initializing Jarvis....")
    wishMe()
    query = takeCommand()

    #Logic for excuting tasks per the query
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2) #2
        print(results)
        speak(results)
    #Make sure chrome.exe is in the correct directory
    elif 'open youtube' in query.lower():
        webbrowser.open('http://youtube.com')

    elif 'open google' in query.lower():
        webbrowser.open('http://google.com')

    #your own directory below navigate to your own music
    elif 'play music' in query.lower():
        songs_dir = 'C:\\Users\\joshua\\Music\\Playlists\\'
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir, songs[1]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'email to me' in query.lower():
        try:
            speak("What should I send")
            content = takeCommand()
            to = "recipient@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent")
        except Exception:
            print() 

main()
