# Linked List

A linked list is a linear data structure made up of a sequence of **nodes**. Each node stores:

1. **Data** - the value held by the node.
2. **Link** - a reference to the next node in the sequence.

The first node is called the **head**. The last node points to `None`, which marks the end of the list.

Unlike an array, linked-list nodes do not need to be stored in consecutive memory locations. This makes insertion and deletion efficient when the position of the relevant node is already known.

## Node representation

```text
Node
├── data
└── next ──> next node
```

Example:

```text
head -> [10 | next] -> [20 | next] -> [30 | None]
```

## Types of linked lists

## 1. Singly linked list

Each node contains a link to the next node only.

```text
head -> A -> B -> C -> None
```

## 2. Doubly linked list

Each node contains links to both the previous and the next node.

```text
None <- A <-> B <-> C -> None
```

## 3. Circular linked list

The last node links back to the first node instead of pointing to `None`.

```text
A -> B -> C
^         |
└─────────┘
```

## Operations

| Operation | Description | Time complexity |
| --- | --- | --- |
| Traversal | Visit each node in order | `O(n)` |
| Search | Find a node containing a value | `O(n)` |
| Access by index | Find the node at a specific position | `O(n)` |
| Insert at the beginning | Add a new node before the current head | `O(1)` |
| Insert at the end | Add a new node after the last node | `O(n)` without a tail reference, `O(1)` with a tail reference |
| Insert after a known node | Link a new node after an existing node | `O(1)` |
| Delete from the beginning | Move the head to the next node | `O(1)` |
| Delete a known node | Update links to skip the node | `O(1)` when the previous node is known |
| Delete by value | Search for and remove a matching node | `O(n)` |

## Basic operations

### Traversal

Start at the head and follow each node's `next` link until `None` is reached.

```text
current = head

while current is not None:
    visit(current.data)
    current = current.next
```

### Insertion at the beginning

Create a new node, point it to the current head, and then make it the new head.

```text
new_node.next = head
head = new_node
```

### Insertion after a node

Save the current next node, connect the new node to it, and then connect the existing node to the new node.

```text
new_node.next = current.next
current.next = new_node
```

### Deletion from the beginning

Move the head to the second node.

```text
head = head.next
```

### Deletion after a node

Change the current node's link so that it skips the node being deleted.

```text
current.next = current.next.next
```

## Advantages

- Insertion and deletion do not require shifting other elements.
- The list can grow and shrink dynamically.
- It is useful for implementing stacks, queues, and graph adjacency lists.

## Disadvantages

- Accessing an element by index is slower than with an array.
- Each node requires extra memory for one or more links.
- Nodes are not stored contiguously, which can reduce cache performance.
