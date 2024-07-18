from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
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
driver.get('https://cursoautomacao.netlify.app/desafios.html')
driver.maximize_window()
sleep(2)
botao1 = driver.find_element(By.XPATH,'//*[@id="btn1"]')
botao2= driver.find_element(By.XPATH,'/html/body/section[1]/button[2]')
botao3= driver.find_element(By.XPATH,'/html/body/section[1]/button[3]')

if botao1.is_enabled():
    print('botao habilitato')

if botao1.is_enabled() == False:
    print('botao desabilitado')

if botao2.is_enabled():
    print('botao habilitato')

if botao2.is_enabled() == False:
    print('botao desabilitado')

if botao3.is_enabled():
    print('botao habilitato')

if botao3.is_enabled() == False:
    print('botao desabilitado')
    
input('')
driver.close()