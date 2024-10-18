# bubble sort implementation

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

unsortedArr=[5,4,3,2,1]
sortedArr=bubbleSort(unsortedArr)
print(sortedArr)