import pandas as pd

# Substitua pelo caminho do seu arquivo
arquivo_excel = 'Modificando_estrutura_limpo.xlsx'

# Ler o arquivo Excel e definir a segunda linha como cabeçalho
dados = pd.read_excel(arquivo_excel, sheet_name='Sheet1', header=1)

# Calcular o somatório e a média da coluna "Quantidade"
somatorio_quantidade = dados['Quantidade'].sum()
media_quantidade = dados['Quantidade'].mean()

# Exibir os resultados
print(f"Somatório da coluna 'Quantidade': {somatorio_quantidade}")
print(f"Média da coluna 'Quantidade': {media_quantidade}")
