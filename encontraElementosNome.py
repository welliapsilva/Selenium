#cogigo base para iniciar os projetos
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


#a função abaixo esta minimizada clicando na ceta a esquerda ela abre
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
nome= driver.find_element(By.NAME,'seu-nome')
rarioButtons = driver.find_elements(By.NAME,'exempleRadios')

if nome is not None:
    print('botao encontrado')
if rarioButtons is not None:
    print('botoes encontrado')


input('')
driver.close()