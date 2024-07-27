import openpyxl.workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

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
sleep(1)
carro= driver.find_elements(By.XPATH,'/html/body/section[5]/div//input')
carro[1].click()
carro[3].click()
carro[4].click()
sleep(1)

motos= driver.find_elements(By.XPATH,'//input[@name = "motos"]')
for moto in motos:
    moto.click()
sleep(3)

print('')
driver.close()