def bubbleSort(array):
    size = len(array)
    
    for i in range(size):
        for j in range(size - 1 - i):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array

array = [56, 45, 78, 32 ,60]
arr = bubbleSort(array)
for i in arr:
    print(i, end=" ")
    
# Time Complexity O(n^2)
# Space Complexity O(1)