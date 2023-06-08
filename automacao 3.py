from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

# Configurando o serviço do driver do Chrome
servico = Service(ChromeDriverManager().install())

# Inicializando o navegador Chrome
navegador = webdriver.Chrome(service=servico)

# Acessando o URL desejado
navegador.get('https://selenium.dunossauro.live/aula_09.html')

# Espera de 5 segundos
sleep(5)

# Clicando no elemento usando XPath
navegador.find_element('xpath','//*[@id="request"]').click()

# Espera de 10 segundos
sleep(10)

# Fechando o navegador
navegador.quit()
