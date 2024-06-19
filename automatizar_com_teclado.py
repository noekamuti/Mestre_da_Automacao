# 17-06-2024 | 19-06-2024
# Tempo: 9:00 minutos de aula

# Ontem e anteontem estive meio embaixo, mistura da Gripe e cabeça as voltas, mas estou bem hoje e seguimos automatizando
# Surgiu-me a preocupação de ha: Estou a criar automações e o pyautogui agora é pago! Resposta: 
# E o que que isso me impede de continuar? Quem me esta a ensinar Python, me irá ensinar a usar a versão paga e por ai!
# Apenas devo me preocupar em aprender e entrar nesse NICHO DA AUTOMATIZAÇÃO
# Ele saberá como me direcionar 

# DESAFIO 1- Usar o teclado para fazer login numa pagina web, por si só
# Como usar os botões e atalhos?
# Passo 1: Importar a biblioteca 
# Passo 2: Abrir o software de coordenadas MouseInfo 0.1.3 (Obter as coordenadas)
    #->Obter as coordenadas para cada uma das ações
# Passo 3: Navegar e clicar no campo E-mail -> Mover o maouse ate a coordenada
    #->Incluir os comandos para que omouse mova-se ate la
# Passo 4: Apertar TAB -> 
# Passo 5: Arrastar ate ao ponto da senha e colar a mesma
# Passo 6: Apertar TAB
# Passo 7: Apertar Space
# Passo 8: Importar a biblioteca para a utomatização: PYAUTO GUI e para Gestão do Tempo: SLEEP

import pyautogui
from time import sleep

#Passo 3: Navegar e clicar no campo E-mail -> Mover o maouse ate a coordenada
pyautogui.click(x=-3079,y=728,duration=6)
# Digitar o email
pyautogui.typewrite('noe.kamuti')

# Passo 4: Apertar TAB -> 
# Acção para parecer acção humana
sleep(1)
pyautogui.press('tab')
# Digitar a senha:
pyautogui.typewrite('Se111111')
sleep(1)
# Passo 5: Apertar TAB -> 
pyautogui.press('tab')
sleep(1)
## Passo 4: Apertar TAB -> 
pyautogui.press('space')

# A automação funcionou perfeitamente.
# Para ver as possiveis teclas:
#print(pyautogui.KEYBOARD_KEYS)