#Olá, espero que esteja tudo muintissimo bemmm!

import pyautogui
import pyperclip

def transcrever_texto(frase):
     pyperclip.copy(frase)
     pyautogui.hotkey('ctrl','v')
#pyautogui.moveTo(x=996,y=447,duration=4)
#pyautogui.click()
pyautogui.click(x=996,y=447,duration=4)
transcrever_texto('Consegui passar ao bloco de notas! Obáááá')
#pyautogui.typewrite ('Consegui passar ao bloco de notas! Obáááá')
#pyautogui.moveTo(x=996,y=777,duration=12)