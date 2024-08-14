from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
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
driver.get('https://cursoautomacao.netlify.app/desafios')
# 1) Salvar nossa janela atual
janela_ini = driver.current_window_handle
print(f'primeira janela: {janela_ini}') # mostrar a primeira janela so apra conferencia
# 2) Abrir um nova janela
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)
abrir_nova = driver.find_element(
    By.XPATH, "/html/body/section[7]/button") #localiza o botao de abrir a janela
sleep(1)
driver.execute_script('arguments[0].click()', abrir_nova) #forma paliativa de clicar para abrir a janela caso a forma comuma não abra
sleep(1)
# 3) quais janelas estão abertas
janelas = driver.window_handles
for janela in janelas:
    print(janela)
    if janela not in janela_ini: #verifica se a janela se a janela atual não é a incial se não for abra a outra janela
        # alterar para essa nova janela
        driver.switch_to.window(janela)
        sleep(2)
        campo_opiniao = driver.find_element(By.XPATH, '//*[@id="opiniao_sobre_curso"]')
        sleep(2)
        campo_opiniao.send_keys('eu estou gostando muito deste curso')
        sleep(2)
        botao_pesquisar = driver.find_element(By.XPATH, '//*[@id="fazer_pesquisa"]')
        sleep(2)
        botao_pesquisar.click()
        driver.close()
driver.switch_to.window(janela_ini)
sleep(1)
comentario= driver.find_element(By.XPATH,'//*[@id="campo_desafio7"]')
sleep(1)
comentario.send_keys('Desafio mudar de janela')
sleep(1)

input('')
driver.close()