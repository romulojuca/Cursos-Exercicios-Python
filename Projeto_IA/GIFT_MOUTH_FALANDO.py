import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading
from gtts import gTTS
import pygame
import tempfile
import os
import time

pygame.mixer.init()

root = tk.Tk()
root.title("GIF fala test")
root.geometry("400x400")

# Label para o GIF
gif_label = tk.Label(root)
gif_label.pack()

# Carrega GIF
gif_path = "mouth.gif"  # caminho do seu GIF
gif_image = Image.open(gif_path)
frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA"))
          for frame in ImageSequence.Iterator(gif_image)]

frame_index = 0
animating = False


def animate_gif():
    global frame_index
    if animating:
        gif_label.config(image=frames[frame_index])
        frame_index = (frame_index + 1) % len(frames)
        root.after(100, animate_gif)  # ajusta velocidade aqui


def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(50)
    global animating
    animating = False
    gif_label.config(image=frames[0])  # volta para frame inicial


def speak_text(text):
    global animating, frame_index
    frame_index = 0
    animating = True

    # Cria arquivo temporário de áudio
    temp_file_path = os.path.join(
        tempfile.gettempdir(), f"tts_{int(time.time()*1000)}.mp3")
    tts = gTTS(text, lang='en')
    tts.save(temp_file_path)

    # Inicia animação
    animate_gif()

    # Toca áudio em outra thread
    threading.Thread(target=play_audio, args=(
        temp_file_path,), daemon=True).start()


# Botão para falar
tk.Button(root, text="Speak", command=lambda: speak_text(
    "Hello, how are you?")).pack(pady=20)

root.mainloop()
