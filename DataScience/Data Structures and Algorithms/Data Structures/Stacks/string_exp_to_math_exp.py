import re
class Tweak:
    def __init__(self,exp):
        self.exp=exp
    def convert(self):
        ans=[]
        nums=re.findall(r'([0-9]+)',self.exp)
        symbols=re.findall(r'([-+*)(/])',self.exp)
        flag=False
        for i in self.exp:
            if i in symbols: 
                ans.append(symbols[0])
                del symbols[0]
                flag=False
            elif flag is False:
                ans.append(float(nums[0]))
                del nums[0]
                flag=True
        return ans
if __name__=='__main__':
    a=Tweak(input('Enter the Experssion:'))
    print(a.convert())