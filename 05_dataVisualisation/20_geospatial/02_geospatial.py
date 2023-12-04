'''
Section 5
Lecture 20 - geospatial plots
'''

import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

gdf = gpd.read_file(r'..\..\Data_Files\GBR_adm0.shp')

# Data not loading correctly giving errors.  Look into later.
