from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

# Configurando o serviço do driver do Chrome
servico = Service(ChromeDriverManager().install())

# Inicializando o navegador Chrome
navegador = webdriver.Chrome(service=servico)

# Acessando o URL desejado
navegador.get('https://selenium.dunossauro.live/aula_07_c.html')

# Espera de 3 segundos
sleep(3)

# Clicando no botão usando XPath
navegador.find_element('xpath','//*[@id="btn"]').click()

# Espera de 3 segundos
sleep(3)

# Fechando o navegador
navegador.quit()
