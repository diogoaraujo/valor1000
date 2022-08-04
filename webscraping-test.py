import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd

#1. Pegar conteúdo HTML a partir da URL
http = requests.get("https://especial.valor.com.br/valor1000/2021/ranking1000maiores")    
# soup = BeautifulSoup(http.content, 'xml')
if http.status_code == 200:
    print("Success")
    content = http.content

soup = BeautifulSoup(content, 'html.parser')
tabela =soup.find("div", class_="tabelao")
table_str = str(tabela)

df = pd.read_html(table_str)[0]
display(df)

print(tabela)