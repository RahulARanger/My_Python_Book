# this alg. is good when we need to create the list of numbers in the fibb.series
import time
def create_series(n):
    series=[0,1]
    for i in range(n):
        if i==0 or i==1:continue
        else:
            series.append(series[i-1]+series[i-2])
    if n<2:
        return series[:n]
    return series
n=int(input('Enter the Number of elements in the series: '))
time1=time.time()
print(create_series(n))            
print(time.time()-time1)