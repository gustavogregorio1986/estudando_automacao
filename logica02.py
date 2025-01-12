import pandas as pd

# Substitua pelo caminho do seu arquivo
arquivo_excel = 'Modificando_estrutura_limpo.xlsx'

# Ler o arquivo Excel e definir a segunda linha como cabeçalho
dados = pd.read_excel(arquivo_excel, sheet_name='Sheet1', header=1)

# Selecionar uma coluna específica (por exemplo, "Produto")
coluna_produto = dados['Produto']

# Exibir a coluna
print(coluna_produto)
