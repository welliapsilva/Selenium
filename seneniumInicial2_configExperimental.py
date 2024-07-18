#inicial para usar o selenium
from selenium import webdriver
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

#adicionando configuraçoes experimentais
chrome_options.add_experimental_option('prefs',{
 # Alterar o local padrão de download de arquivos
    'download.default_directory': 'C:\\Users\\WellingtonAS\\Downloads',
    # notificar o google chrome sobre essa alteração
    'download.directory_upgrade': True,
    # Desabilitar a confirmação de download
    'download.prompt_for_download': False,
    # Desabilitar notificações
    'profile.default_content_setting_values.notifications': 2,
    # Permitir multiplos downloads
    'profile.default_content_setting_values.automatic_downloads': 1,
       
})
# inicializando o webdriver
driver= webdriver.Chrome(options=chrome_options)#instalando as dependencias do google Chrome do computador

#navegar ate um site usando driver
driver.get('https://pt.wikipedia.org/wiki/Brasil')
input('aperte uma tecla para fechar')