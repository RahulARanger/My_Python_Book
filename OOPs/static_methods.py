class test:
    number_of_instances=0
    def __init__(self):
# we can also write test.number_of_instances+=1 to update an static variable
        self.fav_num=66
    def check(self):
        print(test.number_of_instances)    
    @staticmethod
    def wow():
        # static method doesn't take self as an argument
        #print(test.fav_num)    
        test.number_of_instances+=1     
a=test()
a.wow()
#a.check()
b=test()
b.wow()
c=test()
c.wow()
c.check()