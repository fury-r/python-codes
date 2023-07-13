import math as m
import pandas as pd
import sys

df1=pd.read_csv("./datasets/players_20.csv")

df2=pd.DataFrame(df1,columns=['short_name','wage_eur','value_eur','release_clause_eur'])
df2['release_clause_eur']=df2['release_clause_eur'].apply(lambda x:   0 if m.isnan(x) else x)
df2=df2.sort_values('release_clause_eur',ascending=False)
df2.to_csv("./datasets/test.csv")
df2.to_html("./datasets/test.html")