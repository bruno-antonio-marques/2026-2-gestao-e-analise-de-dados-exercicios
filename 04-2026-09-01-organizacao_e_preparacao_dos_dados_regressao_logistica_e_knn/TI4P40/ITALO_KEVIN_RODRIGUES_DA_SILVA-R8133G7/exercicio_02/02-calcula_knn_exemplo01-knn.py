import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1. Carregar o dataset salvo anteriormente (ou definir a variável df_clientes)
df_clientes = pd.read_csv("clientes_supermercado_knn.csv")

# 2. Separar Atributos (X) e Rótulo (y)
X = df_clientes.drop(columns=['perfil_cliente'])
y = df_clientes['perfil_cliente']

# 3. Normalização/Padronização dos dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Treinar o KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_scaled, y)

# 5. Testar uma nova predição
# Exemplo: %_frescos, %_industrializados, preco_medio, volume, %_promocao
novo_cliente = np.array([[12, 68, 14.50, 10, 15]])
novo_cliente_scaled = scaler.transform(novo_cliente)

predicao = knn.predict(novo_cliente_scaled)
print(f"Perfil previsto para o novo cliente: {predicao[0]}")