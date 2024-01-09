import time
import pandas
import pyautogui

pyautogui.PAUSE = 1

#CLICAR WINDOWS
pyautogui.press("win")

#DIGITAR CHROME
pyautogui.write("chrome")

#CLICAR NO ENTER
pyautogui.press("enter")

#CLICAR COM O MOUSE NO PESQUISAR
pyautogui.click(x=932, y=66)

#DIGITAR YOUTUBE.COM
link = "youtube.com"
pyautogui.write(link)

#CLICAR NO ENTER
pyautogui.press("enter")

#CLICAR COM O MOUSE NO CANAL
time.sleep(1)
pyautogui.click(x=3374, y=118)

#CLICAR EM ACESSAR CANAL
time.sleep(0.5)
pyautogui.click(x=3246, y=209)