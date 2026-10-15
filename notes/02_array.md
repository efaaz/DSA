# Array 
An array is a continues memory allocation data structure

+ we can store same type of data in an array

> but in python we can store multiple type data in an array

In python we can use array in 2 way

+ Python array module
+ Python Numpy module

> In other language we need to manualy enter the array size but in python the array size is dynamicaly selected based on the array

# Array using Python array module

```python
import array as *

val = array('i',[1, 2, 3, 4, 5, 6])

for i in range(0, len(val)):
    print(val[i])

# output:
# 1
# 2
# 3
# ...

for i in range(0, len(val)):
    print(val[i], end=:" ")

# output: 1 2 3 4 5 6


val.reverse()
for i in range(0, len(val)):
    print(val[i], end=:" ")

# output: 6 5 4 3 2 1
```

+ 'i' Integar    2 byte
+ 'L' Integar    4 byte
+ 'f' float      4 byte
+ 'd' float      8 byte
+ 'u' Character  2 byte


## Array manipulation

```python

import array as *

arr = array('i', [10, 20, 30, 40, 50, 60])

arr.insert(idx, value)
arr.append(value)
arr[2] = value

# delete any array element 
arr.pop(idx)
arr.remove(value)

# copy array
newarr = array(arr.typecode, (x for x in arr))
```

# Array using NumPy array module

```python
import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
print("1D array: ", arr_1d)

array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
print("2D array: ", array_2d)

```


```python

arr = np.linspace(start, end, devideParts)
arr = np.linspace(10, 20, 11)
# OUTPUT: 10.0 11.0 12.0 13.0 14.0 15.0 16.0 17.0 18.0 19.0 20.0

arr = np.arrange(start, end, diff)
arr = np.arrange(10, 20, 2)
# OUTPUT: 10 12 14 16 18
```

```python

# create a zero value array
zero = np.zeros((3, 3))
print("zeros array: ", zero)

#creating a one value array
ones = np.ones((2,3))
print("one array: ", ones)

# creating constant value array
con = np.full((2,2), 5)
print("constant value array: ", con)

# creating random value array
random = np.random.random((3,3))
print("Random value array: ", random)

# creating squence array
sequence = np.arange(0, 10, 2)
print("array of sequence: ", sequence)

```

