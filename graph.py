import plotly.express as px
import pandas as pd

def show():
  df = pd.read_csv('output.csv', parse_dates=["date"]).drop_duplicates()

  fig = px.line(df, x="date", y="price", color='name', labels={ "name": "Produto", "date": "Data", "price": "Preço" })

  fig.update_yaxes(tickprefix="R$ ")
  fig.update_layout(template='plotly_dark')
  fig.show()
