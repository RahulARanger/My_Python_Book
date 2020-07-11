import pandas
s_1=pandas.Series({'Name':'Rahul','Age':19})
s_2=pandas.Series({'Name':'Yukhihira','Age':19})
s_3=pandas.Series({'Name':'yukhimura','Age':21})
s_4=pandas.Series({'Name':'Megami','Age':19})
s_5=pandas.Series({'Name':'Erina','Age':19})
s_6=pandas.Series({'Name':'Ayami','Age':21})
df=pandas.DataFrame([s_1,s_2,s_3,s_4,s_5,s_6],index=['Real','Fictional','Fictional','Fictional','Fictional','Fictional'])
# we can use either iloc and loc  to extact the rows we want but the methods may change
# depending on the presence of the index attribute of the pandas.DataFrame
# let's start with loc
print(df)
print('\n')
print(df.loc['Real'])
print()
print(df.loc['Fictional'])
# now with the iloc()
print('\n')
print(df.iloc[3])
print(df.iloc[[0,3]])
