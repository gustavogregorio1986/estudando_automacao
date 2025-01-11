import pandas as pd

# Substitua 'seu_arquivo.xlsx' pelo caminho do seu arquivo Excel
arquivo_excel = 'Modificando_estrutura_limpo.xlsx'

# Ler todas as planilhas do Excel
todas_planilhas = pd.read_excel(arquivo_excel, sheet_name=None)

# Iterar por todas as planilhas e exibir os dados
for nome_planilha, dados in todas_planilhas.items():
    print(f"\n--- Conteúdo da Planilha: {nome_planilha} ---\n")
    print(dados)
