from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
driver.implicitly_wait(10) #faz com que para todas as requisiçoes, ele espere ate 10 segundos antes de retornar um erro
driver.get('http://google.com/flights')

sugestoes_de_voo = driver.find_elements(By.XPATH, "//div[@class='wIuJz']")

sugestoes_de_voo[0].click()
input('')
driver.close()