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


driver = iniciar_driver()
# navegar até o site
driver.get('https://cursoautomacao.netlify.app')

#clicar em login
login= driver.find_element(By.XPATH,'//*[@id="navbarsExample04"]/ul[2]/li[3]/a')
login.click()
sleep(1)
#clciar em e-mail
email= driver.find_element(By.XPATH,'//*[@id="email"]')
email.send_keys('teste@teste.com')
sleep(1)

#concontrar campo senha
senha= driver.find_element(By.XPATH,'//*[@id="senha"]')
senha.send_keys('12345')
sleep(1)

#clicar em logar
clogin= driver.find_element(By.XPATH,'/html/body/section/form/div/button')
clogin.click()

input('')
driver.close()