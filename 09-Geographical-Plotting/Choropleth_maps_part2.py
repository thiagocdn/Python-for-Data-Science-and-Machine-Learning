# %%
# import plotly.plotly as py
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

df = pd.read_csv('2014_World_GDP')
df.head()

data = dict(type='choropleth',
            locations=df['CODE'],
            text=df['COUNTRY'],
            z=df['GDP (BILLIONS)'],
            colorbar={'title': 'GDP in Billions USD'})

layout = dict(title='2014 Global GDP',
              geo=dict(showframe=False,
                       projection={'type': 'mercator'}))

choromap = go.Figure(data=[data], layout=layout)

iplot(choromap)


# %%
