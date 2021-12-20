import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
import os
import random
import playsound

engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def speak(text):#line 5 to 11 for text to speech
    engine.say(text)
    engine.runAndWait()

def wishMe():#wishes you according to time
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Good morning sir!!\n")
        speak("Good morning sir!!")
    elif hour>=12 and hour<17:
        print("Good afternoon sir!!\n")
        speak("Good afternoon sir!!")
    elif hour>=17 and hour<20:
        print("Good evening sir!!\n")
        speak("Good evening sir!!")
    elif hour>=20 and hour<0:
        print("Good night sir!!\n")
        speak("Good night sir!!")
    print("Jarvis at your service, how may I help you?\n")
    speak("Jarvis at your service, how may I help you?")


def takeCommand():#speech to text (recognises speech and returns a string.)
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...\n")
        playsound.playsound("E:\\Working Folders\\Parth Asopa\\Coding(Programming)\\Python\\J.A.R.V.I.S\\tone.mp3")
        r.pause_threshold=1
        r.energy_threshold=200
        audio=r.listen(source)
        try:
            print("Recognizing...\n")
            query=r.recognize_google(audio,language="en-in")
            print(f"You said:{query}\n")
        except Exception as e:
            print(e)
            print("Pardon...could you please repeat...\n")
            speak("Pardon...could you please repeat...")
            return "None"
        return query


if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if "wikipedia" in query:
            print("Searching wikipedia....")
            speak("Searching wikipedia....")
            query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(f"According to wikipedia: {results}")
            speak(f"According to wikipedia: {results}")

        elif "open youtube" in query:
            print("opening youtube")
            speak("opening youtube")
            webbrowser.open("http://www.youtube.in/")

        elif "open whatsapp" in query:
            print("opening WhatsAapp")
            speak("opening whatsapp")
            webbrowser.open("http://web.whatsapp.com/")
        
        elif "open google" in query:
            print("opening Google")
            speak("opening Google")
            webbrowser.open("http://www.google.com/")

        elif "google" in query:
            print("What do you want me to Google?")
            speak("What do you want me to google?")
            sub_query=takeCommand().lower()
            if sub_query!="none":
                webbrowser.open(f"https://www.google.com/search?q={sub_query}&sxsrf=AOaemvKxUuOaxrnphUh4Fecjs7lufPL4ow%3A1636362702389&ei=zumIYZWSF8LWz7sPp4inkA4&oq=hot&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBAguEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyCwgAEIAEELEDEIMBMg4IABCABBCxAxCDARDJAzoFCAAQgAQ6CAgAELEDEIMBOggIABCABBCxAzoKCAAQsQMQgwEQQzoKCC4QsQMQQxCTAkoECEEYAFAAWNoMYOodaAFwAngAgAHoAYgBoAaSAQUwLjIuMpgBAKABAcABAQ&sclient=gws-wiz&ved=0ahUKEwiVseWMtoj0AhVC63MBHSfECeIQ4dUDCA8&uact=5")
                print(f"Searching {sub_query} on Google...")
                speak(f"Searching {sub_query} on Google...")
        elif "youtube" in query:
            print("What do you want me to search on YouTube?")
            speak("What do you want me to search on youtube?")
            sub_query=takeCommand().lower()
            if sub_query!="none":
                webbrowser.open(f"https://www.youtube.com/results?search_query={sub_query}")
                print(f"Searching {sub_query} on YouTube...")
                speak(f"Searching {sub_query} on YouTube...")

        elif "open allen" in query:
            print("Opening Allen Digital...")
            speak("Opening Allen Digital...")
            webbrowser.open("https://student.allendigital.in/Pune/dashboard/2021-2022/PUNE6F53D0/PARTH-ASOPA?token=bgG05e%2f9P2P0sFnueF4eF31v9Bgtx2N9n2XdDUkDxVs%3d")

        elif "open allen digital" in query:
            print("Opening Allen Digital...")
            speak("Opening Allen Digital...")
            webbrowser.open("https://student.allendigital.in/Pune/dashboard/2021-2022/PUNE6F53D0/PARTH-ASOPA?token=bgG05e%2f9P2P0sFnueF4eF31v9Bgtx2N9n2XdDUkDxVs%3d")

        elif "open drive" in query:
            print("Opening Google Drive...")
            speak("Opening Google Drive...")
            webbrowser.open("https://drive.google.com/")
        
        elif "open calendar" in query:
            print("Opening Google Calender...")
            speak("Opening Google calender...")
            webbrowser.open("https://calendar.google.com/calendar/u/0/r")

        elif "open github" in query:
            print("Opening GitHub...")
            speak("Opening GitHub...")
            webbrowser.open("https://github.com/")



        elif "play music" in query:
            music_dir="C:\\Users\\Parth Asopa\\Music"
            songs=os.listdir(music_dir)#list of songs in the folder
            rand=random.randint(0,len(songs))#picks random song from list of songs in folder.
            print(f"Playing {songs[rand]} ")
            speak(f"Playing {songs[rand]} ")
            os.startfile(os.path.join(music_dir, songs[rand]))#join here joins the name of the song in the end of path of music folder.
