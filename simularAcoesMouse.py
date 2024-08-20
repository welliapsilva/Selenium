from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver import ActionChains #usado para mexer nas movimentações do teclado
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
#exeplo 1
driver.get('https://cursoautomacao.netlify.app/exemplo_chains')

# ActionChains(sequencia de passos)
botao = driver.find_element(By.ID, 'botao-direito')
chain = ActionChains(driver) #após realizar este passo ira receber as ações
chain.context_click(botao).pause(3).send_keys(Keys.DOWN).pause(3).send_keys(
    Keys.DOWN).pause(3).send_keys(Keys.DOWN).pause(3).click().perform()

#exemplo 2 ##não rodar oe exeplos juntos, comentar um para executar o outro
driver.get('https://cursoautomacao.netlify.com/')
window_10_radio_button = driver.find_element(By.ID, 'WindowsRadioButton')
chain2 = ActionChains(driver)
chain2.click(window_10_radio_button).pause(3).send_keys(
    Keys.DOWN).pause(3).send_keys(Keys.UP).click().perform()
input('')
driver.close()