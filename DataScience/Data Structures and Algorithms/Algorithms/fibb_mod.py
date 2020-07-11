# refer week 2 problem 5
import time
def create_series(n,m):
    series=[0,1]
    for i in range(n):
        if i==0 or i==1:continue
        else:
            series.append((series[i-1]+series[i-2])%m)
    if n<2:
        return series[:n]
    return series
n,m=[int(i) for i in input().split()]
predict=3+(m-1)*5
if n>m:
    n=n%m+2
       
series=create_series(predict,m)
print(series[n])
print(151 in series)
print(series.index(151))