#inicial para usar o selenium
from selenium import webdriver

# inicializando o webdriver
driver= webdriver.Chrome()#instalando as dependencias do google Chrome do computador

#navegar ate um site usando driver
driver.get('https://www.facebook.com')
input('aperte uma tecla para fechar')
