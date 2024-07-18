from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


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
#radio button é diferente de checkbox, ele é um campo que so da pra marcar um por vez

driver = iniciar_driver()
# navegar até o site
driver.get('https://cursoautomacao.netlify.app')
linux_radio_button = driver.find_element(By.ID, 'LinuxRadioButton')#selecionou somente um elemento
if linux_radio_button.is_selected() == True:#verifica se o botao já est amarcado antes de clicar
    print('botão já está selecionado')
sleep(1)
linux_radio_button.click()
sleep(5)
radios = driver.find_elements(By.XPATH, "//input[@type='radio']")#contra aqui vários
sleep(1)
radios[1].click()#precisa informa o indice do botao que deseja, lembrando que o indice começa do 0

input('')
driver.close()