import pandas
series_with_indexes=pandas.Series(['Orange','Apple','Banana'],index=['Orange','Red','Yellow'])
print(series_with_indexes.loc['Orange':])
series_without_indexes=pandas.Series(['Orange','Apple','Banana','Grapes','Papaya','Watermelon','Kiwi'])
# end is included for the loc
print(series_without_indexes.loc[0:6:3])
# end is not included for the iloc
print(series_without_indexes.iloc[0:6:3])
# multiple indexs (comma seperated) only with iloc
print(series_without_indexes.iloc[[0,3,6]])