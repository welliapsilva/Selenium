from tkinter import Radiobutton
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


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
driver.get('https://cursoautomacao.netlify.app/')

titulo_do_site = driver.find_element(By.TAG_NAME, 'img')
elementos_h4 = driver.find_elements(By.TAG_NAME, 'h4')

if titulo_do_site:
    print('Encontrei o título do site')
if elementos_h4:
    print('Encontrei os elementos h4')

input('')
driver.close()