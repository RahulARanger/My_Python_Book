def wrapper(f):
    def fun(l):
        for i in range(len(l)):
           number=[j for j in l[i]]
           if len(number)>10:
              if number[0]=='0':
                   del number[0]
                   number.insert(0,'+')
                   number.insert(1,'9')
                   number.insert(2,'1')
              elif number[0]=='9':
                  number.insert(0,'+')                       
           elif len(number)<=10:
               number.insert(0,'+')
               number.insert(1,'9')
               number.insert(2,'1')
           number.insert(3,' ')
           number.insert(9,' ')
           l[i]=str('')
           for z in number:
               l[i]+=z
        print(*sorted(l), sep='\n') 
        return l                  
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 