# DESAFIO 1- DIGITAR EM QUALQUER LUGAR:
# 12-06-2024 Comecei ontem, informarei quando terminar
# Assim ja me estou a ajustar no quesito de tempo que levarei a automatizar
# Entre em alguma pasta do computador, crie uma nova pasta usando pyautogui

# SEMPRE ANOTAR OS PASSOS SEQUENCIAS PARA TRANSFORMAR EM CODIGO:::

# Passos1 : Importar a biblioteca pyatuogui
# Passo 2: Mover o mouse ate a coordenada para digitar
# Clicar no campo para digitar
# Digitar a mensagem
# Clicar no botao de enviar


import pyautogui
from time import sleep
import pyperclip

# Defino uma fun~ção para temas de acentos linguisticos:
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.moveTo(x=788,y=992,duration=4)
pyautogui.click()
# Me faltava esse novo parametro!

escrever_frase('Olá, espero que esteja tudo muintissimo bemmm! Quero relatório do dia de hoje!')

# Cancelo a proxima linha de cogigo, pela função que criei acima:
#pyautogui.typewrite('Olá, agora sou eu novamente; o bot Elkamuti, espero que esteja tudo bem!')
#sleep(2)
#pyautogui.moveTo(x=1885,y=989,duration=4)
#pyautogui.click()

pyautogui.click(x=1885,y=989,duration=4)
