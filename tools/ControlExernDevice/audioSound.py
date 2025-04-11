import pyaudio
import speech_recognition as sr # для считывания записи с микрафона и переобразования в текст 
import tkinter as tk
import keyboard # для увелечения значения в функции readMicrophone в переменной record_second чтоб когда нажимал на кнопку и он добовлял значение переменой на 1 минуту и больше 
import wave


def readMicrophone(DeviceIndex=1, timeout=7, phrase_time_limit=5):
    windows = tk.Tk()
    windows.geometry("650x450")
    windows.title("Запись с микрофона")
    windows.resizable(False, False)

    # p = pyaudio.PyAudio() device microphone use users 
    # for i in range(p.get_device_count()):
    #     print(i, p.get_device_info_by_index(i)['name'])



    r = sr.Recognizer()

    def speech():
        with sr.Microphone(device_index=DeviceIndex) as sourse:
            txt_label.configure(text="Говорите...")
            windows.update()

            try:
                audio = r.listen(sourse, phrase_time_limit=phrase_time_limit, timeout=timeout)
                query = r.recognize_google(audio, language='ru-RU')
            
            except(sr.WaitTimeoutError, sr.UnknownValueError):
                txt_label.configure(text="Я вас не понял или не слышу....Скажите еще раз....")
                windows.update()
                speech()
            
            else:
                txt_label.configure(text="Нажмите на кнопку и говорите")
                return query.capitalize()
            
    def insert_rec():
        recording = speech()
        txt.insert(1.0, recording)
            
    txt = tk.Text(windows)
    txt.place(x=0, y=0)


    # def save_output(): # funcition not active 
    #     with open("static/audio/output.mp3", "w+") as file:
    #         file.write(txt_label)
    #         file.close()

    button_rec = tk.Button(windows, text='rec', bg='red', font=('copper', 16), command=insert_rec)
    button_rec.place(x=30, y=400)
    # button_save_audio = tk.Button(windows, text="save output", font=('copper', 16), command=save_output)

    txt_label = tk.Label(windows, text="Нажмите на кнопку и говорите", font=('coover', 16))
    txt_label.place(x=100, y=408)
    # button_save_audio.place(x=30, y=10)
    windows.mainloop()
    
def readMicroAndSave(filename="recorded.wav",  record_second=5):
    # имя файла для записи
    filename = "recorded.mp3"
    # установить размер блока в 1024 сэмпла
    chunk = 1024
    # образец формата
    FORMAT = pyaudio.paInt16
    # моно, если хотите стере измените на 2
    channels = 1
    # 44100 сэмплов в секунду
    sample_rate = 44100
    record_seconds = 5
    # initialize PyAudio object
    p = pyaudio.PyAudio()
    # открыть объект потока как ввод и вывод
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
        # если вы хотите слышать свой голос во время записи
        # stream.write(data)
        frames.append(data)
    print("Finished recording.")
    # остановить и закрыть поток
    stream.stop_stream()
    stream.close()
    # завершить работу объекта pyaudio
    p.terminate()
    # сохранить аудиофайл
    # открываем файл в режиме 'запись байтов'
    wf = wave.open(filename, "wb")
    # установить каналы
    wf.setnchannels(channels)
    # установить формат образца
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # установить частоту дискретизации
    wf.setframerate(sample_rate)
    # записываем кадры как байты
    wf.writeframes(b"".join(frames))
    # закрыть файл
    wf.close()