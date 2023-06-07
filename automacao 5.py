from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get('https://selenium.dunossauro.live/aula_10_d.html')

sleep(5)

navegador.find_element('xpath','/html/body/div/div/fieldset/form/div[1]/input').send_keys("fernando")
sleep(5)
navegador.find_element('xpath','/html/body/div/div/fieldset/form/div[2]/input').send_keys("exemplo@hotmail.com")
sleep(5)
navegador.find_element('xpath','/html/body/div/div/fieldset/form/div[3]/input').send_keys("exemplo@hotmail.com")
sleep(5)
navegador.find_element('xpath','/html/body/div/div/fieldset/form/div[4]/input').send_keys("102030")
sleep(5)
navegador.find_element('xpath','/html/body/div/div/fieldset/form/div[5]/input').send_keys("102030")
sleep(5)
navegador.find_element('xpath','/html/body/div/div/fieldset/form/input').click()

driver.quit()
