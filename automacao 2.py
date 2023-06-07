from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get('https://selenium.dunossauro.live/aula_07_c.html')

sleep(3)

navegador.find_element('xpath','//*[@id="btn"]').click()

sleep(3)

driver.quit()
