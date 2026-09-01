import pandas as pd
import numpy as np

# Configurar semente para reprodutibilidade dos resultados na aula
np.random.seed(42)

def gerar_clientes_por_perfil(perfil, n_amostras):
    """
    Gera dados sintéticos baseados nas características de cada perfil de cliente.
    
    Atributos:
    - qtd_frescos: % de itens hortifrúti/frescos na cesta (0 a 100)
    - qtd_industrializados: % de itens ultraprocessados/congelados (0 a 100)
    - preco_medio_item: Valor médio gasto por item em R$
    - volume_total_itens: Quantidade total de itens no carrinho
    - %_itens_promocao: Porcentagem de itens comprados com desconto (0 a 100)
    """
    if perfil == "Cliente Saudável":
        frescos = np.random.normal(loc=70, scale=8, size=n_amostras)
        industrializados = np.random.normal(loc=10, scale=5, size=n_amostras)
        preco_medio = np.random.normal(loc=18, scale=3, size=n_amostras)
        volume = np.random.normal(loc=25, scale=5, size=n_amostras)
        promocao = np.random.normal(loc=15, scale=5, size=n_amostras)
        
    elif perfil == "Família Grande":
        frescos = np.random.normal(loc=30, scale=8, size=n_amostras)
        industrializados = np.random.normal(loc=45, scale=8, size=n_amostras)
        preco_medio = np.random.normal(loc=12, scale=2, size=n_amostras)
        volume = np.random.normal(loc=85, scale=12, size=n_amostras)
        promocao = np.random.normal(loc=40, scale=10, size=n_amostras)
        
    elif perfil == "Casal Jovem Gourmet":
        frescos = np.random.normal(loc=45, scale=7, size=n_amostras)
        industrializados = np.random.normal(loc=15, scale=5, size=n_amostras)
        preco_medio = np.random.normal(loc=35, scale=5, size=n_amostras)
        volume = np.random.normal(loc=20, scale=4, size=n_amostras)
        promocao = np.random.normal(loc=10, scale=4, size=n_amostras)
        
    elif perfil == "Solteiro Prático":
        frescos = np.random.normal(loc=10, scale=4, size=n_amostras)
        industrializados = np.random.normal(loc=70, scale=8, size=n_amostras)
        preco_medio = np.random.normal(loc=15, scale=3, size=n_amostras)
        volume = np.random.normal(loc=12, scale=3, size=n_amostras)
        promocao = np.random.normal(loc=20, scale=5, size=n_amostras)
        
    elif perfil == "Caçador de Ofertas":
        frescos = np.random.normal(loc=25, scale=6, size=n_amostras)
        industrializados = np.random.normal(loc=35, scale=8, size=n_amostras)
        preco_medio = np.random.normal(loc=8, scale=2, size=n_amostras)
        volume = np.random.normal(loc=35, scale=8, size=n_amostras)
        promocao = np.random.normal(loc=80, scale=8, size=n_amostras)

    df_perfil = pd.DataFrame({
        'pct_frescos': np.clip(frescos, 0, 100),
        'pct_industrializados': np.clip(industrializados, 0, 100),
        'preco_medio_item': np.clip(preco_medio, 1, None),
        'volume_total_itens': np.clip(volume, 1, None).astype(int),
        'pct_promocao': np.clip(promocao, 0, 100),
        'perfil_cliente': perfil
    })
    
    return df_perfil

# Gerar 20 amostras para cada um dos 5 perfis (Total: 100 clientes)
perfis = ["Cliente Saudável", "Família Grande", "Casal Jovem Gourmet", "Solteiro Prático", "Caçador de Ofertas"]
dfs = [gerar_clientes_por_perfil(p, n_amostras=20) for p in perfis]

# Combinar em um único DataFrame
df_clientes = pd.concat(dfs, ignore_index=True)

# Arredondar valores numéricos para melhor apresentação
df_clientes = df_clientes.round(2)

# Exibir os 5 primeiros registros e salvar em CSV
print(df_clientes.head())
df_clientes.to_csv("clientes_supermercado_knn.csv", index=False)