# performing binary search
def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1

    return -1

arr=[10,23,35,45,50,70,85]
target=50
result = binary_search(arr,target)

if result!=-1:
    print(f"element found at index{result}")

else:
    print("element not found in the array")