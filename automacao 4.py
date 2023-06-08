from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

# Configurando o serviço do driver do Chrome
servico = Service(ChromeDriverManager().install())

# Inicializando o navegador Chrome
navegador = webdriver.Chrome(service=servico)

# Acessando o URL desejado
navegador.get('https://selenium.dunossauro.live/aula_10_b.html')

# Espera de 10 segundos
sleep(10)

# Clicando no botão usando XPath
navegador.find_element('xpath','/html/body/button').click()

# Espera de 5 segundos
sleep(5)

# Fechando o navegador
navegador.quit()
