import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

import time
time.sleep(1)  # Add a delay to let the microphone initialize


import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsApi="95619dba11854e87b708063ff16f1d52"

        

def speak(text):
    female_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', female_voice_id)
    engine.setProperty('rate' ,175)#voice control
    engine.say(text)
    engine.runAndWait()

def open_custom_file(file_name):
    file_path = f"C:/Users/subha/Downloads/{file_name}.png"  # Correctly format the file path
    if os.path.exists(file_path):
        os.startfile(file_path)
    else:
        speak("Sorry, the file does not exist.")
   

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/watch?v=IV-MKtSOZNY&ab_channel=ShemarooMusicalMaestros")
    elif "open song" in c.lower():
        webbrowser.open("https://www.youtube.com/watch?v=ilNt2bikxDI")
    elif"open file" in c.lower():
         file_path= r"C:\Users\subha\Downloads"
         os.startfile (file_path)
    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open[link]
    elif "open file" in c.lower():
        speak("Give me the file name")
        while True:
            print("4Recognizing...")
            try:
                with sr.Microphone() as sou:
                    print("3Listening...")
                    name = recognizer.listen(sou, timeout=1, phrase_time_limit=1)
                name1 = recognizer.recognize_google(name)
                print(name1)
                open_custom_file(name1)
                break
            except Exception as e:
                speak(f"Sorry, I didn't understand that. {str(e)}")  
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsApi}")
        if r.status_code ==200:
            data= r.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])

    

    speak(f"Opening")
    
    
if __name__ == "__main__":
    speak("Initializing AKIRA....")
    while True:
        # Listen for the wake word "Akira"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print(word)
            
            
            if "exit" in word:
                speak("Goodbye There.....")
                break
            if(word.lower() == "akira"):
                speak("Hi There \n How may I help You")
                # Listen for command
                with sr.Microphone() as source:
                    print("Akira Active...")
                    audio = r.listen(source,timeout=5,phrase_time_limit=5)
                    command = r.recognize_google(audio)

                    processCommand(command)
                     
        except Exception as e:
            speak("Sorry, I didn't understand that; {0}".format(e))
            
