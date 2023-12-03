'''
Sectpom 5 Data Visualisation
lecture 18 - Statical Data Visualisation - Pairplots, heatmap
with Seaborn
'''

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('iris')
# print(df)
sns.pairplot(data=df, hue='species')
# plt.savefig(r'..\Plots\Pairplot.png')
plt.show()
plt.close()

# Plot a heatmap:

# first see the correlations available
# print(df)
df = pd.DataFrame(df)
# Tutor didn't have to drop the species column.  Could be because she is using jupyter.
df_corr = df.drop('species', axis=1)
# print(df_corr.corr())

sns.heatmap(df_corr.corr(), annot=True, cmap='YlGnBu')
# plt.savefig(r'..\Plots\Heatmap.png')
plt.show()
plt.close()

# lmplot

sns.lmplot(data=df, x='petal_length', y='sepal_width',
           col='species', hue='species', palette='muted', ci=None, height=4, scatter_kws={'s': 50, 'alpha': 1})
plt.savefig(r'..\Plots\lmplot.png')
plt.show()
plt.close()
