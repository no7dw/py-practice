import plotly.graph_objs as go
import plotly.offline as py

import numpy as np

data = [go.Scatter(
    y = np.random.randn(500),
    mode='markers',
    marker=dict(
        size='16',
        color = np.random.randn(500),
        colorscale='Viridis',
        showscale=True,
        line={'width': 0.5}
    )
)]

layout = dict(
   plot_bgcolor ='#F5F7FA',
   paper_bgcolor = '#F5F7FA',
   width = 500,
   xaxis= {'zeroline': false},
   yaxis= {'zeroline': false},
)

py.iplot( dict(data=data, layout=layout) )
