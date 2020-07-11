# this is the solution for the problem 7 of the week 3 assignment
import itertools
def check_this_up(lst):
  try:
    if lst[0][0]<lst[0][1]:
      lst.reverse()
  except:pass    
  for i in lst:
    [print(_,end='') for _ in i if type(_)==int]
n=int(input())
lst=[int(i) for i in input().split()]
lst.sort()
note=len(str(max(lst)))
collected=[]
for i in range(len(lst)):
  check=[int(i) for i in str(lst[i])]
  for j in range(note-len(check)):
    check.append(float(check[0]))
  collected.append(check)
collected.sort()
collected.reverse()  
count=0
for i in itertools.count(0):
  if collected.count(collected[count])==1:
    [print(_,end='') for _ in collected[count] if type(_)==int]
    count+=1
  else:
    hmm=collected.count(collected[count])
    check_this_up(collected[count:count+hmm])
    count+=hmm
  if count==len(collected):break  