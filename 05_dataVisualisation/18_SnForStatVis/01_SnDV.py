'''
Sectpom 5 Data Visualisation
lecture 18 - Statical Data Visualisation
with Seaborn
'''
import seaborn as sns
import matplotlib.pyplot as plt

# x = sns.get_dataset_names()
# print(x)
# Get a dataset to work on

df = sns.load_dataset('tips')

# Interactive visualisations:
# Have added a call to plt.text to give a title to the plot.  Title didn't plece it well
# Joint plot 2 plots joined.  This example density with histogram:

sns.jointplot(x=df['total_bill'], y=df['tip'], kind='hex', color='#4CB391')
plt.text(12, 9, 'Join Plot Total Bill against Tip',
         color='Blue', fontsize=12, fontstyle='italic', fontweight='bold')
plt.savefig(r'..\Plots\BasicJoinPlot.png')
plt.show()
plt.close()

# Now add a line to both plots:

sns.jointplot(x=df['total_bill'], y=df['tip'], kind='reg', color='#4CB391')
plt.text(12, 9, 'Join Plot Total Bill against Tip',
         color='Blue', fontsize=12, fontstyle='italic', fontweight='bold')
plt.savefig(r'..\Plots\BasicJoinPlotreg.png')
plt.show()
plt.close()

# Same plot as a KDE plot

sns.jointplot(x=df['total_bill'], y=df['tip'],
              kind='kde', color='#4CB391', fill=True)
plt.text(12, 9, 'Join Plot Total Bill against Tip',
         color='Blue', fontsize=12, fontstyle='italic', fontweight='bold')
plt.savefig(r'..\Plots\BasicJoinPltKDE.png')
plt.show()
plt.close()

# Same chart with colour mapping

sns.jointplot(x=df['total_bill'], y=df['tip'],
              kind='kde', color='#4CB391', fill=True, cmap='YlGnBu')
plt.text(12, 9, 'Join Plot Total Bill against Tip',
         color='Blue', fontsize=12, fontstyle='italic', fontweight='bold')
plt.savefig(r'..\Plots\BasicJoinPltcmap.png')
plt.show()
plt.close()

# Create a dis(tribution)plot:

sns.displot(df['tip'], kde=True, bins=15)
plt.title('Distributin of Tip Amount')
plt.show()
plt.close()

# Produce a boxplot:

sns.boxplot(data=df, x='day', y='tip')
plt.savefig(r'..\Plots\Boxplot.png')
plt.show()
plt.close()

# Boxenplot

sns.boxenplot(data=df, x='day', y='tip')
plt.savefig(r'..\Plots\Boxenplot.png')
plt.show()
plt.close()

# Boxenplot with hue on sex
sns.boxenplot(data=df, x='day', y='tip', hue='sex', palette='YlGnBu')
plt.savefig(r'..\Plots\BoxenplotHuePal.png')
plt.show()
plt.close()
