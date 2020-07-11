import numpy
for x in range(int(input())):
    triangle=[]
    n=int(input())
    for i in range(n):
        line=[int(z) for z in input().split()]
        triangle.append(line)
    sum_of_lines=[]    
    for i in range(n):
        temp=[]
        if len(sum_of_lines)==0:
            element=[]
            element.append(triangle[0][0])
            temp.append(element)
        else:
            for j in range(i+1):
                element=[]
                flag_0=j
                flag_1=j-1
                if flag_0<len(sum_of_lines):
                    for z in sum_of_lines[flag_0]:
                        element.append(triangle[i][j]+z)
                if flag_1>=0:
                    for z in sum_of_lines[flag_1]:
                        element.append(triangle[i][j]+z)
                element.sort()
                element.reverse()
                temp.append(element)        
        sum_of_lines=temp
        print(sum_of_lines)
    #print(numpy.max(sum_of_lines))
    
                    
