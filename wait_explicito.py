from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait #tem que ser importado para que o wait explicito funciona
from selenium.common.exceptions import * #permite usar as excessoes dentreo do webdriver wait
from selenium.webdriver.support import expected_conditions as condicao_esperada #usado para validar a condição esperada do wait

# Iniciar o webdriver
#inserir o wait dentro do webdriver

def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=en-US', '--window-size=1300,1000',
                 '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1

    })
#deve colocar este wait dentro do webdriver pra ara qu eel possa funcionar ##as excessões podem ser vistas no domento do seleniou no site: https://selenium-python.readthedocs.io/api.html?_gl=1*wwvy6k*_ga*NTc3NDI5MjQwLjE3MTg3NTcxNjQ.*_ga_37GXT4VGQK*MTcyNDExNTU1OC41Mi4xLjE3MjQxMTk4MjguMC4wLjA.#module-selenium.common.exceptions
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait

# o waint explicito, é a forma mais garantida de interagir aguardando o tempo certo de cada elemento ficar disponivel
driver, wait = iniciar_driver() #
driver.get('https://google.com/flights')

sugestoes_de_voo = wait.until(condicao_esperada.visibility_of_all_elements_located(
    (By.XPATH, "//div[@class='wIuJz']"))) #espera que todos os elementos estejam visiveis. espera soment eo tempo necessario


# sugestoes_de_voo = wait.until(condicao_esperada.visibility_of_any_elements_located(
#     (By.XPATH, "//div[@class='wIuJz']")))

sugestoes_de_voo[0].click()


sleep(5)
##segundo exemplo:
##o exemplo abaixo verifica se seomente um elemento esepecífico esta visivel na pagina para que ele seja clicavel
driver.get('https://cursoautomacao.netlify.app/login')

campo_email = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, "//input[@id='email']")))

campo_email.send_keys('jhonatan@hotmail.com')

# sugestoes_de_voo = driver.find_elements(By.XPATH, "//div[@class='wIuJz]")

input('')
driver.close()