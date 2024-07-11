#inicial para usar o selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# inicializando o webdriver
driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))#instalando as dependencias do google Chrome do computador

#navegar ate um site usando driver
driver.get('https://www.facebook.com')
input('aperte uma tecla para fechar')