# syntax of starting a file from os module--> os.startfile(os.path.path of file)




        elif "open telegram" in query:
            print("Opening Telegram...")
            speak("Opening Telegram...")
            os.startfile(os.path.join("F:\Programs\Telegram Desktop","Telegram.exe"))

        
        elif "internet" in query:
            print("Opening Brvae Browser...")
            speak("Opening Brvae Browser...")
            os.startfile(os.path.join("C:\ProgramData\Microsoft\Windows\Start Menu\Programs","Brave.ink"))
        
        elif "open" in query:
            index= query.find("open")
            arguement=query[index+5:]
            try:
                os.startfile(os.path.join("C:\ProgramData\Microsoft\Windows\Start Menu\Programs",f"{arguement}.ink"))
            except Exception as e:
                os.startfile(os.path.join(f"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\{arguement}",f"{arguement}.ink"))
            except:
                print("Here's what I found on Google...")
                speak("Here's what I found on Google...")
                webbrowser.open(f"https://www.google.com/search?q={arguement}&sxsrf=AOaemvKxUuOaxrnphUh4Fecjs7lufPL4ow%3A1636362702389&ei=zumIYZWSF8LWz7sPp4inkA4&oq=hot&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBAguEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyCwgAEIAEELEDEIMBMg4IABCABBCxAxCDARDJAzoFCAAQgAQ6CAgAELEDEIMBOggIABCABBCxAzoKCAAQsQMQgwEQQzoKCC4QsQMQQxCTAkoECEEYAFAAWNoMYOodaAFwAngAgAHoAYgBoAaSAQUwLjIuMpgBAKABAcABAQ&sclient=gws-wiz&ved=0ahUKEwiVseWMtoj0AhVC63MBHSfECeIQ4dUDCA8&uact=5")
                    
        elif "time" in query:
            hour=datetime.datetime.now().hour
            minute=datetime.datetime.now().minute
            if hour>=0 and hour<12:
                time="morning"
            elif hour>=12 and hour<17:
                hour-=12
                time="afternoon"
            elif hour>=17 and hour<20:
                hour-=12
                time="evening"
            elif hour>=20 and hour<0:
                hour-=12
                time="night"

            print(f"Its {hour}:{minute} in the {time}.")
            speak(f"Its {hour} {minute} in the {time}.")

        elif query=="none":
            pass

        elif query=="exit":
            print("See you soon sir!!")
            speak("See you soon sir!!")
            break

        elif query=="power off":
            print("See you soon sir!!")
            speak("See you soon sir!!")
            break

        elif query=="quit":
            print("See you soon sir!!")
            speak("See you soon sir!!")
            break

        elif "bye jarvis" in query:
            print("See you soon sir!!")
            speak("See you soon sir!!")
            break
        
        elif query=="go to sleep":
            print("See you soon sir!!")
            speak("See you soon sir!!")
            break


        elif query=="bye bye":
            print("See you soon sir!!")
            speak("See you soon sir!!")
            break



        else:
            print("Here's what I found on Google...")
            speak("Here's what I found on Google...")
            webbrowser.open(f"https://www.google.com/search?q={query}&sxsrf=AOaemvKxUuOaxrnphUh4Fecjs7lufPL4ow%3A1636362702389&ei=zumIYZWSF8LWz7sPp4inkA4&oq=hot&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBAguEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyCwgAEIAEELEDEIMBMg4IABCABBCxAxCDARDJAzoFCAAQgAQ6CAgAELEDEIMBOggIABCABBCxAzoKCAAQsQMQgwEQQzoKCC4QsQMQQxCTAkoECEEYAFAAWNoMYOodaAFwAngAgAHoAYgBoAaSAQUwLjIuMpgBAKABAcABAQ&sclient=gws-wiz&ved=0ahUKEwiVseWMtoj0AhVC63MBHSfECeIQ4dUDCA8&uact=5")
