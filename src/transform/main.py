import pandas as pd
import sqlite3 

dados = pd.read_json('C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\Python-projetos\\pipelinePython\\data\\data.json')


dados['Preço'] = dados['Preço'].astype(str).str.replace('.', '', regex=False)
dados['Quantidade de avaliações'] = dados['Quantidade de avaliações'].astype(str).str.extract(r'\((\d+)\)').fillna(0).astype(int)

dados ['Preço'] = dados['Preço'].astype(float)
dados ['Número de classificação da revisão'] = dados['Número de classificação da revisão'].astype(float)

#dados = dados[(dados['Preço'] >= 1000 & dados['Preço'] <= 10000)]
dados = dados[(dados['Preço'] >= 1000) & (dados['Preço'] <= 10000)]

dados.to_excel('C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\Python-projetos\\pipelinePython\\data\\dados.xlsx', index=False)
print(dados)