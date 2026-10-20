class Node:
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class SinglyLinkedlist:
    def __init__(self, head=None) -> None:
        self.head = head

    def push_back(self, value):
        temp = Node(value)
        if self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = temp
        else:
            self.head = temp

    def push_front(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def pop_front(self):
        if self.head is None:
            print("Linklist is empty")
            return
        self.head = self.head.next

    def pop_back(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next is not None and temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def deleteByValue(self, value):
        current = self.head
        if current is None:
            print("Linklist is empty")
            return
        if current.data is value:
            self.head = current.next
            return
        while current.next is not None:
            if current.next.data is value:
                current.next = current.next.next
                return
            else:
                current = current.next
        print("Not found")

    def searchByData(self, value):
        temp = self.head
        idx = 0
        while temp is not None:
            if temp.data == value:
                return idx
            temp = temp.next
            idx += 1

    def printAll(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next


class doublyLinklist:
    def __init__(self, head=None) -> None:
        self.head = head

    def push_back(self, data):
        temp = Node(data)

        if self.head is None:
            self.head = temp
            return
        current = self.head

        while current.next is not None:
            current = current.next

        # *! you cant use current.next = temp.prev beacuse both are None
        current.next = temp
        temp.prev = current

    def push_front(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def pop_front(self):
        if self.head is None:
            print("Linklist is empty")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    def pop_back(self):
        if self.head is None:
            print("Linklist is empty")
            return
        current = self.head

        while current.next is not None and current.next.next is not None:
            current = current.next
        current.next = None

    def deleteByVal(self, value):
        current = self.head
        if self.head is None:
            print("Linklist is empty")
            return
        while current is not None and current.data != value:
            current = current.next
            
        if current is None:
            print("Value not found")
            return
        
        if current.prev is None:
            self.head = current.next
            
        else:
            current.prev.next = current.next

        if current.next is not None:
            current.next.prev = current.prev
            
            
    def serachByData(self, data):
        if self.head is None:
            print("Linklist is empty")
        current = self.head
        idx = 0
        while current is not None:
            if current.data == data:
                return idx
            current = current.next
            idx += 1

    def printAll(self):
        if self.head is None:
            print("Linklist is empty")
            return
        current = self.head

        while current is not None:
            print(current.data, end=" <--> ")
            current = current.next


obj = SinglyLinkedlist()
obj.push_back(20)
obj.push_back(30)
obj.push_back(40)
obj.push_front(10)
obj.printAll()
print("\n--------")
obj.pop_front()
obj.pop_back()
obj.printAll()
print("\n--------")
idx = obj.searchByData(40)
print("serched index of the value: ", idx)

print("\n+++++ Doubly Linklist +++++ ")
dl = doublyLinklist()
dl.push_back(20)
dl.push_back(30)
dl.push_back(40)
dl.push_back(50)
dl.push_back(60)
dl.push_front(10)
dl.printAll()
dl.pop_back()
dl.pop_front()
print("\n------")
dl.printAll()
print("\n--------")
print(dl.serachByData(40))
