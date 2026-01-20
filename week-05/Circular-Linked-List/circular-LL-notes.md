
# Circular Linked List


## 1. What is a Circular Linked List?

A **circular linked list** is a linked list where the **last node points back to the first node** instead of `None`.

```
[data | next] -> [data | next] -> [data | next]
      ^_____________________________________|
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

## 3. Circular Linked List Implementation

```python
class CircularLinkedList:
    def __init__(self):
        self.head = None
```

---

## 4. Insert at Beginning

```python
def insert_at_beginning(self, data):
    new_node = Node(data)

    if self.head is None:
        new_node.next = new_node
        self.head = new_node
        return

    temp = self.head
    while temp.next != self.head:
        temp = temp.next

    temp.next = new_node
    new_node.next = self.head
    self.head = new_node
```

---

## 5. Insert at End

```python
def insert_at_end(self, data):
    new_node = Node(data)

    if self.head is None:
        new_node.next = new_node
        self.head = new_node
        return

    temp = self.head
    while temp.next != self.head:
        temp = temp.next

    temp.next = new_node
    new_node.next = self.head
```

---

## 6. Display the List

```python
def display(self):
    if self.head is None:
        print("List is empty")
        return

    temp = self.head
    while True:
        print(temp.data, end=" -> ")
        temp = temp.next
        if temp == self.head:
            break
    print("(back to head)")
```

---

## 7. Delete a Node

```python
def delete(self, key):
    if self.head is None:
        return

    curr = self.head
    prev = None

    while True:
        if curr.data == key:
            if prev:
                prev.next = curr.next
            else:
                # deleting head
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = curr.next
                self.head = curr.next
            return

        prev = curr
        curr = curr.next

        if curr == self.head:
            print("Value not found")
            return
```

---

## 8. Search

```python
def search(self, key):
    if self.head is None:
        return False

    temp = self.head
    while True:
        if temp.data == key:
            return True
        temp = temp.next
        if temp == self.head:
            break
    return False
```

---

## 9. Full Usage Example

```python
cll = CircularLinkedList()

cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_beginning(5)
cll.insert_at_end(30)

cll.display()
# Output: 5 -> 10 -> 20 -> 30 -> (back to head)

cll.delete(10)
cll.display()
# Output: 5 -> 20 -> 30 -> (back to head)

print(cll.search(20))   # True
print(cll.search(100))  # False
```

---

## 10. Time Complexity

| Operation           | Time |
| ------------------- | ---- |
| Insert at beginning | O(n) |
| Insert at end       | O(n) |
| Delete              | O(n) |
| Search              | O(n) |

---

## 11. Why use Circular Linked Lists?

* No `None` pointer
* Efficient for **round-robin scheduling**
* Used in **CPU scheduling**, multiplayer games, buffers

