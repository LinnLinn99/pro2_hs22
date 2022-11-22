import plotly.express as px

df = px.data.gapminder().query("year == 2007").query("continent == 'Switzerland'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()


import plotly.express as px

df = px.data.gapminder().query("country == 'Switzerland'")
fig = px.bar(df, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             labels={'pop':'population of Canada'}, height=400)
fig.show()
