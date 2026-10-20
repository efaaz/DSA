# Stack

A **stack** is a linear data structure that follows **LIFO**: **Last In, First
Out**. The item added most recently is the first item removed.

Example:

```text
push(10) -> push(20) -> push(30)

top: 30
pop() -> 30
pop() -> 20
```

Stacks are commonly used for function calls, undo operations, browser history,
expression parsing, and depth-first search.

## Basic methods

| Method | Description |
| --- | --- |
| `push(item)` | Add an item to the top |
| `pop()` | Remove and return the top item |
| `peek()` | Return the top item without removing it |
| `is_empty()` | Check whether the stack has no items |
| `size()` | Return the number of items |

## Building a stack with `insert()`

With `insert(0, item)`, index `0` is treated as the top of the stack.

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

`insert(0, item)` and `pop(0)` are `O(n)` because the other list elements
must be shifted.

## Building a stack with `append()`

With `append(item)`, the end of the list is treated as the top of the stack.

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

`append()` and `pop()` at the end of a Python list are `O(1)` amortized, so
this is usually the preferred implementation.

## Complexity

| Operation | `insert(0)` version | `append()` version |
| --- | --- | --- |
| `push` | `O(n)` | `O(1)` amortized |
| `pop` | `O(n)` | `O(1)` |
| `peek` | `O(1)` | `O(1)` |
| `is_empty` | `O(1)` | `O(1)` |
| `size` | `O(1)` | `O(1)` |