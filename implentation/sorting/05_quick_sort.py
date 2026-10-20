
def quickSort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quickSort(arr, l, p - 1)
        quickSort(arr, p + 1, r)


def partition(arr, l, r):
    pivot = arr[l]
    i = l + 1
    j = r

    while True:
        while i <= r and arr[i] < pivot:
            i += 1

        while j > l and arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j


arr = [24, 56, 78, 99, 65]

quickSort(arr, 0, len(arr) - 1)
print(arr)


# Time Complexity O(n^2)
# Space Complexity 