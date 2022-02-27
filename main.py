#!/usr/bin/python3
import speech_recognition as sr
import pyttsx3 # converts text to speech
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

# set voice to female
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# engine.say("Hi, I'm Jarvis")
# engine.say("At your service")
# engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source: # source of audio
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                # engine.say(command)
                # engine.runAndWait()
                command = command.replace('jarvis', '')
                print(command)
                # talk(command)
    except:
        print("Something else went wrong")
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say that command again')

while True: # runs the virtual assistant infinitely
    run_jarvis()