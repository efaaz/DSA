def selectionSort(array):
    size = len(array)
    
    for i in range(size):
        min = i
        for j in range(i, size):
            if array[min] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array
    
  
array = [56, 45, 78, 32 ,60]
arr = selectionSort(array)
for i in arr:
    print(i, end=" ")
    
# Time Complexity O(n^2) 
# Time Complexity O(1) 