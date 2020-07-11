import pandas
s_1=pandas.Series({'Name':'Rahul','Age':19})
s_2=pandas.Series({'Name':'Yukhihira','Age':19})
s_3=pandas.Series({'Name':'yukhimura','Age':21})
s_4=pandas.Series({'Name':'Megami','Age':19})
s_5=pandas.Series({'Name':'Erina','Age':19})
s_6=pandas.Series({'Name':'Ayami','Age':21})
df=pandas.DataFrame([s_1,s_2,s_3,s_4,s_5,s_6],index=['Real','Fictional','Fictional','Fictional','Fictional','Fictional'])

df['Gender']=['M','M','M','F','F','F']
print(df)