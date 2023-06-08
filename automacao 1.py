from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

# Configurando o serviço do driver do Chrome
servico = Service(ChromeDriverManager().install())

# Inicializando o navegador Chrome
navegador = webdriver.Chrome(service=servico)

# Acessando o URL desejado
navegador.get('https://selenium.dunossauro.live/aula_05_c.html')

# Espera de 4 segundos
sleep(4)

# Preenchendo o primeiro campo de entrada com o valor "parasita"
navegador.find_element('xpath', '/html/body/input[1]').send_keys("parasita")

# Preenchendo o segundo campo de entrada com o valor "exemplo@hotmail.com"
navegador.find_element('xpath', '/html/body/input[2]').send_keys("exemplo@hotmail.com")

# Preenchendo o terceiro campo de entrada com o valor "(099)99999-9999"
navegador.find_element('xpath', '/html/body/input[3]').send_keys("(099)99999-9999")

# Clicando no quarto botão
navegador.find_element('xpath', '/html/body/input[4]').click()

# Espera de 10 segundos
sleep(10)

# Fechando o navegador
navegador.quit()
