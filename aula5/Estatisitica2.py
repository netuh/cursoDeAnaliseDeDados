import pandas as pd
from scipy import stats

# ler o arquivo csv
df1 = pd.read_csv("vacinados-2022.csv", sep=';', on_bad_lines='skip')
df2 = pd.read_csv("vacinados-2021.csv", sep=';', on_bad_lines='skip')

# selecionar a coluna desejada
coluna_A = pd.to_numeric(df1["idade"], errors='coerce')
coluna_B = pd.to_numeric(df2["idade"], errors='coerce')

mediana = coluna_A.median()

# exibir o resultado
print("Mediana:", mediana)

mediana = coluna_B.median()

# exibir o resultado
print("Mediana:", mediana)

# Realizar o teste t-test independente
t, p = stats.ttest_ind(coluna_A, coluna_B)

# Imprimir o valor de t e o valor-p
print("t =", t)
print("p =", p)

# interpretação do resultado
# alpha = 0.05
# if p > alpha:
#     print("Não há diferença significativa entre as médias das colunas (falha ao rejeitar H0)")
# else:
#     print("Há diferença significativa entre as médias das colunas (rejeitar H0)")
