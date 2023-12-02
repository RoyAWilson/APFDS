'''
Section 5 Advanced Matplotlib
Lecture 17
More advanced visualisations
'''

import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset tips from seaborn
df = sns.load_dataset('tips')

plt_scatter = plt.scatter(
    x=df['total_bill'], y=df['tip'], marker='h', s=100, alpha=0.5, c='green', edgecolors='black')
plt.title('Tips by Meal Cost')
plt.xlabel('Total Bill')
plt.ylabel('Tip Given')
plt.savefig('../Plots/BillVsTipsAdv1.png')
plt.show()
plt.close()

# Changing the grid:

plt_scatter = plt.scatter(
    x=df['total_bill'], y=df['tip'], marker='h', s=100, alpha=0.5, c='green', edgecolors='black')
plt.grid(visible=True, linestyle='--', alpha=0.5)
plt.title('Tips by Meal Cost')
plt.xlabel('Total Bill')
plt.ylabel('Tip Given')
plt.savefig('../Plots/BillVsTipsAdv2Grid.png')
plt.show()
plt.close()

# Subplot:

fig, axes = plt.subplots(2, 2, figsize=(8, 6))
plt.subplot(2, 2, 1)
plt.bar(df['day'], df['total_bill'])
plt.title('Tip by Week Day')
plt.xlabel('Day of week')
plt.ylabel('Total Bill', labelpad=2)
plt.subplot(2, 2, 2)
plt.scatter(x=df['total_bill'], y=df['tip'], marker='h',
            s=100, alpha=0.5, c='green', edgecolors='black')
plt.title('Tips by Meal Cost')
plt.ylabel('Tip Given')
plt.subplot(2, 2, 3)
plt.bar(df['smoker'], df['tip'])
plt.title('Tips Smoker vs Non-Smoker')
plt.subplot(2, 2, 4)
plt.bar(df['sex'], df['tip'])
plt.title('Tips by Gender')
plt.savefig('../Plots/BasicMultiplot.png')
plt.show()
plt.close()

# Adding text:

plt_scatter = plt.scatter(
    x=df['total_bill'], y=df['tip'], marker='h', s=100, alpha=0.5, c='green', edgecolors='black')
plt.grid(visible=True, linestyle='--', alpha=0.5)
plt.annotate('Min Value', xy=(3, 1), xytext=(1, 3), fontsize=12,
             arrowprops=dict(arrowstyle='->', color='blue'))
plt.title('Tips by Meal Cost')
plt.xlabel('Total Bill')
plt.ylabel('Tip Given')
plt.text(50, 9.5, 'max value', fontsize=12, color='blue')
plt.savefig('../Plots/PlotWithText.png')
plt.show()
plt.close()
