#inicial para usar o selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # configura opçoes do  navegacor

chrome_options = Options()
arguments= ['--lang=pt-BR','--window-size=500,500','--incognito'] #lista de argumentos da opçoes
'''os principais argmentos usados são:
--start-maximized # Inicia maximizado
--lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
--incognito # Usar o modo anônimo
--window-size=800,800 # Define a resolução da janela em largura e altura
--headless # Roda em segundo plano(com a janela fechada)
--disable-notifications # Desabilita notificações
--disable-gpu # Desabilita renderização com GPU
'''
for argument in arguments:
    chrome_options.add_argument(argument) #passa os argumentos acima para as oções do chrome

# inicializando o webdriver
driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)#instalando as dependencias do google Chrome do computador

#navegar ate um site usando driver
driver.get('https://pt.wikipedia.org/wiki/Brasil')
input('aperte uma tecla para fechar')