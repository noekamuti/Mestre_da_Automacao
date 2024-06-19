# Como movimentar, clicar e zerar um jogo com PyAutoGUI
import pyautogui

#   Posição algo - use o mouse info: python
#   From mouseinfo import mouseInfo
#   mouseInfo()
#   Fazer algo com a posição:
#   pyautogui.moveTo(1779,68,duration=5)
#   pyautogui.move(-80,0,duration=5)

pyautogui.moveTo(564,548,duration=5)
for i in range(500):
    pyautogui.click()

