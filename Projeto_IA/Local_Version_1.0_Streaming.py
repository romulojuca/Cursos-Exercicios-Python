from ctransformers import AutoModelForCausalLM
import speech_recognition as sr
from gtts import gTTS
import pygame
import tempfile
import os
import time

# --- CAMINHO DO MODELO GGUF LOCAL ---
MODEL_FILE = r"C:\Users\romul\Desktop\Python\Projeto_IA\wizardlm-7b-uncensored-q4_k_m.gguf"

# --- CARREGANDO MODELO (CPU) ---
print("Carregando modelo (CPU)...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_FILE,
    model_type="llama",
    gpu_layers=0  # CPU-only
)

# --- CONFIGURAÇÕES ---
history = ["User: Hello",
           "AI: Hello! I am an English teacher helping a user practice English."]
max_history = 4
recognizer = sr.Recognizer()
recognizer.pause_threshold = 2.0
pygame.mixer.init()

english_levels = {
    "number one": "Beginner",
    "number two": "Elementary",
    "number three": "Pre-Intermediate",
    "number four": "Intermediate",
    "number five": "Upper-Intermediate"
}

# --- SELEÇÃO DE NÍVEL ---
user_level = None
print("Please choose your English level by saying the number or name:")
for key, level in english_levels.items():
    print(f"{key} - {level}")

while user_level is None:
    with sr.Microphone() as source:
        print("Listening for your choice...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        spoken_text = recognizer.recognize_google(audio)
        print(f"You said: {spoken_text}")
        for key in english_levels:
            if key == spoken_text or english_levels[key].lower() == spoken_text.lower():
                user_level = english_levels[key]
                break
        if user_level is None:
            print("I didn't understand. Please say the number (1-5) or the level name.")
    except sr.UnknownValueError:
        print("Didn't catch that, please try again.")
    except sr.RequestError:
        print("Speech recognition service error.")

print(f"User level set to: {user_level}\n")
print("Fale 'exit' a qualquer momento para sair.\n")

# --- LOOP PRINCIPAL ---
while True:
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, phrase_time_limit=None)
    try:
        user_input = recognizer.recognize_google(audio)
        print(f"You (voice): {user_input}")
    except sr.UnknownValueError:
        print("Não entendi o que você disse, tente novamente.")
        continue
    except sr.RequestError:
        print("Erro de conexão com o serviço de reconhecimento de voz.")
        continue

    if user_input.lower() == "exit":
        break

    # --- HISTÓRICO ---
    history.append(f"User: {user_input}")
    recent_history = history[-max_history*2:]

    # --- INSTRUÇÕES DO MODELO ---
    instructions = f"""
    You must answer in full sentences and **always end your response with a question** that prompts the user to continue speaking.
    """

    # --- PROMPT ---
    prompt = f"{instructions}\n" + "\n".join(recent_history) + "\nAI:"

    # --- RESPOSTA (streaming) ---
    response_text = ""
    for chunk in model._stream(
        prompt,
        max_new_tokens=150,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        stop=["\nUser:", "\nYou:"]
    ):
        response_text += chunk
        print(chunk, end="", flush=True)

    print("\n")

    history.append(f"AI: {response_text.strip()}")

    # --- TTS ---
    tts = gTTS(response_text, lang='en')
    temp_file = os.path.join(tempfile.gettempdir(), "response.mp3")
    tts.save(temp_file)

    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.unload()
    os.remove(temp_file)
