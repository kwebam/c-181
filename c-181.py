from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime


root = Tk()
root.geometry("500x500")

text_to_speech = pyttsx3.init()
def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def r_audio():
    speak("How can i help you..?")
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data=''
    try:
        voice_data= speech_recognisor.recognize_google(audio, language='en-in')
        
    except sr.UnknownValueError:
        print("Please repeat i did not get that")
        speak("Please repeat i did not get that")
        
    respond(voice_data)
    
def respond(voice_data):
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Amol Kumar")
        print("My name is Amol Kumar")
    if "time" in voice_data:
        speak("Current time is ")
        now = datetime.now()
        Current_time = strftime("%H:%M:%S")
        speak(Current_time)
        print(Current_time)

        
r_audio()

root.mainloop()