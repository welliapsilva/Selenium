from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e  https://peter.sh/experiments/chromium-command-line-switches/
chrome_options = Options() #configura as oções conforme descritas abaixo(os argumentos comentatos abaixo são os mais comuns utilizados)
'''
--start-maximized # Inicia maximizado
--lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
--incognito # Usar o modo anônimo
--window-size=800,800 # Define a resolução da janela em largura e altura
--headless # Roda em segundo plano(com a janela fechada)
--disable-notifications # Desabilita notificações
--disable-gpu # Desabilita renderização com GPU
'''
arguments = ['--lang=pt-BR', '--window-size=500,500', '--incognito'] # mais explicações no comentario acima(explicando o que pose ser usado para cada argumento)
for argument in arguments: #função que passa os argumentos pras o chrome_options
    chrome_options.add_argument(argument)

# Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
# Uso de configurações experimentais # elas alteram coisas do google chrome
chrome_options.add_experimental_option('prefs', {
    # Alterar o local padrão de download de arquivos
    'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
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
driver = webdriver.Chrome(options=chrome_options)
# Navegar até um site
driver.get('https://pt.wikipedia.org/wiki/Brasil')

input('aperta uma tecla para fechar')