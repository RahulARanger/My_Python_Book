import sqlite3
import json
class json_scrap:
    def __init__(self):
        self.data=''''''
    def get_data(self):
        self.hand=open('roster_data.json')
        for i in self.hand:
            self.data+=i+'''\n'''
        return self.data              

a=json_scrap()
data=a.get_data()  
loaded=json.loads(data)
try:
    conn=sqlite3.connect('studs.sqlite')
    cur=conn.cursor()
    cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')
    NAME=[]
    TITLE=[]
    for i in range(len(loaded)):
        if loaded[i][0] not in NAME:
            NAME.append(loaded[i][0])
        else:pass
        if loaded[i][1] not in TITLE:
            TITLE.append(loaded[i][1])    
    print(NAME,TITLE)    
    for i in range(len(loaded)):
        ROLE=loaded[i][2]
        check_name=loaded[i][0]
        check_title=loaded[i][1]
        course_id=TITLE.index(check_title)+1
        member_id=NAME.index(check_name)+1
        print(member_id,course_id,ROLE)
        cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id,role) VALUES (?,?,?)''',
        ( member_id, course_id,ROLE) )
        conn.commit()
        cur.execute('''insert or replace into user(id,name) Values(?,?)''',(member_id,loaded[i][0]))
        conn.commit()
        cur.execute('''insert or replace into Course(id,title) Values(?,?)''',(course_id,loaded[i][1]))
        conn.commit()
    output=cur.execute('''SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X''')
    for i in output:
        print(i)
    conn.commit()
    cur.close()
    conn.close()
except:
    print('error')