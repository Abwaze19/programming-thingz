import random
arrayLength = input('enter the length of array: ')
arrayLength = int(arrayLength)
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [random.randrange(1, 50, 1) for i in range(arrayLength)]

print ("Unsorted array is:" + str(arr))




from datetime import datetime
start_time = datetime.now()
print("Code start time is: {}".format(start_time))
bubbleSort(arr)
end_time = datetime.now()
print ("Sorted array is:" + str(arr))



print('Bubble sort Algorithm Code Execution Time: {}'.format(end_time - start_time))
print("Code End time is: {}".format(end_time))
