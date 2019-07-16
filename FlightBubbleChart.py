# This generates a bubble chart of the number of pessengers in a given month of a year

data1 = [go.Scatter(x = df['month'],
                   y = df['year'],
                   text = df['passengers'],# Text allows you to link up a column of values to what you want to display when you are hovering over something with your cursor
                   mode = 'markers',
                   marker = dict(size = df['passengers']/11,color=df['passengers'],  # Divide the marker to make it bigger since we are dealing we small values
                   showscale = True ))]                                              # Ddd color to add an extra dimension of information

layout1 = go.Layout(title = 'Number of pessengers in a given month of a year', hovermode = 'closest')
#hovermode = 'closest' hoovers over the closest point
fig1 = go.Figure(data=data1, layout=layout1)
pyo.plot(fig1)
