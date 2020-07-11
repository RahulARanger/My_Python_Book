'''
This is a program that counts the number of times of substr in str
there is a difference from the count() method of the string
'''
def subcount(str,substr):
    count=0
    str='a'
    
    a=len(substr)
    for i in range(len(str)):
        if(str[i:i+a]==substr):
            count+=1
    return count     

if __name__=='__main__':
    str=input()
    substr=input()
    print(subcount(str,substr))
