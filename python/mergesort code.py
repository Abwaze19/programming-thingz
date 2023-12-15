import random


arrayLength = input('enter the length of array: ')
arrayLength = int(arrayLength)

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1

arr = [random.randrange(1, 1000, 1) for i in range(arrayLength)]

print ("Unsorted array is:" + str(arr))
from datetime import datetime
start_time = datetime.now()
print("Code start time is: {}".format(start_time))

mergeSort(arr)
print ("Sorted array is:" + str(arr))

end_time = datetime.now()

print('merge sort Algorithm Code Execution Time:: {}'.format(end_time - start_time))
print("Code End time is: {}".format(end_time))