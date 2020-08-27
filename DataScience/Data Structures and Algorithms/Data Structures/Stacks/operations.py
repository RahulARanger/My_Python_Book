
# ! This program Doesn't Follow BODMAS
class Plate:
    def __init__(self):
        self.lst=[]
        self.Ready=False
    def push(self,data):
        self.lst.append(data)
        assert self.analyse(data)
    def analyse(self,data):
        if type(data)==str:
            if data in '*+/-':
                self.Ready=True
            else:
                print('Error Occured!! Try again')
                return False
        else:
            if self.Ready:
                answer=eval(str(self.lst[-3])+self.lst[-2]+str(self.lst[-1]))
                for _ in range(3):self.pop()
                self.Ready=False
                self.push(answer)
        return True
    def pop(self):
        if len(self.lst)!=0:self.lst.pop()
        else:
            assert(False,'Stack UnderFlow')
    def __str__(self):
        return str(self.lst)
if __name__=='__main__':
    a=Plate()
    a.push(3)
    a.push('+')
    a.push(3)
    print(a)
    a.push('*')
    a.push(34)
    print(a)