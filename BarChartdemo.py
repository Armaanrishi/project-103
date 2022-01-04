import pandas as pd
import plotly.express as px
df = pd.read_csv("data.csv")
figure = px.bar(df,x="Country",y="InternetUsers",color = "Country",title="Bar Chart demo")
figure.show()