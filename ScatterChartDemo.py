import pandas as pd
import plotly.express as px
df = pd.read_csv("data.csv")
figure = px.scatter(df,x="Population",y="Per capita",color = "Country",title="Scatter Chart demo",size="Percentage",size_max=60)
figure.show()