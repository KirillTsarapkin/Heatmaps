#  This will generate 3 side by side heatmaps for 3 different cities.

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools # This will help organize the heat maps using subplots


df1 = pd.read_csv('BooneNC.csv')
df2 = pd.read_csv('AshevilleNC.csv')
df3 = pd.read_csv('JacksonvilleFL.csv')

#print(df.header())

trace1 = go.Heatmap(x = df1['DAY'],
                    y = df1['LST_TIME'],
                    z = df1['T_HR_AVG'].values.tolist(),
                    colorscale = 'Jet',
                    zmin =5 , zmax = 40) # Since there are multiple heat maps, we need to set max and min color values

trace2 = go.Heatmap(x = df2['DAY'],
                    y = df2['LST_TIME'],
                    z = df2['T_HR_AVG'].values.tolist(),
                    colorscale = 'Jet',
                    zmin =5 , zmax = 40)

trace3 = go.Heatmap(x = df3['DAY'],
                    y = df3['LST_TIME'],
                    z = df3['T_HR_AVG'].values.tolist(),
                    colorscale = 'Jet',
                    zmin =5 , zmax = 40)

data = [trace1, trace2, trace3]
fig = tools.make_subplots(rows = 1,cols = 3, subplot_titles=['Boone, NC','Asheville, NC','Jacksonville, FL'], shared_yaxes=True) # shared_yaxes=True makes hours appear only on the left
fig.append_trace(trace1,1,1) #'trace goes into row 1, column 1
fig.append_trace(trace2,1,2) #'trace goes into row 1, column 2
fig.append_trace(trace3,1,3) #trace goes into row 1, column 3
fig['layout'].update(title = 'Hourly Average Temperature Comparison for a Week ')
pyo.plot(fig)
