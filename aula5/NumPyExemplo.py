import numpy as np
import matplotlib.pyplot as plt
import random


# notas = [10, 2, 3, 5, 7.5, 3, 5]
# notas = [5, 3, 3, 5, 5, 3, 5]

notas = []
for i in range(100):
    nota = random.randint(0, 10)
    notas.append(nota)

x = np.array(notas)
# mais facilmente, podemos utilizar o metodo numpy.mean
media = np.mean(x)
mediana = np.median(x)
# calcular a variância amostral
variance = np.var(x)

print("a média da notas é ", media)
print("a mediana da notas é ", mediana)
print("a variância da notas é ", variance)


# calcular o percentil 25
percentil25 = np.percentile(x, 25)

# calcular o percentil 50 (mediana)
mediana = np.percentile(x, 50)

# calcular o percentil 75
percentil75 = np.percentile(x, 75)

# exibir os resultados
print(percentil25)
print(mediana)
print(percentil75)

plt.hist(x, bins=10)
plt.title('Histograma')
plt.ylabel('Frequencia')
plt.xlabel('Nota')
plt.show()


# fig = plt.figure(figsize=(10, 7))
# # Creating plot
# plt.boxplot(x)
# # show plot
# plt.show()
