import pandas as pd

# Caminho do arquivo Excel
caminho_arquivo = 'Modificando estrutura.xlsx'

# Ler o arquivo Excel
df = pd.read_excel(caminho_arquivo)

# Verificar os nomes das colunas antes da limpeza
print("Colunas disponíveis no DataFrame antes da limpeza:")
print(df.columns.tolist())

# Exibir as primeiras linhas do DataFrame
print("Primeiras linhas do DataFrame:")
print(df.head())

# Limpar espaços nos nomes das colunas
df.columns = df.columns.str.strip()

# Renomear as colunas 'Unnamed' se necessário
for col in df.columns:
    if 'Unnamed' in col:
        print(f"Coluna '{col}' parece não ter um nome. Verifique o conteúdo.")

# Verificar se a coluna 'Data' existe ou se está em uma coluna não nomeada
if 'Data' in df.columns:
    print("Conteúdo da coluna 'Data':")
    print(df['Data'])
else:
    print("A coluna 'Data' não foi encontrada. Verifique as colunas não nomeadas.")

