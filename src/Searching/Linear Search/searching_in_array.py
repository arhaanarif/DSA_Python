'''def linear_search(arr,target):
    size=len(arr)
    for index in range(0,size):
        if arr[index]==target:
            return index
    return -1

my_list=[10,23,45,70,11]
target=70
print(linear_search(my_list,target))'''


def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Return the index where the target is found
    return -1  # Return -1 if target is not found

# Example Usage:
arr = [10, 20, 30, 40, 50]
target = 30

result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
