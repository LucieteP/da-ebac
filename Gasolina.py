import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('gasolina.csv')

sns.lineplot(x='dia', y='venda', data=dados)

plt.title('Média de Venda da Gasolina')
plt.xlabel('Dias')
plt.ylabel('Preço de Venda')

plt.savefig('Gasolina.png')

plt.show()