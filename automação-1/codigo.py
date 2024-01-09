import pyautogui
import time
import pandas
# Passo a passo do projeto

#importar o pyautogui

pyautogui.PAUSE = 0.5

#clicar - > pyautogui.click("")
#escrever - > pyautogui.write("")
#apertar uma tecla - > pyautogui.press("")

#ABRIR A ABA WINDOWS
pyautogui.press("win")
#PESQUISAR CHROME
pyautogui.write("chrome")
#PRESSIONAR ENTER
pyautogui.press("enter")
#CLICAR NO BUSCAR
time.sleep(2)
pyautogui.click(x=510, y=66)
#DIGITAR O LINK DE ACESSO
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
#PRESSIONAR ENTER
pyautogui.press("enter")
#SELECIONAR EMAIL
time.sleep(2)
pyautogui.click(x=1633, y=375)
#ESCREVER EMAIL
pyautogui.write("doria@gmail.com")
#IR PARA SENHA
pyautogui.press("tab")
#ESCREVER SENHA
pyautogui.write("FamiliaDoria10")
#SELECIONAR ENTRAR
pyautogui.press("tab")
#CLICAR EM ENTRAR
pyautogui.press("enter")

#LER A BASE DE DADOS
tabela = pandas.read_csv("produtos.csv")
print(tabela)

#SELECIONAR CADASTRO
pyautogui.click(x=1550, y=256)

#CADASTRAR OS PRODUTOS
for linha in tabela.index:
    #código
    pyautogui.write(tabela.loc[linha,"codigo"])
    pyautogui.press("tab")

    #marca
    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab")

    #tipo
    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")

    #preço
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]

    if not pandas.isna(obs):
        pyautogui.write(obs)

    #SELECIONAR O ENVIAR
    pyautogui.press("tab")

    #ENVIAR O CADASTRO
    pyautogui.press("enter")

    #SUBIR A PÁGINA
    pyautogui.scroll(5000)

    #SELECIONAR CADASTRO
    pyautogui.click(x=1550, y=256)

