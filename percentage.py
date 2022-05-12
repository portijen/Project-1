import pandas as pd
import plotly.express as px

fields = ['date',' Annual % Change']

df = pd.read_csv('united-states-population-2022-03-03.csv', usecols=fields)

fig = px.line(df, x='date', y=' Annual % Change', title='percentage change over the years')

fig.show()