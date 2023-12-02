'''
Section 5 Advanced Matplotlib
Lecture 17
More advanced visualisations
3D Plot
'''

import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
# Load dataset tips from seaborn

df = sns.load_dataset('tips')
# Produce an empty fig to hold the plot
fig = plt.figure()
# add to subplot position 1, 1, 1 the projection of the plot
ax = fig.add_subplot(111, projection='3d')
# Add data to the x,y and z axes:
x = df['total_bill']
y = df['tip']
z = df['size']
ax.set_xlabel('Cost')
ax.set_ylabel('Tip')
ax.set_zlabel('Covers')
ax.set_title('Tips by # covers, meal cost and tip')

# Send it the plot
ax.scatter(x, y, z, color='b', marker='h')
# Save it and show it:
plt.savefig('../Plots/3DScatter.png')
plt.show()
plt.close()
