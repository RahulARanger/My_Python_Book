import pandas
sports={
    'Archery':'Bhutan',
    'Golf':'Scotland',
    'Sumo':'Japan',
    'Taekwodo':'South Korea'
}
s=pandas.Series(sports)
print(s)
print(s.index)
sports_part_two=pandas.Series(['India','England'],index=['Hockey','Cricket'])
print(sports_part_two)
print(type(sports_part_two.index))
# default Indexes
default=pandas.Series([1,2,3,4,5,6])
print(default)
print(default.index)