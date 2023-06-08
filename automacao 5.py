from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

# Configurando o serviço do driver do Chrome
servico = Service(ChromeDriverManager().install())

# Inicializando o navegador Chrome
navegador = webdriver.Chrome(service=servico)

# Acessando o URL desejado
navegador.get('https://selenium.dunossauro.live/aula_10_d.html')

# Espera de 5 segundos
sleep(5)

# Preenchendo o primeiro campo de entrada com o valor "fernando"
navegador.find_element('xpath','/html/body/div/div/fieldset/form/div[1]/input').send_keys("fernando")

# Espera de 5 segundos
sleep(5)

# Preenchendo o segundo campo de entrada com o valor "exemplo@hotmail.com"
navegador.find_element('xpath','/html/body/div/div/fieldset/form/div[2]/input').send_keys("exemplo@hotmail.com")

# Espera de 5 segundos
sleep(5)

# Preenchendo o terceiro campo de entrada com o valor "exemplo@hotmail.com"
navegador.find_element('xpath','/html/body/div/div/fieldset/form/div[3]/input').send_keys("exemplo@hotmail.com")

# Espera de 5 segundos
sleep(5)

# Preenchendo o quarto campo de entrada com o valor "102030"
navegador.find_element('xpath','/html/body/div/div/fieldset/form/div[4]/input').send_keys("102030")

# Espera de 5 segundos
sleep(5)

# Preenchendo o quinto campo de entrada com o valor "102030"
navegador.find_element('xpath','/html/body/div/div/fieldset/form/div[5]/input').send_keys("102030")

# Espera de 5 segundos
sleep(5)

# Clicando no botão usando XPath
navegador.find_element('xpath','/html/body/div/div/fieldset/form/input').click()

# Fechando o navegador
navegador.quit()
