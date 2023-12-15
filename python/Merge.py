import matplotlib.pyplot as plt
import pandas as pd
import time
import seaborn as sns
sns.set()
# To genrate random array
from numpy import random

# MERGE SORT : Merge sort first divides the array into equal halves and then combines them in a sorted manner.
def merge_sort(unsorted_list):
    
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and divide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


#Creating an array of randomly unsorted values from the lower limit to the upper limit             
arr1 = list(random.randint(1,50,10000))
arr2 = list(random.randint(1,40,20000))
arr3 = list(random.randint(1,30,30000))
arr4 = list(random.randint(1,20,40000))
arr5 = list(random.randint(1,10,50000))

#Using Python time.time function we measure the time taken for the merge_sort function to run on each array
start1 = time.time()
print('initial time 1:' , start1)
merge_sort(arr1)
print('sorted array 1:' , arr1)
end1 = time.time()
print('end time 1:' , end1)

start2 = time.time()
print('initial time 2:' , start2)
merge_sort(arr2)
print('sorted array 2:' , arr2)
end2 = time.time()
print('end time 2:' , end2)


start3 = time.time()
print('initial time 3:' , start3)
merge_sort(arr3)
print('sorted array 3:' , arr3)
end3 = time.time()
print('end time 3:' , end3)

start4 = time.time()
print('initial time 4:' , start4)
merge_sort(arr4)
print('sorted array 4:' , arr4)
end4 = time.time()
print('end time 4:' , end4)

start5 = time.time()
print('initial time 5:' , start4)
merge_sort(arr5)
print('sorted array 5:' , arr4)
end5 = time.time()
print('end time 5:' , end4)

#A dataframe to hold our records of the different array lengths and the time taken for the bubblesort algorithm
#to run on each
summary  = pd.DataFrame([
    [len(arr1), end1-start1],
    [len(arr2), end2-start2],
    [len(arr3), end3-start3],
    [len(arr4), end4-start4],
    [len(arr5), end5-start5]],
    columns=['ArrayLength','TimeTaken'])

#Using Python's Matplotlib function to plot a graph of ArrayLength against the time taken
plt.plot(summary['TimeTaken'],summary['ArrayLength'], linewidth=2, markersize=5, marker='o', color='orange')
plt.xlabel('Time Taken(s)')
plt.ylabel('ArrayLength')
plt.title('Plot of Time Taken against Array Length')
plt.show()
