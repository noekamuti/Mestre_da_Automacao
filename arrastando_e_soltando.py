# DESAFIO 1- PASSAGEM DE ARQUIVOS 11-06-2024 Comecei ontem, informarei quando terminar
# Assim ja me estou a ajustar no quesito de tempo que levarei a automatizar
# Entre em alguma pasta do computador, crie uma nova pasta usando pyautogui
# Passos1 : Importar a biblioteca 
# Passo 2: Mover o maouse ate a coordenada
# Passo 3: Arrastar ate ao ponto
# Passo 4: Soltar
# Passo 5: Repetir 9x

'''import pyautogui
# Escolha da posição base e coordenadas
pyautogui.rightClick(1408,508,duration=4)
pyautogui.move(50,200,duration=4)
# Acto de clicar na pasta que desejo
pyautogui.click()
pyautogui.rightClick(1164,194,duration=4)
pyautogui.click()
'''
import pyautogui

for i in range(5):
    pyautogui.moveTo(x=396,y=681,duration=1)
    pyautogui.dragTo(1316,466,button='left',duration=0.5)
#pyautogui.move(80,200,duration=4)
#pyautogui.click()
#pyautogui.rightClick(x=994,y=174,duration=4)
#pyautogui.doubleClick()

