from DataScience.separar_dados import separar_dados

# Separar os dados em treino e teste
X_train, X_test, y_train, y_test = separar_dados()

# Aqui você pode adicionar o código para usar os dados separados, como treinar um modelo
print(f"Treino: {X_train.shape}, Teste: {X_test.shape}")
