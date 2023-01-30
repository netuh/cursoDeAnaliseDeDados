import pandas
import math
# import matplotlib.pyplot as plt
# from matplotlib import pyplot

# from matplotlib import pyplot
dados = pandas.read_csv('vacinados-2022.csv', sep=';', on_bad_lines='skip')
dados2 = pandas.read_csv('vacinados-2021.csv', sep=';', on_bad_lines='skip')

# # exibir as primeiras linhas do arquivo

dados["idade_norm"] = pandas.to_numeric(dados["idade"], errors='coerce')
dados2["idade_norm"] = pandas.to_numeric(dados2["idade"], errors='coerce')
print(dados["idade"].head())
print(dados["idade_norm"].head())
mediana_idade = dados["idade_norm"].median()
media_idade = dados["idade_norm"].mean()
var_idade = dados["idade_norm"].var()

mediana_idade2 = dados2["idade_norm"].median()
media_idade2 = dados2["idade_norm"].mean()
var_idade2 = dados2["idade_norm"].var()


print("a mediana das idades em 2022 dos vacinados são", mediana_idade)
print("a media das idades em 2022 dos vacinados são", media_idade)
print("o devio padrão das idades em 2022 dos vacinados são", math.sqrt(var_idade))

print("a mediana das idades em 2021 dos vacinados são", mediana_idade2)
print("a media das idades em 2021 dos vacinados são", media_idade2)
print("o devio padrão das idades em 2021 dos vacinados são", math.sqrt(var_idade2))


# plt.hist(dados["idade_norm"], bins=20, range=(0, 100))
# plt.title('Histograma')
# plt.ylabel('Frequencia')
# plt.xlabel('Idade')
# plt.show()
