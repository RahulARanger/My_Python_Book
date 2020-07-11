import csv
users={
    'alpha':[5,6],
    'beta':[7,8],
    'gamma':[9,10]
}
cols=['user','Error','Infos']
with open('test2.csv','w') as hand:
    w=csv.writer(hand)
    w.writerow(cols)
    for i in users:
        row=[i,users[i][0],users[i][1]]
        w.writerow(row)
        
