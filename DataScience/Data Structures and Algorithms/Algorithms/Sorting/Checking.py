import time
import insertion_sort
import selection_sort
import merge_sort
import Quick_sort
import counting_sort
lst=list(range(int(input('Enter a Number to Check: ')),-1,-1))
lst2=lst.copy()
lst3=lst.copy()
check=time.time()
sorted(lst3)
print('Timsort Takes: {}'.format(time.time()-check))
check=time.time()
counting_sort.count_sort(lst3)
print('Counting Sort Takes: {}'.format(time.time()-check))
lst4=lst.copy()
check=time.time()
Quick_sort.quick_sort(lst4,0,len(lst4)-1)
print('Quick Sort takes: {}'.format(time.time()-check))
check=time.time()
merge_sort.mersort(lst3)
print('Merge Sort Takes: {}'.format(time.time()-check))
check=time.time()
#insertion_sort.insert_sort(lst)
print('Insertion Sort takes: {}'.format(time.time()-check))
check=time.time()
#selection_sort.bub_sort(lst2)
print('Selection Sort takes: {} '.format(time.time()-check))

# According to the test cases right now, Merge Sort>Insertion Sort> Selection Sort (in terms of speed)