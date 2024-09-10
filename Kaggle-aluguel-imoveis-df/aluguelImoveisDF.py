"""
Este dataset contém informações sobre o preço de aluguel de imóveis em diversas regiões do Distrito Federal. 
Colunas:
- 'preco': Preço do aluguel em reais
- 'tipo': Tipo do imóvel (ex.: apartamento, casa)
- 'area': Área do imóvel em metros quadrados
- 'quartos': Quantidade de quartos no imóvel
- 'bairro': Região administrativa onde o imóvel está localizado
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Carregar o dataset
dataSete = 'TrabalhoFinal(python)/imoveisDF.csv' 
df = pd.read_csv(dataSete, delimiter=';')  # Caso o delimitador seja ponto e vírgula

#print(df.info)
#print(df.head())

'''######################## Analisando valores nulos ########################## '''
#print(df.isnull().sum())
#registros_nulos = df[df.isnull().any(axis=1)] # retorna uma série booleana onde True indica que a linha contém pelo menos um valor nulo.
#print(registros_nulos) #Não foi encontrado registros nulos 
df = df.dropna()

'''####################### Verificar se há duplicatas ########################## '''
#print(df.duplicated().sum())
#registros_duplicados = df[df.duplicated()]
# print(registros_duplicados) # Foram encontrados 433 registros duplicados
#df = df.drop_duplicates() # Não se fez necessário remover registos duplicados por que é um comparativo de imóveis com mesma características

'''######## Convertendo a coluna 'area' para tipo numérico ############## '''
df['area'] = pd.to_numeric(df['area'], errors='coerce') # transforma valores inválidos em NaN

# Verificar novamente valores nulos após conversão
#print(df.isnull().sum())
#registros_nulos = df[df.isnull().any(axis=1)] 
#print(registros_nulos)
df = df.dropna()  # Considerei 12 imoveis Ruarais como outliers  e os deletei
#print("Após a remoção:")
#print(df.isnull().sum())

# Exibir informações gerais sobre o dataset
#print(df.info())


''' Código Principal'''

# Exemplo: Distribuição dos preços de aluguel com histograma 
plt.figure(figsize=(8, 6))
sns.histplot(df['preco'], bins=20, kde=True)  # kde=True adiciona a linha de densidade
plt.title('Distribuição dos Preços de Aluguel')
plt.show()

# Exemplo: Gráfico de dispersão entre área e preço do aluguel
plt.figure(figsize=(8, 6))
sns.scatterplot(x='area', y='preco', data=df)
plt.title('Área vs Preço do Aluguel')
plt.show()

# Exemplo: Boxplot do preço de aluguel por tipo de imóvel
plt.figure(figsize=(8, 6))
sns.boxplot(x='tipo', y='preco', data=df)
plt.title('Preço do Aluguel por Tipo de Imóvel')
plt.show()


''' Separar os Arquivos de Treino e Teste'''

# Definir as colunas de features e o target (preço de aluguel)
X = df[['area', 'quartos', 'tipo', 'bairro']]  # Exemplo de features
y = df['preco']  # Target (preço do aluguel)

# Realizar a divisão de treino e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"Tamanho do conjunto de treino: {len(X_train)}")
print(f"Tamanho do conjunto de teste: {len(X_test)}")
