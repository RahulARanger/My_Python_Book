class Plate:
    index=0
    def __init__(self,data=None):
        self.lst=[]
        if data is None:
            self.lst=[]
        else:
            for i in data:
                self.append(i)
    def append(self,data):
        if data in '({)}[]':
            self.lst.append(data)
        else:return None
        Plate.index+=1
    def __str__(self):
        return str(self.lst)
    def check(self):
        test={'{':0,'[':0,'(':0}
        for i in self.lst:
            if i in '{[(':test[i]+=1
            else:
                if i=='}':test['{']-=1
                elif i==']':test['[']-=1
                else:test['(']-=1
        return True if sum(list(test.values()))==0 else False
if __name__=='__main__':
    data=input('String: ')
    lst=[i for i in data]
    a=Plate(lst)
    print(a)
    print('{}Correct Expression'.format('' if a.check() else 'In'))