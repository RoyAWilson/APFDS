'''
Sectpom 5 Data Visualisation
lecture 19 - Interactive plots with plotly
https://plotly.com/graphing-libraries/
Note saving the image requires kaleido to be installed.
Saved images are obviously not interactive.
'''

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.offline import iplot
import plotly.graph_objects as go

df = sns.load_dataset('tips')

# Plot the graph - arg size='size' set size of points relative to value of size field.

# fig = px.scatter(df, x='total_bill', y='tip', size='size',
#                  color='sex', hover_name='sex', size_max=20)
# fig.write_image(r'..\Plots\plotlyPlot.png')
# fig.show()

# Create density heatmap

# figpx = px.density_heatmap(data_frame=df, x='total_bill',
#                            y='tip', marginal_x='histogram', marginal_y='histogram')
# figpx.write_image(r'..\Plots\plotlyHeatHistoPlot.png')
# # Saving as html retains details on hover in plot
# figpx.write_html(r'..\Plots\plotlyHeatHistoPlot.html')
# # Saving as Json does what it says on the tim
# figpx.write_json(r'..\Plots\plotlyHeatHistoPlot.json')
# figpx.show()

# Pie Chart:

labels = df.day

fig_pie = {
    'data': [
        {
            'values': df['total_bill'],
            'labels': labels,
            'domain': {
                'x': [0, 0.5]
            },
            'name': 'No of Customers',
            'hole': 0.3,
            'type': 'pie'
        },
    ],
    'layout': {
        'title': 'No of Custoemrs per Day',
        'annotations': [
            {
                'font': {
                    'size': 20
                },
                'showarrow': True,
                'text': 'No of Customers',
                'x': 0.20,
                'y': 1
            },
        ]
    }
}
# Cannot find a way to save this figure, need to read more in the documentation'
# iplot(fig_pie)

# produce a contour plot

# iplot([go.Histogram2dContour(x=df['total_bill'], y=df['tip'], contours=go.Contours(coloring='heatmap')),
#        go.Scatter(x=df['total_bill'], y=df['tip'], mode='markers')])

# Produce a 3D plot with plotly:

fig_3D = go.Figure(
    [go.Mesh3d(
        x=df['total_bill'],
        y=df['tip'],
        z=df['size'],
        opacity=0.5,
        color='rgba(244, 22, 100, 0.6)'
    )]
)
fig_3D.update_layout(scene=dict(
    xaxis=dict(
        backgroundcolor='rgb(200, 200, 230)',
        gridcolor='white',
        showbackground=True,
        zerolinecolor='white'
    ),
    yaxis=dict(
        backgroundcolor='rgb(230, 200, 230)',
        gridcolor='white',
        showbackground=True,
        zerolinecolor='white'
    ),
    zaxis=dict(
        backgroundcolor='rgb(230, 230, 200)',
        gridcolor='white',
        showbackground=True,
        zerolinecolor='white'
    )),
    width=700,
    margin=dict(
        r=10,
        l=10,
        b=10,
        t=10
)
)
fig_3D.write_image(r'..\Plots\plotly3DPlot.png')
fig_3D.write_html(r'..\Plots\plotly3DPlot.html')
fig_3D.write_json(r'..\Plots\plotly3DPlot.json')
fig_3D.show()
