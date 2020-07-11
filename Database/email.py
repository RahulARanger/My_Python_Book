""" sqlite file is as the name implies a file that contains SQLite database.
.db is the file extension used by Oracle, Paradox and XoftSpySE databases. """
# this program finds the maximum number of the mails sent by the originzation 
# it gets data from the database
import sqlite3
import re
hand=open('mbox.txt')
emails=[]
max_orginization=0

for i in hand:
    email=re.findall('^From (\S+@*\S)',i)
    if len(email)!=0:
        emails.append(email[0])
email_collect={}
for i in emails:
    f=re.findall('@(.*)',i)
    email_collect[f[0]]=email_collect.get(f[0],0)+1
conn=sqlite3.connect('email_by_orig.sqlite')
curr=conn.cursor()
curr.execute('drop table  if exists counts')
curr.execute('create table counts( org text, count integer)')
for i in email_collect:
    if max_orginization<email_collect[i]:
        max_orginization=email_collect[i]
    curr.execute('''INSERT INTO counts (org, count)
                VALUES (?, ?)''', (i,email_collect[i]))
    conn.commit()
print(max_orginization)
curr.close()    