import pandas as pd

emp2013=pd.read_excel('valor1000-2013.xlsx')
emp2021=pd.read_excel('valor1000-2021.xlsx')

compara= emp2013.compare(emp2021, keep_shape=True, keep_equal=True)

compara.to_excel('valor1000compara-2013-2021.xlsx', sheet_name="Sheet1")

