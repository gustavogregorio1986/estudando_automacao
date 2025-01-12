import pandas as pd

# Substitua pelo caminho do seu arquivo
arquivo_excel = 'Modificando_estrutura_limpo.xlsx'

# Ler o arquivo Excel e definir a segunda linha como cabeçalho
dados = pd.read_excel(arquivo_excel, sheet_name='Sheet1', header=1)

# Filtrar as linhas onde a coluna 'Produto' começa com a letra 'A'
# Filtrar as linhas onde a coluna 'Produto' começa com a letra 'A' após remover espaços
linhas_comeca_com_a = dados[dados['Produto'].str.strip().str.startswith('A', case=False, na=False)]


# Exibir as linhas encontradas
print(linhas_comeca_com_a)
