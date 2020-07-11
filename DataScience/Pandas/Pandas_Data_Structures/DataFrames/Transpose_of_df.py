import pandas
s_1=pandas.Series({'Name':'Rahul','Age':19})
s_2=pandas.Series({'Name':'Yukihira','Age':19})
s_3=pandas.Series({'Name':'yukimura','Age':21})
df=pandas.DataFrame([s_1,s_2,s_3],index=['Real','Fictional','Fictional'])
df_t=df.T
print(df)
print('\n`')
print(df_t)