import pandas as pd
import csv

#1. Pegar conteúdo HTML a partir da URL
url = 'https://especial.valor.com.br/valor1000/2021/ranking1000maiores'
html = pd.read_html(url, match='Sede')

print(type(html))
print(html)

''' with open ('out.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(html) '''