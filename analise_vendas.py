import pandas as pd
import matplotlib.pyplot as plt

# Carregar CSV
df = pd.read_csv("data/vendas.csv")

# Criar coluna de faturamento
df["faturamento"] = df["quantidade"] * df["preco"]

# 1 — Faturamento total
print("📌 Faturamento total:", df["faturamento"].sum())

# 2 — Faturamento por produto
faturamento_produto = df.groupby("produto")["faturamento"].sum()
print("\n📌 Faturamento por produto:\n", faturamento_produto)

# 3 — Vendas por dia (gráfico)
vendas_dia = df.groupby("data")["faturamento"].sum()

plt.figure(figsize=(10,5))
vendas_dia.plot(kind="line")
plt.title("Faturamento por Dia")
plt.xlabel("Data")
plt.ylabel("R$ Faturamento")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4 — Produto mais vendido
produto_mais_vendido = df.groupby("produto")["quantidade"].sum().sort_values(ascending=False)
print("\n📌 Produto mais vendido:\n", produto_mais_vendido)
