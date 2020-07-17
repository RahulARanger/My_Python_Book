# this is the method to read the values after the x-dspam-confidence in the file and display the average of all such values
fname=input('Enter the Name of the File: ')
check='X-DSPAM-Confidence: '
len_of_check=len(check)
count,sum=0.000,0.000
hand=open(fname)
for i in hand:
    if check in i:
        count+=1
        sum+=float(i[len_of_check:])
avg=sum/count
print('Average spam Confidence: %.12f'%avg)
fname.close()