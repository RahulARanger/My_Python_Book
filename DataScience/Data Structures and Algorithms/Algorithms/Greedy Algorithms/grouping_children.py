'''
statement : there are n children of Xi age try to group them in such a way childrens in one group has atmost age differnece of 1 year
and try to make tht number of group as minimum as possible
test cases : https://codereview.stackexchange.com/questions/126793/celebration-party-problem-algorithm#:~:text=I%20solved%20the%20following%20problem%3A&text=You've%20invited%20a%20lot,to%20each%20of%20the%20groups
'''
n=int(input())
count=1
lst=[float(i) for i in input().split()]
current_grp=[]
for i in range(len(lst)):
    if len(current_grp)==0:
        current_grp.append(lst[i])
    else:
        if lst[i]-min(current_grp)<=1.0:
            current_grp.append(lst[i])
        else:
            current_grp=[]
            current_grp.append(lst[i])
            count+=1
print(count)