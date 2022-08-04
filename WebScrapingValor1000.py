import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

#1. Pegar conteúdo HTML a partir da URL

url = "https://especial.valor.com.br/valor1000/2021/ranking1000maiores"

option = Options()
option.headless = True
#driver = webdriver.Firefox(executable_path=r'C:\usr\local\bin\geckodriver.exe')
driver = webdriver.Firefox()
#driver = webdriver.Firefox(options=option)


driver.get(url)
time.sleep(10)

''' driver.find_element_by_xpath(
    "/html/body/div[5]/div[1]/div[3]/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[1]/p").click() '''

element = driver.find_element_by_xpath("//html/body/div[5]/div[1]/div[3]/div/div/div/div[2]")
#html_content = element.get_attribute("//div[@class='tabelao']")
html_content = element.get_attribute("html_content")
#2. Parsear o conteúdo HTML - BeautfulSoup
soup = bs4.BeautifulSoup(html.text)
#table =soup.find(name='tabelao')

#3. Estruturar o conteúdo em um Data Frame - Pandas
#4. Transformar os Dados em um Dicionário de dados próprio
driver.quit()
#5. Converter e salvar em um arquivo JSON