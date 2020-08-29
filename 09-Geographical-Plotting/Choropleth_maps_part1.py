# %%
# import plotly.plotly as py
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

init_notebook_mode(connected=True)

data = {'type': 'choropleth',
        'locations': ['AZ', 'CA', 'NY'],
        'locationmode': 'USA-states',
        'colorscale': 'Greens',
        'text': ['text 1', 'text 2', 'text 3'],
        'z': [1.0, 2.0, 3.0],
        'colorbar': {'title': 'Colorbar title goes here'}}

layout = dict(geo={'scope': 'usa'})

choromap = go.Figure(data=[data], layout=layout)

iplot(choromap)

# df = pd.read_csv('2011_US_AGRI_Exports')

# df.head()

# datadf = dict(type='choropleth',
#               locations=df['code'],
#               locationmode='USA-states',
#               colorscale='YlOrRd',
#               text=df['text'],
#               z=df['total exports'],
#               colorbar={'title': 'Millions USD'},
#               marker=dict(line=dict(color='rgb(255,255,255)', width=1))
#               )

# layoutdf = dict(title='2011 US Agriculture Exports by State',
#                 geo=dict(scope='usa', showlakes=True,
#                          lakecolor='rgb(85,173,240)')
#                 )

# choromap2 = go.Figure(data=[datadf], layout=layoutdf)

# iplot(choromap2)

# %%
