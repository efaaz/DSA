# Queue, Deque, and Circular Queue

## Queue

A **queue** is a linear data structure that follows **FIFO**: **First In,
First Out**. The first item added is the first item removed.

```text
enqueue(10) -> enqueue(20) -> enqueue(30)

front: 10
dequeue() -> 10
dequeue() -> 20
```

Queues are used in task scheduling, printer queues, breadth-first search, and
data buffering.

### Basic implementation with `front` and `rear`

In languages such as C or C++, a queue is often implemented with a fixed-size
array. Two positions are tracked:

- `front` points to the next item to remove.
- `rear` points to the next position where an item can be added.

```text
enqueue(item):
    if rear == capacity:
        queue is full
    else:
        items[rear] = item
        rear = rear + 1

dequeue():
    if front == rear:
        queue is empty
    else:
        item = items[front]
        front = front + 1
        return item
```

The `front` and `rear` positions are needed because a fixed-size array does
not grow automatically. In a real implementation, the positions may need to
be shifted or reused when space becomes available.

### Python implementation with a list

Python lists grow dynamically, so a separate capacity is not required. The
beginning of the list can represent the front and the end can represent the
rear.

```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

`append()` adds at the rear, but `pop(0)` is `O(n)` because the remaining
elements must be shifted. For efficient queues, Python provides
`collections.deque`.

```python
from collections import deque

items = deque()
items.append(10)       # enqueue
items.append(20)
first = items.popleft()  # dequeue: 10
```

`deque.append()` and `deque.popleft()` are `O(1)`.

## Deque

A **deque** (double-ended queue) allows insertion and removal at both ends.
It is pronounced “deck”.

```text
push_front(10) -> push_back(20)

front: 10
back: 20
```

### Basic methods

| Method | Description |
| --- | --- |
| `push_front(item)` | Add an item at the front |
| `push_back(item)` | Add an item at the rear |
| `pop_front()` | Remove and return the front item |
| `pop_back()` | Remove and return the rear item |
| `peek_front()` | Read the front item |
| `peek_back()` | Read the rear item |

### Python implementation

`collections.deque` is designed for efficient operations at both ends.

```python
from collections import deque

items = deque()
items.appendleft(10)  # push_front
items.append(20)     # push_back
items.popleft()      # pop_front
items.pop()          # pop_back
```

The four insertion and removal operations are `O(1)`.

## Circular queue

A **circular queue** uses a fixed-size array as if its end connects back to
its beginning. When `rear` reaches the last index, it wraps around to index
`0`. This reuses spaces created by earlier dequeues.

```text
index:  0   1   2   3   4
        └───────────────┘
             wraps around
```

The positions are updated with:

```python
next_position = (position + 1) % capacity
```

For a fixed-size implementation:

- The queue is empty when `front == -1`.
- The queue is full when `(rear + 1) % capacity == front`.
- After removing the last item, reset both `front` and `rear` to `-1`.

```python
class CircularQueue:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        next_rear = (self.rear + 1) % self.capacity
        if next_rear == self.front:
            raise OverflowError("queue is full")

        if self.front == -1:
            self.front = 0

        self.rear = next_rear
        self.items[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            raise IndexError("dequeue from an empty queue")

        item = self.items[self.front]
        self.items[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        return item
```

Both `enqueue()` and `dequeue()` take `O(1)` time. A circular queue is useful
when the queue has a fixed capacity, such as a network buffer or a streaming
buffer.

## Comparison

| Structure | Ordering | Main advantage |
| --- | --- | --- |
| Queue | FIFO | Process items in arrival order |
| Deque | Both ends | Add and remove from either end |
| Circular queue | FIFO with wraparound | Reuse fixed-array space |