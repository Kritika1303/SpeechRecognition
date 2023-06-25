import gettext
import time
import os
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)
        print("Say that again please...")
        return "None"
    return query



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('voice', voices[0].id)
print('Hello sir, How can I help you?')
speak('Hello sir, How can I help you?')

while True:
        dt = datetime.datetime.now().strftime("%H:%M:%S")
        query = takeCommand().lower()

        if 'morning' in query:
            print("God's mercy is fresh and new every morning. Good morning sir")
            speak("God's mercy is fresh and new every morning. Good morning sir")
        elif 'google'.lower() in query:
            speak('What should i search on google sir?')
            Google = 'https:\\google.com'
            cm = takeCommand().lower()
            webbrowser.open(f'{cm}')
            speak(f'searching {cm} in Google ')
        elif 'youtube' in query:
            speak('Opening Youtube, sir')
            yt = 'https:\\youtube.com'
            os.startfile(yt)
            time.sleep(1)
            speak('Opened youtube')
        elif 'night' in query:
            print("Good night, sleep tight, don't let the bed bugs bite.")
            speak("Good night, sleep tight, don't let the bed bugs bite.")
        elif 'evening' in query:
            print("Good evening sir, take a sip of your coffee and forget the troubles of the day.")
            speak("Good evening sir, take a sip of your coffee and forget the troubles of the day.")
        elif 'time' in query:
            dt = datetime.datetime.now().strftime("%H:%M:%S")
            print(f'The time is {dt}')
            speak(f'The time is {dt}')
        elif 'game'.lower() in query:
            speak('Which game sir? Genshin impact[GI] or krunker[Kr]?: ')
            which = input('Which game sir? Genshin impact[GI] or krunker[Kr]?: ')
            if which.upper() == 'GI':
                print('opening Genshin impact')
                speak('opening Genshin impact')
                game = "C:\\Program Files\\Genshin Impact\\launcher.exe"
                time.sleep(2)
                os.startfile(game)
            if which.upper() == 'KR':
                print('opening Krunker')
                speak('opening krunker')
                krunker = 'https:\\krunker.io'
                time.sleep(2)
                os.startfile(krunker)
        elif 'discord'.lower() in query:
            print('opening discord')
            speak('opening Discord')
            discord = 'https://discord.com/channels/@me'
            time.sleep(2)
            os.startfile(discord)
        elif 'chess'.lower() in query:
            print('opening chess.com')
            speak('Opening Chess.com')
            chess = 'https://www.chess.com/play/computer'
            time.sleep(2)
            os.startfile(chess)
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'help' in query:
            print('I can help you with anything sir, just ask! ')
            print('for example you can ask me time or tell me to open google or youtube I am always available for you!')
            speak('I can help you with anything sir, just ask!')
            speak('for example you can ask me time or tell me to open google or youtube I am always available for you!')
        elif 'osu' in query:
            print('opening osu')
            speak('opening osu')
            osu = 'C:\\Users\\garva\\AppData\\Local\\osu!\\osu!.exe'
            time.sleep(0.5)
            os.startfile(osu)
        elif 'hello' in query:
            print(f'hello sir, the time right now is {dt}')
            speak(f'hello sir, the time right now is {dt}')
        elif 'hi' in query:
            print(f'Hi sir, the time right now is {dt}')
            speak(f'Hi sir, the time right now is {dt}')
        elif 'date' in query:
            d = datetime.date.today()
            print(f'date today is {d}')
            speak(f'date today is {d}')
        elif 'Thank' in query:
            print('No problem sir.')
            speak('No problem sir!')
        elif 'bye' in query:
            print('Bye sir')
            speak('Bye sir')
            exit()
        elif 'spotify' in query:
            print('opening spotify')
            speak('opening spotify')
            spotify = "C:\\Users\\garva\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotify)
            time.sleep(2)
            speak('successfully opened spotify')
        elif 'whatsapp' in query:
            print('opening whatsapp')
            speak('opening whatsapp')
            whatsapp = 'https://web.whatsapp.com/'
            os.startfile(whatsapp)
        elif 'thank' in query:
            print('Mention not, sir')
            speak('mention not, sir')
