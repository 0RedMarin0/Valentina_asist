import sounddevice as sd

def callback(indata, frames, time, status):
    # Здесь можно выполнять необходимую обработку звуковых данных
    pass

# Установка параметров записи звука
duration = 10  # Длительность записи в секундах
sample_rate = 44100  # Частота дискретизации

# Начало записи аудио с микрофона
with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate):
    print("Запись началась.")
    sd.sleep(int(duration * 1000))
    print("Запись окончена.")