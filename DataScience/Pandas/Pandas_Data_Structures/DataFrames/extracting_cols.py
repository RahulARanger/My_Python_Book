import pandas
s_1=pandas.Series({'Name':'Rahul','Age':19})
s_2=pandas.Series({'Name':'Yukihira','Age':19})
s_3=pandas.Series({'Name':'yukimura','Age':21})
df=pandas.DataFrame([s_1,s_2,s_3],index=['Real','Fictional','Fictional'])
# to extact a single column 
print(df['Name'])
# to extact multiple columns
print(df[['Name','Age']])

print(df['Name':])
# to exact the single cell
print(df.loc['Real','Name'])
df_2=pandas.DataFrame([s_1,s_2,s_3])
print(df_2)
print(df_2.loc[0,'Name'])