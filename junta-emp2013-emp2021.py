import pandas as pd

emp2013=pd.read_excel('valor1000-2013.xlsx')
emp2021=pd.read_excel('valor1000-2021.xlsx')

#faz um merge para unir as tabelas
#Empresas de 2013 que não constam em 2021 e vice-versa
junta= emp2013.merge(emp2021,how='outer', on='Empresa')

#salva no excel
junta.to_excel('valor1000junta-2013-2021.xlsx', sheet_name="Sheet1")
