import pandas as pd

# Substitua pelo caminho do seu arquivo
arquivo_excel = 'Modificando_estrutura_limpo.xlsx'

# Ler o arquivo Excel e definir a segunda linha como cabeçalho
dados = pd.read_excel(arquivo_excel, sheet_name='Sheet1', header=1)

# Selecionar duas colunas específicas (por exemplo, "Quantidade" e "Valor unitário")
colunas_selecionadas = dados[['Quantidade', 'Valor unitário']]

# Exibir as colunas selecionadas
print(colunas_selecionadas)
