import pandas as pd
from scipy import stats

# Read data from CSV file
data = pd.read_csv('vacinados-2022.csv', sep=';',
                   on_bad_lines='skip', low_memory=False)

data.dropna(subset=['idade'], inplace=True)

# Split the data into two samples
# sample1 = data[data['sexo'] == 'FEMININO']['idade']
# sample2 = data[data['sexo'] == 'MASCULINO']['idade']
sample1 = data[data['raca_cor'] == 'PRETA']['idade']
sample2 = data[data['raca_cor'] == 'BRANCA']['idade']


sample1 = pd.to_numeric(sample1, errors='coerce')
sample2 = pd.to_numeric(sample2, errors='coerce')


medianaFem = sample1.median()
medianaMasc = sample2.median()
mediaPreto = sample1.mean()
mediaBranco = sample2.mean()

# exibir o resultado
print(mediaPreto)
print(mediaBranco)

# # Perform t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)

# # Print results
print("t-statistic:", t_stat)
print("p-value:", p_value)
# p-value  0.005


# Interpret results
alpha = 0.05
if p_value > alpha:
    print("Fail to reject the null hypothesis")
else:
    print("Reject the null hypothesis")
