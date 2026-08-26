import numpy as np
import pandas as pd

# Definindo os dados da tabela
dados = {
    'id_aluno': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'horas_estudo': [2, 3, 5, 6, 8, 9, 1, 4, 7, 10],
    'status_real': [0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
}

df = pd.DataFrame(dados)

# Parâmetros do modelo obtidos (w e b)
w = 1.19
b = -6.52

# 1. Calculando o valor de z: z = w * X_1 + b
df['valor_z'] = (w * df['horas_estudo']) + b

# 2. Calculando a Probabilidade via Função Sigmoide: P(y=1) = 1 / (1 + e^-z)
df['probabilidade'] = 1 / (1 + np.exp(-df['valor_z']))

# 3. Formatando a probabilidade para exibição em porcentagem
df['probabilidade_pct'] = (df['probabilidade'] * 100).round(1).astype(str) + '%'

# Exibindo o resultado formatado de forma limpa
tabela_resultado = pd.DataFrame({
    'ID do Aluno': df['id_aluno'],
    'Horas de Estudo (X1)': df['horas_estudo'],
    'Status Real (y)': df['status_real'],
    'Valor de z': df['valor_z'].round(2),
    'Probabilidade Calculada': df['probabilidade_pct'],
    'Probabilidade (Decimal)': df['probabilidade'].round(3)
})

print(tabela_resultado.to_string(index=False))