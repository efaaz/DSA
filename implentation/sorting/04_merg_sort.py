def divide(arr, l, r):
    if l < r:
        m = (l + r) // 2
        divide(arr, l, m)
        divide(arr, m + 1, r)
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    s1 = m - l + 1
    s2 = r - m  # r - (m+1) + 1

    L = [0] * s1
    R = [0] * s2

    for i in range(s1):
        L[i] = arr[l + i]

    for j in range(s2):
        R[j] = arr[m + 1 + j]

    i = j = 0
    k = l
    while i < s1 and j < s2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    while i < s1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < s2:
        arr[k] = R[j]
        j += 1
        k += 1


arr = [21, 31, 34, 50]

divide(arr, 0, len(arr) - 1)

for i in arr:
    print(i, end=" ")

# Time Complexity O(nlogn) 
# Space Complexity O(n) 