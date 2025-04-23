import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("importacoes.csv", parse_dates=["Data_Pedido", "Data_Entrega"])

# Converter datas
df["Tempo_Total"] = (df["Data_Entrega"] - df["Data_Pedido"]).dt.days

# KPIs principais
print("Tempo médio de entrega:", df["Tempo_Total"].mean(), "dias")
print("Custo médio por embarque: R$", round(df["Custo_Total"].mean(), 2))
print("Percentual de entregas com atraso:", round((df["Atraso_Dias"] > 0).mean() * 100, 2), "%")

# Gráfico: Atraso médio por fornecedor
atrasos = df.groupby("Fornecedor")["Atraso_Dias"].mean().sort_values()
atrasos.plot(kind="barh", title="Atraso Médio por Fornecedor", color="skyblue")
plt.xlabel("Dias de Atraso")
plt.tight_layout()
plt.show()
