from playsound import playsound
from gtts import gTTS
from time import sleep


audio = 'galerinha.mp3'
language = 'pt-br'

sp = gTTS(
    text='E ae galerinha do grupo, deu certo criar o audio apartir de texto',
    lang=language
)

sp.save(audio)
sleep(2)
playsound('galerinha.mp3')
