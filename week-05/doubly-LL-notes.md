
#  Doubly Linked List

## 1. What is a Doubly Linked List?

A **doubly linked list** is a linear data structure where each node contains **two pointers**:

* Pointer to the **previous node**
* Pointer to the **next node**

```
None <- [prev | data | next] <-> [prev | data | next] <-> [prev | data | next] -> None
```

---

## 2. Node Definition

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

---

## 3. Doubly Linked List Implementation

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
```

---

## 4. Insert at Beginning

```python
def insert_at_beginning(self, data):
    new_node = Node(data)

    if self.head is not None:
        self.head.prev = new_node
        new_node.next = self.head

    self.head = new_node
```

---

## 5. Insert at End

```python
def insert_at_end(self, data):
    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        return

    temp = self.head
    while temp.next:
        temp = temp.next

    temp.next = new_node
    new_node.prev = temp
```

---

## 6. Display the List (Forward)

```python
def display(self):
    temp = self.head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")
```

---

## 7. Delete a Node

```python
def delete(self, key):
    temp = self.head

    while temp and temp.data != key:
        temp = temp.next

    if temp is None:
        print("Value not found")
        return

    if temp.prev:
        temp.prev.next = temp.next
    else:
        self.head = temp.next

    if temp.next:
        temp.next.prev = temp.prev
```

---

## 8. Search

```python
def search(self, key):
    temp = self.head
    while temp:
        if temp.data == key:
            return True
        temp = temp.next
    return False
```

---

## 9. Full Usage Example

```python
dll = DoublyLinkedList()

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_beginning(5)
dll.insert_at_end(30)

dll.display()
# Output: 5 <-> 10 <-> 20 <-> 30 <-> None

dll.delete(10)
dll.display()
# Output: 5 <-> 20 <-> 30 <-> None

print(dll.search(20))   # True
print(dll.search(100))  # False
```

---

## 10. Time Complexity

| Operation           | Time |
| ------------------- | ---- |
| Insert at beginning | O(1) |
| Insert at end       | O(n) |
| Delete              | O(n) |
| Search              | O(n) |

---

## 11. Why use Doubly Linked Lists?

* Traversal in **both directions**
* Easier deletion (no need to track previous node)
* Used in **undo/redo**, browser navigation, LRU cache

---
