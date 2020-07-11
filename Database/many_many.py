import sqlite3
try:
    conn=sqlite3.connect('many_many_through_py.sqlite')
    cur=conn.cursor()
    cur.execute('drop table if exists Course')
    cur.execute('drop table if exists User')
    cur.execute('drop table if exists Member')
    cur.execute('''
  CREATE TABLE "User" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name"	TEXT,
	"email"	TEXT
);''')
    cur.execute('''
    create table Member(
user_id integer,
course_id integer,
role integer,
primary key (user_id,course_id)
    );
    ''')
    conn.commit()
    cur.execute('''
  CREATE TABLE "Course" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"title"	TEXT
);
    ''')
    conn.commit()
    cur.execute('insert into Course(id,title) values(?,?);',(1,'Python'))
    cur.execute('insert into Course(title) values(?);',('SQL',))
    cur.execute('insert into Course(title) values(?);',('PHP',))   
    conn.commit()
    cur.execute('insert into Member(user_id,course_id,role) values(?,?,?);',(1,1,1))
    cur.execute('insert into Member(user_id,course_id,role) values(?,?,?);',(2,1,0))
    cur.execute('insert into Member(user_id,course_id,role) values(?,?,?);',(3,1,0))
    cur.execute('insert into Member(user_id,course_id,role) values(?,?,?);',(1,2,0))
    cur.execute('insert into Member(user_id,course_id,role) values(?,?,?);',(2,2,0))
    cur.execute('insert into Member(user_id,course_id,role) values(?,?,?);',(2,3,1))
    cur.execute('insert into Member(user_id,course_id,role) values(?,?,?);',(3,3,0))
    conn.commit()
    cur.execute('insert into User(id,name,email) values(?,?,?)',(1,'Jane','jane@tsugi.org'))
    cur.execute('insert into User(name,email) values(?,?)',('ed','ed@tsugi.org'))
    cur.execute('insert into User(name,email) values(?,?)',('sue','sue@tsugi.org'))
    conn.commit()
    cur.execute('select * from Course where title=?',('SQ',))
    print(cur.fetchone())#none for the not found results
    for i in cur.execute('select * from Course where title=?',('SQL',)):
      print(i)
    conn.close()
except:
        print('error')