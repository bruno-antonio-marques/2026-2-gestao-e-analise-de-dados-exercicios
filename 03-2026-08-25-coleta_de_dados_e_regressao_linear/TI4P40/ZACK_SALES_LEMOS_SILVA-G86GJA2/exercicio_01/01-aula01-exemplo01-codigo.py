import numpy as np
from scipy import stats


def calcular_correlacao_pearson(v_independentes_x: np.ndarray, v_dependentes_y: np.ndarray) -> tuple[float, float]:
    """Calcula o coeficiente de correlação de Pearson e o p-valor correspondente."""
    print("--- a) Coeficiente de Correlação de Pearson e Teste ---")
    coeficiente_de_correlacao_r, valor_de_p = stats.pearsonr(v_independentes_x, v_dependentes_y)

    print(f"Coeficiente de Correlação (r): {coeficiente_de_correlacao_r:.4f}")
    print(f"P-valor da correlação: {valor_de_p:.5f}")

    if ( valor_de_p < 0.05):
        print("Conclusão: Rejeitamos a Hipótese. A correlação é estatisticamente relevante a 5%.\n")
    else:
        print("Conclusão: Não rejeitamos a Hipótese.\n")
    return coeficiente_de_correlacao_r, valor_de_p


def calcular_regressao_linear(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    """Calcula os parâmetros e o teste de significância da regressão linear simples."""
    print("--- b) Modelo de Regressão Linear Simples ---")

    # Ajustando a reta de regressão e obtendo estatísticas completas
    inclinacao_reta, interceptacao, correlacao_r, valor_p, erro_padrao = stats.linregress(x, y)

    print(f"Intercepto (beta_0): {interceptacao:.4f}")
    print(f"Coeficiente Angular (beta_1): {inclinacao_reta:.4f}")
    print(f"Equação ajustada: Y_hat = {interceptacao:.4f} + {inclinacao_reta:.4f} * X")
    print(f"P-valor do coeficiente angular (teste do modelo): {valor_p:.5f}")

    if ( valor_p < 0.05):
        print("Conclusão: O modelo de regressão linear é estatisticamente significativo a 5%.")
    else:
        print("Conclusão: O modelo não é estatisticamente significativo.")

    return interceptacao, inclinacao_reta, valor_p


def funcao_principal() -> None:
    # 1. Definindo os dados
    # X: Número de horas sem dormir
    variaveis_independentes_x = np.array([8, 8, 12, 12, 16, 16, 20, 20, 24, 24])

    # Y: Número de erros
    variaveis_dependentes_y = np.array([6, 8, 6, 10, 8, 14, 12, 14, 12, 16])

    # Executando a correlação
    calcular_correlacao_pearson(variaveis_independentes_x, variaveis_dependentes_y)

    # Executando a regressão linear
    calcular_regressao_linear(variaveis_independentes_x, variaveis_dependentes_y)


if __name__ == '__main__':
    funcao_principal()