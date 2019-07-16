# This generates a heatmap of the number of pessengers in a given month of a year


import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools

df = pd.read_csv('flights.csv')

data = [go.Heatmap(x = df['year'],
                  y = df['month'],
                  z = df['passengers'].values.tolist(),
                  colorscale = 'Jet')]

layout = go.Layout(title = 'Number of pessengers in a given month of a year')

fig = go.Figure(data = data, layout = layout)
pyo.plot(fig)
