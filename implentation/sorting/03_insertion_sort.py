def insertionSort(array):
    size = len(array)
    for i in range(1, size):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key
    return array

array = [56, 45, 78, 32, 60]
arr = insertionSort(array)
for i in arr:
    print(i, end=" ")

# Time Complexity O(n)
# space Complexity O(1)