import os
from gtts import gTTS
import  datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser



def speak(hey):
    tts = gTTS(text = hey, lang = 'hi',slow = False)
    tts.save("p4.mp3")
    os.system("p4.mp3")
   

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <12:
        speak("good morning Ankit How are you! ")
    elif hour>=12 and hour <18 :
        speak("good Afternoon Ankit How are you! ")
    else :
        speak("good evening Ankit How are you!. ")
    speak("I am your Assistance. Please tell me  how can I help You")

def takecammand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        audio = r.listen(source) 
        try:
            print("Recognizing....")
            text = r.recognize_google(audio)
            print(f"You said : {text}")
        except:
            print("sorry recognize your voice ")
            return 'None'

    return text


if __name__=="__main__":

    wish()
    while True:
        query = takecammand().lower()
        web=webbrowser.get('windows-default')

        if 'wikipedia' in query:
            speak("searching wikipedia .....please wait")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According wikipedia ......")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening Youtube .....")
            web.open('https://youtube.com')
            
        elif 'open google' in query:

            speak("opening gogle ")
            web.open('https://google.com')
        elif 'play music' in query:
            try:
               music="D:\\aman\\Top 20 Heart Touching Songs 2018 October ★ New Romantic Hindi Hist Song 2018 Octorber ★ Indian Song ( 256kbps cbr ) - Shortcut.lnksong"
               songs = os.listdir(music)
               print(songs)
               os.startfile(os.path.join(music ,songs[0]))
            except:
                print("somthing Error")
                speak("Try Again")
        elif 'play video' in query:
            video='D:\\movie'
            count=os.listdir(video)
            print(count)
            os.startfile(os.path.join(video ,count[0]))
        
            
    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" the time is {strTime}")
        elif 'favourite setup' in query:
            speak("tell me your favraiot video name")
            query
            faviraiot=takecammand()
            print("compleat!")
            speak ("setup is ready")
            
        elif 'favourite video' in query:
            speak("openning")
            web.open(f"https://www.youtube.com/results?search_query={faviraiot}")                 

        elif 'bye' in query:
            speak("byee Mr. Ankit singh and wish you have a nice day....")
            break
        else :
            speak("I have no any such this cammand plz. standart cammand ")
