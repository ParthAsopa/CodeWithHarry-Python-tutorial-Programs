import os
import speech_recognition as sr


def takeCommand():#speech to text (recognises speech and returns a string.)
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...\n")
        r.pause_threshold=1
        r.energy_threshold=200
        audio=r.listen(source)
        try:
            print("Recognizing...\n")
            query=r.recognize_google(audio,language="en-in")
            print(f"You said:{query}\n")
        except Exception as e:
            print("Couldn't understand...\n")
            return "None"
        return query


if __name__=="__main__":
    while True:
        query=takeCommand().lower()
        if "hello jarvis" in query:
            os.startfile(os.path.join("E:\\Working Folders\\Parth Asopa\\Coding(Programming)\\Python\\J.A.R.V.I.S","J.A.R.V.I.S. main.py"))
            print("\n\nOpening main file....\n\n")
        else:
            pass
