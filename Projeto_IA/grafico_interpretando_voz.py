import tkinter as tk
import threading
import wave
import struct
import numpy as np
import pyttsx3
import simpleaudio as sa
from gtts import gTTS
import tempfile
import os
import time


# ===== Função de animação de ondas =====
def animate_waves(canvas, wav_path):
    wav = wave.open(wav_path, 'rb')
    n_frames = wav.getnframes()
    frames_per_chunk = 1024
    width = int(canvas['width'])
    height = int(canvas['height'])

    def update():
        while True:
            data = wav.readframes(frames_per_chunk)
            if len(data) == 0:
                break
            count = len(data) // 2
            shorts = struct.unpack("%dh" % count, data)
            amp = np.abs(shorts)
            avg_amp = np.mean(amp) / 32768

            canvas.delete("wave")
            num_bars = 50
            bar_width = width / num_bars
            for i in range(num_bars):
                bar_height = avg_amp * height * np.random.uniform(0.5, 1.0)
                x0 = i * bar_width
                y0 = height - bar_height
                x1 = x0 + bar_width * 0.8
                y1 = height
                canvas.create_rectangle(
                    x0, y0, x1, y1, fill="#1E90FF", tag="wave")
            canvas.update()
            time.sleep(0.03)
        canvas.delete("wave")
        wav.close()

    threading.Thread(target=update, daemon=True).start()


# ===== Função para falar com gTTS e pyttsx3 =====
def speak_text(text, canvas):
    # --- WAV temporário para animação ---
    wav_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
    engine = pyttsx3.init()
    engine.save_to_file(text, wav_path)
    engine.runAndWait()

    # --- MP3 temporário para voz da IA ---
    mp3_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
    tts = gTTS(text=text, lang='en')
    tts.save(mp3_file)

    # --- Toca o MP3 da IA ---
    try:
        import playsound
        time.sleep(0)
        threading.Thread(target=lambda: playsound.playsound(
            mp3_file), daemon=True).start()
    except:
        print("Erro ao tocar o MP3. Certifique-se de ter a biblioteca playsound instalada.")

    # --- Inicia animação das ondas (WAV) ---
    time.sleep(0.3)
    animate_waves(canvas, wav_path)


# ===== GUI =====
root = tk.Tk()
root.title("IA Falando com Ondas")
root.geometry("600x300")

canvas = tk.Canvas(root, width=580, height=150, bg="#EEE")
canvas.pack(pady=50)

tk.Button(root, text="Falar: Hello, how are you?",
          command=lambda: threading.Thread(target=speak_text, args=(
              "Hello, how are you, are you doing well?", canvas), daemon=True).start()
          ).pack(pady=10)

root.mainloop()
