import pyautogui
import time

pyautogui.PAUSE = 0.5

# Entrar na aba windows
pyautogui.press("win")

# Escrever chrome
pyautogui.write("chrome")

# Pressionar enter
pyautogui.press("Enter")

# Clicar na aba pesquisar
pyautogui.click(x=525, y=61)

# Escrever o link
link = "https://chat.openai.com/"
pyautogui.write(link)

# Pressionar Enter
pyautogui.press("Enter")

