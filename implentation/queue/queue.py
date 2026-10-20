class queue:
    def __init__(self) -> None:
        self.items = []

    def is_Empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_Empty():
            print("Queue is empty")
        else:
            return self.items.pop(0)


class deque:
    def __init__(self) -> None:
        self.items = []

    def is_Empty(self):
        return len(self.items) == 0

    def push_front(self, data):
        self.items.insert(0, data)

    def push_back(self, data):
        self.items.append(data)

    def pop_front(self):
        if self.is_Empty():
            print("Queue is empty")
        else:
            return self.items.pop(0)

    def pop_back(self):
        if self.is_Empty():
            print("Queue is empty")
        else:
            return self.items.pop()


class circularQueue:
    def __init__(self, size) -> None:
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        elif self.rear == -1:
            self.rear = self.front = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size


q = queue()
q.push(2)
q.push(3)
q.push(4)
q.push(5)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

dq = deque()
dq.push_front(2)
dq.push_back(3)
dq.push_back(4)
dq.push_back(5)

print("+++++pop+++++")

print(dq.pop_front())
print(dq.pop_back())

print("+++++circular Queue+++++")

cq = circularQueue(5)
cq.enqueue(5)
cq.enqueue(6)
cq.enqueue(7)
cq.enqueue(8)
cq.enqueue(9)
cq.dequeue()
cq.enqueue(2)


