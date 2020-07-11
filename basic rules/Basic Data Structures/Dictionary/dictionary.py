# in this program we will use dictionary to store the email address and count them and we will print the ones with highest occurence (use test2.txt)
name=input()
hand=open(name)
check='From '
email={}
emaillist=[]
for i in hand:
    if check in i:
        emaillist=i.split()
        email[emaillist[1]]=email.get(emaillist[1],0)+1
index=None
m=0
for x in email:
    if(email[x]>m):
        m=email[x]
        index=x
print('%s %d'%(index,m))        
    