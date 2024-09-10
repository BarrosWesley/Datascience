import pandas as pd
from sklearn.model_selection import train_test_split

# Função para carregar o dataset e separar em treino e teste
def separar_dados():
    # Carregar o dataset a partir de um arquivo CSV
    df = pd.read_csv('TrabalhoFinal(python)/imoveisDF.csv')

    # Definir as features (variáveis preditoras) e a target (variável alvo)
    X = df[['area', 'quartos', 'tipo', 'bairro']]  # Variáveis independentes
    y = df['preco']  # Variável dependente (alvo)

    # Separar em treino (70%) e teste (30%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Retornar os dados separados
    return X_train, X_test, y_train, y_test

# Código para testar a função (executado apenas se rodar o script diretamente)
if __name__ == "__main__":
    X_train, X_test, y_train, y_test = separar_dados()
    print(f"Tamanho do conjunto de treino: {len(X_train)}")
    print(f"Tamanho do conjunto de teste: {len(X_test)}")
