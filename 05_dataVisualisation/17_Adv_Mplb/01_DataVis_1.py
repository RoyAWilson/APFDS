'''
Section 5 Advanced Matplotlib
Lecture 17
Basic Visualisations
'''

import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset tips from seaborn
df = sns.load_dataset('tips')
# print(df)
# First Plot will be a scatter plot - a very simple scatter plot,
# it is hardly using any of the bsst of pyplot.

plt_scatter = plt.scatter(x=df['total_bill'], y=df['tip'],)
plt.title('Tips by Meal Cost')
plt.xlabel('Total Bill')
plt.ylabel('Tip Given')
plt.savefig('../Plots/BillVsTips.png')
plt.show()
plt.close()

# Simple barplot:

plt.bar(df['day'], df['total_bill'])
plt.title('Cost by Week Day')
plt.xlabel('Day of Week')
plt.ylabel('Total Bill')
plt.savefig('../Plots/CostOverWeekday.png')
plt.show()
plt.close()
