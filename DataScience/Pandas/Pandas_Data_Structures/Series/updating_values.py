import pandas
lst=[int(i) for i in input('List of numbers: ').split()]
series=pandas.Series(lst)
print(series)
series**=2
print(series)
