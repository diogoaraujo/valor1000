import sys
import pandas as pd
import numpy as np
import lxml
from urllib.parse import urlparse


f=2013
l=2021
while f<=l:
    #1. Pegar conteúdo HTML a partir da URL
    url = f'https://especial.valor.com.br/valor1000/{f}/ranking1000maiores'


    part1 = pd.read_html(url, match = '')
    part2 = pd.read_html(url, match = 'Sede')

    df1 = part1[0]
    df2 = part2[0]

    # Organiza os DataFrames lado a lado
    df_stack = pd.concat([df1, df2], axis=1)

    df_stack.to_excel(f'valor1000-{f}.xlsx', sheet_name="Sheet1")

    f=f+1