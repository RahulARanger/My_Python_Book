import sys
n=len(sys.argv)
sum=0
a=1
while a<n:
    if(int(sys.argv[a])%2==0):
     sum+=int(sys.argv[a]) 
    a+=1
print(sum)    