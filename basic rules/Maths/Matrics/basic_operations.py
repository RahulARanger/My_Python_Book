import os
import math
import functools as f
# functools helps us to use reduce() which can reduce the list to a numerical value
# map() function modifies the elements of the list using lambda function
def add_vectors(lists,list2):
     return ([lists[i]+list2[i] for i in range(len(lists))])
def subtract_vectors(lists,list2):
     return ([lists[i]-list2[i] for i in range(len(lists))])
def mod_of_vector(list):
    a=0.000
    for i in list:
        a+=float(i*i)
    return math.sqrt(a)    
def dot_product(lists,list2):
    answer=[lists[i]*list2[i] for i in range(len(lists))]
    return float(f.reduce(lambda x,y:x+y,answer))
def scalar_projection(lists,list2):
    return dot_product(lists,list2)/mod_of_vector(list2)
def vector_projection(lists,list2):
    a=scalar_projection(lists,list2)/mod_of_vector(list2)
    return list(map(lambda x:a*x,list2))
def lay_coordinates(vectors,names):
    answer=[]
    for i in range(1,len(names)):
         answer.append(dot_product(vectors[names[0]],vectors[names[i]])/(math.pow(mod_of_vector(vectors[names[i]]),2)))
    return answer
vector,vectors=[],{}
answer=[]
name=input('The name of the Vector: ')
vector=[int(i) for i in input('Enter the Values of the Vector of any dimensions: ').split()]
vectors[name]=vector
a=1
while(a>0 and a<10):
  try:  
      
     print('1 Enter another vector\n')
     print('2 for adding it to another vector\n')
     print('3 for subtracting it to another vector\n')
     print('4 for finding the scalar projection of the another vector\n')
     print('5 for finding the vector projections of the another vector\n')
     print('6 for the changing the dimensions based on the two orthogonal vectors\n')
     print('7 for printing the all the Stored vector\n')
     print('8 for printing the Modulus of the Vector\n')
     print('9 for finding the dot product of the Vectors\n')
     print('any other input for exiting\n')
     a=int(input('Your call: '))
# entering or modyfimng the vector
     if a==1:
         name=input('Enter the name of the vector: ')
         vector=[int(i) for i in input('Enter the Values of the Vector of any dimensions: ').split()]
         vectors[name]=vector
# this is for adding the vectors
     elif a==2:
         names=[i for i in input('Enter the names of the vectors that you want to add: ').split()]
         for j in range(len(names)-1):
          if len(vectors[names[j]])!=len(vectors[names[j+1]]):assert(False,'The Vectors of Differnent Dimensions cannot be added')
          else:
              if len(answer)!=0: 
               answer=add_vectors(answer,vectors[names[j+1]])
              else:
                  answer=add_vectors(vectors[names[j]],vectors[names[j+1]]) 
         print('The Sum of the Choosen Vectors are',answer)
         answer=[]
# this is for subtracting the vectors
     elif a==3:
         names=[i for i in input('Enter the names of the vectors that you want to Subtract: ').split()]
         for j in range(len(names)-1):
          if len(vectors[names[j]])!=len(vectors[names[j+1]]):assert(False,'The Vectors of Differnent Dimensions cannot be Subtracted')
          else:
              if len(answer)!=0: 
               answer=subtract_vectors(answer,vectors[names[j+1]])
              else:
                  answer=subtract_vectors(vectors[names[j]],vectors[names[j+1]]) 
         print('The Difference of the Choosen Vectors are',answer)
         answer=[]
# this is for finding the scalar projection of the vector over another
     elif a==4:
         names=[i for i in input('Enter the names of the Vectors first name will be the vector which will be projected on the next vector: ').split()]
         if len(names)==2:
          print('The Scalar projection of that two vectors are: %.3f'% scalar_projection(vectors[names[0]],vectors[names[1]]))
         else:
             assert(False,'U have not given exactly two names')
# vector projection of one vector over another
     elif a==5:
         names=[i for i in input('Enter the names of the Vectors first name will be the vector which will be projected on the next vector: ').split()]
         if len(names)==2:
          print('The Vector projection of that two vectors are: ',vector_projection(vectors[names[0]],vectors[names[1]]))
         else:
             assert(False,'U have not given exactly two names')
# this is for the change of the axis             
     elif a==6:
         names=[i for i in input('Enter the names of the Vectors first name will be the maim vector and anothers are the new dimensional axis make sure they are orthogonal to each other: ').split()]
         if len(vectors[names[0]])!=(len(names)-1):
             assert(False,'The Axies are Not enough')
         elif dot_product(vectors[names[1]],vectors[names[2]])!=0:
             assert(False,'The axis are not perpendicualar pair wise check them')
         else:
             print('The changed Coordinates are: ',end='')
             ae=lay_coordinates(vectors,names)
             print('[ ',end='')
             for i in range(len(ae)):
                 print(str(i)+str(names[i+1]),end=' ')
             print(' ]',end='')
             print('')
# for showing the total vectors in the dictionary
     elif a==7:
         for i in vectors:
             print(i,'=',vectors[i])
# this is for finding the modulus of the vector
     elif a==8:
             names=[i for i in input('Enter the names of the Vector to find it\'s modulus: ').split()]
             print('The modulus of the given vector is: ',mod_of_vector(vectors[names[0]]))
# this is for dot product of two vectors
     elif a==9:
         names=[i for i in input('Enter the name of the two vectors to find their dot product: ').split()]
         print(names[0]+'*'+names[1]+' = ',dot_product(vectors[names[0]],vectors[names[1]]))

     else:break           
  except AssertionError as obj:
       print(obj)
       answer=[]
       continue
  except:
      print('try again')
      continue  
  os.system('pause')
    