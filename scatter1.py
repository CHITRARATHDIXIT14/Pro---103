import pandas as pd
import plotly.express as px

dataframes = pd.read_csv("data1.csv")
fig = px.scatter(dataframes , x='date' , y='cases' ,size = "country" , color="country" , maxsize=60 ) 
fig.show()