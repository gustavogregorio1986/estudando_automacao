import pandas as pd

# Caminho do arquivo Excel
caminho_arquivo = 'Modificando estrutura.xlsx'

# Ler o arquivo Excel
df = pd.read_excel(caminho_arquivo)

# Exibir o DataFrame antes da limpeza
print("DataFrame antes de remover linhas em branco:")
print(df)

# Remover linhas completamente vazias
df_limpo = df.dropna(how='all')

# Exibir o DataFrame após a limpeza
print("DataFrame após remover linhas em branco:")
print(df_limpo)

# Salvar o DataFrame limpo em um novo arquivo Excel
caminho_arquivo_limpo = 'Modificando_estrutura_limpo.xlsx'
df_limpo.to_excel(caminho_arquivo_limpo, index=False)

print(f"Arquivo limpo salvo em: {caminho_arquivo_limpo}")
