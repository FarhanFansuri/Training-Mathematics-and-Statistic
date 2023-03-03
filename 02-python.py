import pandas as pd
import numpy as np

data = pd.read_excel('data.xlsx')

#Mencar perecntile untuk remove outliers
#interpolation?
print(data.income.quantile(0.99))

#remove outliers
data_new = data[data.income <  data.income.quantile(0.99)]

# mengganti nilai na
data.fillna(data.income.mean())

#tampilkan data
print(data_new)

