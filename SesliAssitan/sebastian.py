from datetime import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import webbrowser
import random
import os
import time
from random import Random,choice
r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        except sr.RequestError:
            speak('sistem çalışmıyor')
        return voice

def response(voice):
    if 'nasılsın' in voice:
        speak('iyiyim siz nasılsınız')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('ne aramak istiyorsunuz')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(search + ' için bulduklarım')
   
        speak('youtube acılıyor')    
    if 'kapan' in voice:
        speak('görüşürüz')
        exit()

    if "github" in voice or "proje" in voice:
        speak("Githubda ne aramamı istersin?")
        search = record()
        url = "https://github.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("İşte github sonuçları.")

    if 'video aç' in voice:
        searchb = record('ne aramak istiyorsunuz ?')
        urlb = 'https://www.youtube.com/results?search_query='+ searchb
        webbrowser.get().open(urlb)
        speak(searchb + 'için bulduklarım')
   
        

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speak('Nasıl yardımcı olabilirim') 

while True:
    voice = record()
    print(voice)
    response(voice)