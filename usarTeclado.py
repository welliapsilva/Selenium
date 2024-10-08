from ensurepip import bootstrap
from this import d
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(options=chrome_options)

    return driver


driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')
sleep(1)

botao_windows = driver.find_element(By.ID, 'WindowsRadioButton') #clica no rariobtton e depois usa as tecals do teclad para mudar de posição
botao_windows.click() 
botao_windows.send_keys(Keys.DOWN) #neste exemplo: aperta ceta pra baixao no teclado
botao_windows.send_keys(Keys.TAB) #neste exemplo: aperta tab no teclado
botao_windows.send_keys(Keys.PAGE_DOWN) #neste exemplo: aperta page down no teclado

input('')
driver.close()