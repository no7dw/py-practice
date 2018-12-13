from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import plotly.graph_objs as go

plot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])], filename='a')


import numpy as np

x = np.random.randn(2000)
y = np.random.randn(2000)
plot([go.Histogram2dContour(x=x, y=y, contours=dict(coloring='heatmap')),
       go.Scatter(x=x, y=y, mode='markers', marker=dict(color='white', size=3, opacity=0.3))], show_link=False, filename='b')
