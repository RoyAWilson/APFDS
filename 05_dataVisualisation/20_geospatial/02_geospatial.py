'''
Section 5
Lecture 20 - geospatial plots

Geopandas documentation: https://geopandas.org/en/stable/docs/user_guide/io.html
Much more useful than anything the tutor said in the lecture.
'''

import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
gpd.options.io_engine = "pyogrio"

# Read in the file
# Managed to work out the problems and errors with the help of the  documentation
# and experimentation.

gdf = gpd.read_file(
    r'..\..\Data_Files\StatPlanet_uk\map\map.shp', engine='pyogrio')

# Check data imported to frame
# print(gdf)

# Plot the polygons and the boudaries, make figsize 10, 10 for second plot

gdf.plot()
gdf.boundary.plot(figsize=(10, 10))

# Plot the countries of the UK with colour coding:

gdf.plot('NAME1', cmap='Accent', legend=True)

# Now plot counties of Scotland:

gdf_Scot = gdf[gdf['NAME1'] == 'Scotland']
# print(gdf_Scot)
gdf_Scot.plot()
gdf_Scot.boundary.plot()
gdf_Scot.plot('NAME2', cmap='Accent', legend=True)
# print(gdf_Scot.columns)

# # Plot whole of data with respect to the  world map
# fig = px.scatter_geo(
#     gdf, lat=gdf['geometry'].centroid.y, lon=gdf['geometry'].centroid.x)
# fig.show()
# fig.write_image(r'..\Plots\WorldGeoPlotUK.png')

# fig_street = px.scatter_mapbox(
#     gdf, lat=gdf['geometry'].centroid.y, lon=gdf['geometry'].centroid.x, color='NAME2')
# fig_street.update_layout(mapbox_style='open-street-map')
# fig_street.show()
# fig_street.write_image(r'..\Plots\WorldGeoPlotUKStreet.png')
# NB can also write figs in all the other formats as per last lecture file.
# Other styles of map exist than have been used thusfar

# Produce a density map:

fig_dense = go.Figure(go.Densitymapbox(
    lat=gdf['geometry'].centroid.y, lon=gdf['geometry'].centroid.x, radius=10))
fig_dense.update_layout(mapbox_style='open-street-map', mapbox_center_lon=0)
fig_dense.show()
fig_dense.write(r'..\Plots\WorldGeoPlotUKHeatMap.png')
