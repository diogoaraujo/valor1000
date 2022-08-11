import pandas as pd

#1. Pegar conteúdo HTML a partir da URL
url = 'https://especial.valor.com.br/valor1000/2021/ranking1000maiores'
html = pd.read_html(url, match='Sede')

print(html)