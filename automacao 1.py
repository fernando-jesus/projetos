from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get('https://selenium.dunossauro.live/aula_05_c.html')

sleep(4)

navegador.find_element('xpath', '/html/body/input[1]').send_keys("parasita")
navegador.find_element(
    'xpath', '/html/body/input[2]').send_keys("exemplo@hotmail.com")
navegador.find_element(
    'xpath', '/html/body/input[3]').send_keys("(099)99999-9999")
navegador.find_element('xpath', '/html/body/input[4]').click()

sleep(10)

driver.quit()





