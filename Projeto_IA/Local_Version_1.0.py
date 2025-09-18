from ctransformers import AutoModelForCausalLM
import speech_recognition as sr
from gtts import gTTS
import pygame
import tempfile
import os
import time

# --- CAMINHO DO MODELO GGUF LOCAL ---
MODEL_FILE = r"C:\Users\romul\Desktop\Python\Projeto_IA\wizardlm-7b-uncensored-q4_k_m.gguf"

# --- CARREGANDO MODELO ---
print("Carregando modelo...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_FILE,
    model_type="llama",   # GGUF compatível com ctransformers
    gpu_layers=0           # desativa GPU para 6GB VRAM
)

# --- LOOP DE CONVERSA COM VOZ E HISTÓRICO ---
print("Fale 'exit' a qualquer momento para sair.\n")

history = []          # histórico de interações
max_history = 4       # quantas interações armazenar

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1.5  # mais responsivo

pygame.mixer.init()   # inicializa áudio

# --- Nível de inglês do usuário ---
english_levels = {
    "number one": "Beginner",
    "number two": "Elementary",
    "number three": "Pre-Intermediate",
    "number four": "Intermediate",
    "number five": "Upper-Intermediate"
}

user_level = None
print("Please choose your English level by saying the number or name:")
for key, level in english_levels.items():
    print(f"{key} - {level}")

while user_level is None:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        spoken_text = recognizer.recognize_google(audio).lower()
        for key in english_levels:
            if key in spoken_text or english_levels[key].lower() in spoken_text:
                user_level = english_levels[key]
                break
        if user_level is None:
            print("I didn't understand. Please say the number (1-5) or the level name.")
    except sr.UnknownValueError:
        print("Didn't catch that, please try again.")
    except sr.RequestError:
        print("Speech recognition service error.")

print(f"User level set to: {user_level}\n")

# --- LOOP PRINCIPAL ---
while True:
    # --- CAPTURA DE VOZ ---
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        print("Listening...")
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

    # --- ADICIONA AO HISTÓRICO ---
    history.append(f"User: {user_input}")
    recent_history = history[-max_history*2:]

    # --- INSTRUÇÕES OTIMIZADAS DO MODELO ---
    instructions = f"""
    "role": "system",
        "content":
        You are an English teacher who helps the user to practice speaking. Always use {user_level} English.
        If the user makes any mistakes in vocabulary, grammar, tense or context, correct them carefully. 
        Provide a brief explanation of the correction, explain why this part is wrong, and sometimes offer an improved version of the sentence. 
        Do not correct the punctuation "." "," ";" ":". 
        After the correction, continue the conversation naturally and  always ask a question to keep the user engaged.
        Never use asterisk "*".
        If the user's response does not directly answer your question or seems unrelated, gently ask for clarification, e.g. "Did you mean…?" or "Can you clarify what you meant by that?"
        Always finish your sentences completely.
        Keep your answers short (1-3 sentences).
        Be friendly, patient, and encouraging.
    """

    # --- MONTAR PROMPT ---
    prompt = f"{instructions}\n" + "\n".join(recent_history) + "\nAI:"

    # --- GERA RESPOSTA ---
    response = model(
        prompt,
        max_new_tokens=120,    # aumenta ligeiramente para respostas mais completas
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        stop=["\nUser:", "\nYou:"]
    )
    response_text = response.strip()
    print("\n=== RESPOSTA DO MODELO ===")
    print(response_text)

    # --- ADICIONA RESPOSTA AO HISTÓRICO ---
    history.append(f"AI: {response_text}")

    # --- CONVERTE TEXTO PARA VOZ ---
    tts = gTTS(response_text, lang='en')
    temp_file = os.path.join(tempfile.gettempdir(), "response.mp3")
    tts.save(temp_file)
    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.unload()
    os.remove(temp_file)
