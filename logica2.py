import pandas as pd

# Substitua pelo seu caminho de arquivo
arquivo_excel = 'Modificando_estrutura_limpo.xlsx'

# Ler o arquivo Excel e definir a segunda linha (índice 1) como cabeçalho
dados = pd.read_excel(arquivo_excel, sheet_name='Sheet1', header=1)

# Exibir o conteúdo da planilha
print(dados)

# Exibir o total de linhas para ver se está tudo ok
print(f"Total de linhas: {len(dados)}")
