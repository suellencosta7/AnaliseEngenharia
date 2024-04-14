import pandas as pd 

re = pd.read_json('imdb.csv')

arquivo = re['value']

print(arquivo[0])