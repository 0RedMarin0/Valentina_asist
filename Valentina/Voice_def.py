"""
import pygame
import json, pyaudio
from vosk import Model, KaldiRecognizer
import webbrowser

pygame.init()
model = Model('model-small')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
bg_sound = pygame.mixer.Sound("Audio/Hi.mp3")
bg_sound.play()

#def listen():
while True:

  data = stream.read(4000, exception_on_overflow=False)
  if (rec.AcceptWaveform(data)) and (len(data) > 0):
      answer = json.loads(rec.Result())
      answer2 = json.loads(rec.Result())
      if answer['text']:
          if answer['text'] == "найди в яндексе":
              bg_sound = pygame.mixer.Sound("Audio/Hi.mp3")
              bg_sound.play()
              print('Что найти ?')
              if answer2['text']:
                  aaa = answer2['text']
                  urlurl = ('https://yandex.ru/search/?text='f'{aaa}''&lr=49&clid=2270455&win=583')
                  webbrowser.open(f"{urlurl}", new=2)
          else:
              print(answer['text'])
"""
import speech_recognition as sr
import os
import webbrowser
r = sr.Recognizer()
r.pause_threshold = 0.5
mic = sr.Microphone(device_index=1)


def voice():
    while True:
        with mic as source:
            try:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                comand = r.recognize_google(audio, language="ru-RU").upper()
                if comand == "ОТКРОЙ КАРТИНКУ":
                    os.system("C:/Users/RedMarin/Desktop/maxresdefault.jpg")
                elif comand == "НАЙДИ В ЯНДЕКСЕ":
                    print('Что найти ?')
                    audio2 = r.listen(source)
                    comand2 = r.recognize_google(audio2, language="ru-RU")
                    url = ('https://yandex.ru/search/?text='f'{comand2}''&lr=49&clid=2270455&win=583')
                    webbrowser.open(f"{url}", new=2)
                else:
                    print(comand)
            except:
                print('Это всё что угодно, но не речь !')
