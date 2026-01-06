
## 1. What is a Linked List?

A **linked list** is a linear data structure where elements (nodes) are not stored in contiguous memory.

Each **node** contains:

* **data**
* **reference (pointer)** to the next node

```
[data | next] -> [data | next] -> [data | next] -> None
```

---

## 2. Node Definition

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

## 3. Singly Linked List Implementation

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

---

## 4. Insert at Beginning

```python
def insert_at_beginning(self, data):
    new_node = Node(data)
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
```

---

## 6. Display the List

```python
def display(self):
    temp = self.head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
```

---

## 7. Delete a Node

```python
def delete(self, key):
    temp = self.head

    # If head node is to be deleted
    if temp and temp.data == key:
        self.head = temp.next
        return

    prev = None
    while temp and temp.data != key:
        prev = temp
        temp = temp.next

    if temp is None:
        print("Value not found")
        return

    prev.next = temp.next
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
ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_beginning(5)
ll.insert_at_end(30)

ll.display()
# Output: 5 -> 10 -> 20 -> 30 -> None

ll.delete(10)
ll.display()
# Output: 5 -> 20 -> 30 -> None

print(ll.search(20))   # True
print(ll.search(100))  # False
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

## 11. Why use Linked Lists?

Compared to Python lists:

* Faster insertions/deletions (no shifting)
* Dynamic size
* Used in stacks, queues, graphs, OS memory management, etc.


## TO DO
- Doubly linked list
- Circular linked list
