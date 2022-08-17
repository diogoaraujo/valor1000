import pandas as pd
import numpy as np
import lxml

#1. Pegar conteúdo HTML a partir da URL
url = 'https://especial.valor.com.br/valor1000/2021/ranking1000maiores'
part1 = pd.read_html(url, match = '')
part2 = pd.read_html(url, match = 'Sede')

df1 = part1[0]
df2 = part2[0]

# Organiza os DataFrames lado a lado
df_stack = pd.concat([df1, df2], axis=1)

df_stack.to_excel("valor1000-2021.xlsx", sheet_name="Sheet1")
