import sqlite3
try:
    conn=sqlite3.connect('songs.db')
    curr=conn.cursor()
    f=curr.execute('select * from Artist;')
    g=f.fetchall()
    print(g)
    conn.commit()
    curr.close()   
except:
    print('Error')

