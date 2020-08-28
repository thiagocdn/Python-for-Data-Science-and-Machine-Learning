# %%
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)

# df = pd.read_csv('2014_World_Power_Consumption')
# df.head()


# data = dict(type='choropleth',
#             colorscale='Viridis',
#             locations=df['Country'],
#             reversescale=True,
#             locationmode="country names",
#             text=df['Text'],
#             z=df['Power Consumption KWH'],
#             colorbar={'title': 'Power Consumption in KWH'})

# layout = dict(title='Countries Power Consumption',
#               geo=dict(showframe=False,
#                        projection={'type': 'mercator'}))


df = pd.read_csv('2012_Election_Data')
df.head()


data = dict(type='choropleth',
            colorscale='Viridis',
            locations=df['State Abv'],
            reversescale=True,
            locationmode="USA-states",
            text=df['State'],
            marker=dict(line=dict(color='rgb(255,255,255)', width=1)),
            z=df['Voting-Age Population (VAP)'],
            colorbar={'title': 'Voting-Age Population (VAP)'})

layout = dict(title='Countries Power Consumption',
              geo=dict(scope='usa', showlakes=True,
                       lakecolor='rgb(85,173,240)'))


choromap = go.Figure(data=[data], layout=layout)
iplot(choromap, validate=False)

# %%
