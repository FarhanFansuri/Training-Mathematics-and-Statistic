import pandas as pd

#import data
data = pd.read_csv('AB_NYC_2019.csv')

# # check Column
print(data.price.mean())
data.price.fillna(data.price.mean())

# print(data['price'].quantile(0.99, interpolation="higher"))
print(data[data.price < data.price.quantile(0.9, interpolation="lower")])
