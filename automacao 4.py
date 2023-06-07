from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get('https://selenium.dunossauro.live/aula_10_b.html')

sleep(10)

navegador.find_element('xpath','/html/body/button').click()

sleep(5)

driver.quit()
