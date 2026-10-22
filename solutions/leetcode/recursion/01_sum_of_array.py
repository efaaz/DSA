# calculate total of a given array using iterative and recursive
def sumIterative(arr):
    for i in range(len(arr)):
        total = arr[i]
    return total


def sumRecursive(arr):
    if not arr:
        return 0
    return arr[0] + sumRecursive(arr[1:])
    
arr = [5, 10, 15, 20]  

print("Iteratvie: ", sumIterative(arr))
print("Recursive: ", sumIterative(arr))