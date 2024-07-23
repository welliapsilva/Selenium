from tabnanny import check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random #faz gerar valor aleatorio


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,1000', '--incognito']
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


def digitar_naturalmente(texto, elemento): #função para digirar com pausas aleatorias
    for letra in texto: #para cada letra no texto
        elemento.send_keys(letra) #escrever letra
        sleep(random.randint(1, 5)/30) #determinando velocidade da letra entre 1 a 5 segundos dividido por 30


# navegar até o site
driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(1)
driver.execute_script("window.scrollTo(0,500);")
sleep(1)

desafio4 = driver.find_element(By.XPATH, '//*[@id="campoparagrafo"]')
texto = """hoje eu te digo amigo, que vc é muito importante para Deus e para mim. Saude e um grande abraço. """
digitar_naturalmente(texto,desafio4)
input('')
driver.close()