# =====         first big project for python ( as a beginner)
# Making an personal PC assistant 
import pyttsx3
import speech_recognition as spr
import datetime
import webbrowser
import wikipedia
import random
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice',voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():        
    wis=int(datetime.datetime.now().hour)
    if wis>6 and wis<12:
        speak("Good morning Boss")
    elif wis>12 and wis<16:
        speak("Good Afternoon Boss")
    elif wis>16 and wis<=18:
        speak("Good Evening Boss")
    else:
        speak("night! Again")

def takcommand():
    r = spr.Recognizer()
    with spr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"Command : {query}\n")
    except Exception as e:
        # print(e)
        print('say that again...')
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('sdeymicro2021@gmail.com','Email_password')
#     server.sendmail('sdeyimcro2021@gmail.com',to,content)
#     server.close()
                #email functin is not set until i dont enable the less secure apps to send and access email 

if __name__ =="__main__":
    greet()
    speak("Aisha at your service")
    speak("need help?")
    #while True:
    if 1:
        query=takcommand().lower()
    
        if "wikipedia" in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences=4)
            speak('According to wikipedia..')
            speak(result)
            speak('this is what i found:')
            print(result)
        
        elif "google" in query:
            webbrowser.open("google.com")
        elif "geeks for geeks" in query:
            webbrowser.open("www.geeksforgeeks.org")
       
        elif "what is the time" in query:
            speak(datetime.datetime.now().strftime('%H:%M:%S'))

        elif "play some music"in query:
            music_dir='C:\\Users\\sdeym\\Music\\'
            songs=os.listdir(music_dir)
            speak('ok playing music')
            # s=[]
            # s.extend(list(songs))
            # r=random.s
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "open Photo shop" in query:
            fil= 'C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe'
            os.startfile(fil)


                    # This function will initialize after i add the library of emails with the keys in it as names . and I have to activate teh 'sendEmail' function 

        # elif "send an email" in query:
        #     try:
        #         speak("Whoom should I approach?")
        #         sendaddress= takcommand()
        #         speak("what is your message?")
        #         content = takcommand()
        #         to = email[sendaddress] ## The list of the emails have to be made with email id's and the names as keys
        #         sendEmail(to, content)
        #         speak('Emain sent successfully')
        #     except Exception as e:
        #         print(e)
        #         speak('Some issues have occurred!! Email not sent')

