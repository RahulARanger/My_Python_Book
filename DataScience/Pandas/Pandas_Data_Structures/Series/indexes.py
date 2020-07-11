# indexes of the Series can have duplicate values and it can contain different types too
# append is one of the way to combine two series into one
import pandas
lst=[1,2,3]
series=(pandas.Series(lst))
print(series)
print(series.hasnans)

