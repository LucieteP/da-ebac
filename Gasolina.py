import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('gasolina.csv')

sns.lineplot(x='dia', y='venda', data=dados)

plt.title('Preço Médio de Venda da Gasolina')
plt.xlabel('Dias')
plt.ylabel('Preços')

plt.savefig('Gasolina.png')

plt.show()