import pandas as pd 

re = pd.read_csv('pagamentosOline.csv')

df = pd.DataFrame(re)
tipo_colunas = ()

# tipo_colunas = {'trimestre': int, 'nomeBandeira': str, 'nomeFuncao': str, 'qtdCartoesEmitidos': int, 'qtdCartoesAtivos': int, 'qtdTransacoesNacionais': int,'valorTransacoesNacionais': float }
# leitura = leitura.astype (tipo_colunas)

print(df.dtypes)
print(df)