class Sample:
    def __init__(self,from_,to_):
        self.count=from_
        self.max=to_
    def __iter__(self):
        self.back=False if self.count<self.max else True
        return self
    def __next__(self):
        if not self.back:
            if self.count<=self.max:
                store=self.count
                self.count+=1
                return store
            else:
                raise StopIteration
        else:
            if self.count>=self.max:
                store=self.count
                self.count-=1
                return store
            else:
                raise StopIteration
if __name__=='__main__':
    a=Sample(2,6)
    for i in a:
        print(i)
    b=Sample(9,0)
    print(list(b))