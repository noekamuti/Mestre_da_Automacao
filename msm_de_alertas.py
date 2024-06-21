# Alertar e pedir informação no PyAutoGUI

import pyautogui

# Tufas: A aula de hoje vou fazer atualização em todas aplicações, informando inicio da automação:
pyautogui.alert(text='Seja bem vindo; Iniciamos agora a sua automação',title='Automação de Varedura',button='Okay')

# Pedir informação ao usuario:
email = pyautogui.prompt(text='Digite por favor o seu e-mail:',title='Informações Obrigatórias')
print(f'Você digitou o seguinte e-mail:{email}')

'''
Observação: Noto que agora tenho maior capacidade de gerir os erros e situações adversas no codigo.
Nem tudo agora é novidade e pelo facto de estar a escrever, parece que tudo tem se tornado mais simples de ser lido.

'''