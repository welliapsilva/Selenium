from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select #usado para selecionar a itens da lista do dropdown

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600','--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(options=chrome_options)

    return driver
link= 'https://cursoautomacao.netlify.app/desafios'

driver = iniciar_driver()
driver.get(link)
driver.maximize_window()
sleep(1)
driver.execute_script("window.scrollTo(0,1500);")
dropdown= driver.find_element(By.XPATH, '//*[@id="paisesselect"]')
lista= Select(dropdown)
sleep(1)
lista.select_by_index(2)
sleep(1)
lista.select_by_index(4)
sleep(1)
lista.select_by_index(6)
sleep(1)

print('')
driver.close()