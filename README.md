# 🏠 Análise de Dados de Aluguel de Imóveis com Python

Este projeto realiza uma análise de um dataset de preços de aluguel de imóveis, utilizando a linguagem Python e as bibliotecas pandas, matplotlib, seaborn e scikit-learn. O objetivo é explorar, limpar e visualizar os dados, além de dividir o dataset em conjuntos de treino e teste para futuras análises preditivas.

# 🎯 Objetivo do Dataset

O dataset contém informações sobre imóveis disponíveis para aluguel e possui as seguintes colunas:

preco: Preço do aluguel em reais.
tipo: Tipo do imóvel (casa, apartamento, etc.).
area: Área do imóvel em metros quadrados.
quartos: Quantidade de quartos no imóvel.
bairro: Localização (região administrativa) do imóvel.

# 📁 Estrutura do Projeto

O projeto é dividido nas seguintes etapas:

### 1. Carregar o Dataset
Nesta etapa, o arquivo CSV é carregado utilizando a biblioteca pandas. O dataset é inspecionado para garantir que todas as colunas tenham sido carregadas corretamente.

### 2. Tratamento de Colunas e Linhas
Realiza-se uma verificação para identificar e tratar dados ausentes ou inválidos. Colunas com tipos de dados incorretos, como a coluna area, que pode estar como texto ao invés de número, são ajustadas. Além disso, são removidas duplicatas ou linhas sem informações relevantes.

### 3. Análise Gráfica dos Dados
Nesta etapa, utilizamos as bibliotecas matplotlib e seaborn para gerar gráficos que nos ajudem a entender melhor os dados. Exemplos de gráficos incluem:

Histograma para visualizar a distribuição dos preços de aluguel.
Gráfico de Dispersão para analisar a relação entre a área e o preço de aluguel.
Boxplot para visualizar a distribuição do preço de aluguel por tipo de imóvel.

### 4. Separação dos Dados em Conjuntos de Treino e Teste

Aqui, os dados são divididos em conjuntos de treino (70%) e teste (30%) utilizando a função train_test_split da biblioteca scikit-learn. Isso é importante para preparar os dados para futuras análises preditivas.

# 🛠 Instalação

Para executar este projeto, você precisará instalar as seguintes bibliotecas:

```bash
    pip install pandas matplotlib seaborn scikit-learn
```

# 🚀 Como Executar

Certifique-se de ter o arquivo CSV no mesmo diretório do script Python.
Execute o arquivo principal Python que contém as quatro etapas descritas:

```bash
    python analise_dados.py
```

# 📊 Saídas esperadas:

Visualizações gráficas dos dados.
Informações sobre a divisão dos dados em treino e teste.

# ⚠️ Observações

Este README foi desenvolvido para um script único contendo todas as etapas do processo. Se desejar separar as etapas em arquivos diferentes (como recomendado), o README será ajustado conforme as novas separações.


## Autores

- [@BarrosWesley](https://www.https://github.com/BarrosWesley)
- [DataSetKeggle](https://www.kaggle.com/datasets/matheusnbrega/preo-do-aluguel-de-imveis-no-distrito-federal)
