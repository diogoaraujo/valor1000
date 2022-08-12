import pandas as pd
import numpy as np
import lxml

#1. Pegar conteúdo HTML a partir da URL
url = 'https://especial.valor.com.br/valor1000/2021/ranking1000maiores'
html = pd.read_html(url, match ="Classificação")
print(type(html))
df = html[0]
print(type(df))


