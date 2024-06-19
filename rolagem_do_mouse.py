#print('Seguimos somando!')

# Mini projecto - Rolagem do Mouse:
import pyautogui
from time import sleep

pyautogui.moveTo(x=1909,y=188,duration=4)
for i in range (2):
    pyautogui.scroll(-1500)
    sleep(4)
    
# Depois va para a pagina de Aplicações
pyautogui.moveTo(x=137,y=528,duration=4)
pyautogui.click()


# Porjectionho super interessante que vai aumentando ainda mais a 
# A minha forma de ver o python.
# As coisas se estão encaixando