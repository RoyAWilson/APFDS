'''
Section 7 - Case Studies and Projects
Lecture 29 - Customr Segmentation
Using Clustering methods
'''

import datetime
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from mpl_toolkits.mplot3d import Axes3D


# Added parse_dates and dayFirst though not covered in the lecture

df = pd.read_csv(r'../Data_Files/marketing_campaign.csv',
                 sep=';', parse_dates=True, dayfirst=True)

# Basic first look at tthe data to get an idea of the shape and
# data-types of the data.

# print(df.info())
# print(df.shape)
# print(df.columns)
# print(df.isnull().sum())
# print()
# print(df.isna().sum())

# Data Cleaning
# Drop income column as only column with missing values
# and only 24 missing out of over 2000 records so safe to drop
# in this instance.

df.dropna(inplace=True)
# print(df.isnull().sum())

# Define function to return age based on year of birth:


def age(df):
    '''
    Function to reuturn age based on birth yar

    Argument:
        df - dataframe
    Variables:
        current_year - datetime type - holds the current year
        birth_year - tuple - years of birth from the dataframe
    Returns - pandas dataframe
    '''

    df = df.copy()

    current_year: datetime = datetime.datetime.now().year
    birth_years: tuple = pd.to_datetime(df['Year_Birth'], format='%Y')
    # df['Age'] = (pd.to_datetime(current_year, format='%Y') -
    #              birth_years).astype('<m8[Y]')

    # Could not get this to work as per the tutors way of doing it so found this on the internet.
    df['Age'] = (pd.to_datetime(current_year, format='%Y') -
                 birth_years)/pd.Timedelta(days=365)
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])
    # Probably overkill as have loaded with parse_dates set to True
    return df

# Call the functin on df to apply the required changes:


df = age(df)
# print(df[['Year_Birth', 'Age']].head())
# Drop uneeded columns sum up spend and drop further uneeded columns
df.drop(['Year_Birth', 'AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3',
        'AcceptedCmp4', 'AcceptedCmp5', 'Z_CostContact', 'Z_Revenue'], axis=1, inplace=True)
df['Spent'] = df['MntWines'] + df['MntFruits'] + df['MntMeatProducts'] + \
    df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds']
df.drop(['MntWines', 'MntFruits', 'MntMeatProducts',
        'MntFishProducts', 'MntSweetProducts', 'MntGoldProds'], axis=1, inplace=True)

# EDA

# plt.figure(figsize=(20, 20))

# for i, column in enumerate(df.columns[3:]):
#     plt.subplot(4, 4, i+1)
#     sns.histplot(df[column], kde=True)
#     plt.title(f'Distribution of {column}')
#     plt.savefig(r'Plots/MarketingCampaign.png')
# plt.tight_layout()
# plt.show()
# plt.close()
# for i, column in enumerate(df.columns[3:]):
#     plt.subplot(4, 4, i+1)
#     sns.boxplot(df[column])
#     plt.title(f'Distribution of {column}')
#     plt.savefig(r'Plots/MarketingCampaignBxPlt.png')
# plt.tight_layout()
# plt.show()
# plt.close()

# Drop outliers

df.drop(df[(df['Income'] > 69000)].index, inplace=True)
df.drop(df[(df['NumDealsPurchases'] > 3)].index, inplace=True)
df.drop(df[(df['NumWebPurchases'] > 3)].index, inplace=True)
df.drop(df[(df['NumStorePurchases'] > 4)].index, inplace=True)
df.drop(df[(df['NumCatalogPurchases'] > 2.5)].index, inplace=True)
df.drop(df[(df['NumWebVisitsMonth'] > 10)].index, inplace=True)
df.drop(df[(df['Complain'] > 100)].index, inplace=True)
df.drop(df[(df['Response'] > 250)].index, inplace=True)
df.drop(df[(df['Age'] > 87)].index, inplace=True)
df.drop(df[(df['Spent'] > 145)].index, inplace=True)

# Check Outliers gone
# for i, column in enumerate(df.columns[3:]):
#     plt.subplot(4, 4, i+1)
#     sns.boxplot(df[column])
#     plt.title(f'Distribution of {column}')
#     plt.savefig(r'Plots/MarketingCampaignBxPltOlRmvd.png')
# plt.tight_layout()
# plt.show()
# plt.close()
# print(df[df['Response'] > 0])
# Would be tempted to remove complaints and Response as all exactly 1 and don't actually
# add up to even 100 - complaints could be pulled out and considered
# seperately for insights.

# Plot to find the effects of marital status.  Pity we cannot know the gender
# the male/female split could provide valuable insight to marketers

# sns.countplot(data=df, x='Marital_Status')
# plt.savefig(r'Plots/MarketingMaritial.png')
# plt.title('Distribution by Marital Status')
# plt.show()
# plt.close()

# Encode textual fields with numberic code

s = df.dtypes == 'object'
object_cols = list(s[s].index)
le = LabelEncoder()
for i in object_cols:
    df[i] = df[[i]].apply(le.fit_transform)
# print(df.dtypes)
# Had to drop the date values as scaler does not support the date type
# that this column was although datetime64 is supported datetime64[ns]
# screwed it up.  Need to look at the documentation to work out why this is the case.

df.drop(['Dt_Customer'], axis=1, inplace=True)

scaler = StandardScaler()
scaler.fit(df)
scaled_ds = pd.DataFrame(scaler.transform(df), columns=df.columns)

pca = PCA(n_components=3)
pca.fit(scaled_ds)
PCA_ds = pd.DataFrame(pca.transform(scaled_ds),
                      columns=(['col1', 'col2', 'col3']))
print(PCA_ds.describe().T)

# Visualise it:

x = PCA_ds['col1']
y = PCA_ds['col2']
z = PCA_ds['col3']
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, marker='o')
plt.savefig(r'Plots/3DScatter_Mktng')
plt.show()
plt.close()

# Agglomerative Clustering.

AC = AgglomerativeClustering(n_clusters=4)
yhat_AC = AC.fit_predict(PCA_ds)
PCA_ds['Clusters'] = yhat_AC
fig_2 = plt.figure(figsize=(10, 8))
ax1 = plt.subplot(111, projection='3d', label='bla')
ax1.scatter(x, y, z, s=40, c=PCA_ds['Clusters'], marker='o', cmap='viridis')
plt.savefig(r'Plots/AggCluster_mrkt.png')
plt.show()
plt.close()

# Single clustering:

clustered_data = pd.DataFrame(df, columns=['Education'])
clustered_data['Clusters'] = yhat_AC
for cluster_num in np.unique(yhat_AC):
    cluster = clustered_data[clustered_data['Clusters'] == cluster_num]
    print(f'\nCluster {cluster_num}:\n{cluster}')
