
# Queue (Linked List Implementation)

## 1. What is a Queue?

A **queue** is a linear data structure that follows the **FIFO** principle:

> **First In, First Out**

Elements are:

* **Inserted (enqueue)** from the **rear**
* **Removed (dequeue)** from the **front**

```
Front -> [data] -> [data] -> [data] <- Rear
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

## 3. Queue Implementation (Using Linked List)

```python
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
```

---

## 4. Enqueue (Insert Element)

```python
def enqueue(self, data):
    new_node = Node(data)

    if self.rear is None:
        self.front = self.rear = new_node
        return

    self.rear.next = new_node
    self.rear = new_node
```

---

## 5. Dequeue (Remove Element)

```python
def dequeue(self):
    if self.front is None:
        print("Queue is empty")
        return

    temp = self.front
    self.front = temp.next

    if self.front is None:
        self.rear = None
```

---

## 6. Peek (Front Element)

```python
def peek(self):
    if self.front is None:
        print("Queue is empty")
        return None
    return self.front.data
```

---

## 7. Display the Queue

```python
def display(self):
    temp = self.front
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
```

---

## 8. Search in Queue

```python
def search(self, key):
    temp = self.front
    while temp:
        if temp.data == key:
            return True
        temp = temp.next
    return False
```

---

## 9. Full Usage Example

```python
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
# Output: 10 -> 20 -> 30 -> None

print(q.peek())   # 10

q.dequeue()
q.display()
# Output: 20 -> 30 -> None

print(q.search(30))   # True
print(q.search(100))  # False
```

---

## 10. Time Complexity

| Operation | Time |
| --------- | ---- |
| Enqueue   | O(1) |
| Dequeue   | O(1) |
| Peek      | O(1) |
| Search    | O(n) |

---

## 11. Why use Queues?

Compared to stacks or lists:

* Order is preserved (FIFO)
* Efficient insert & delete (**O(1)**)
* Used in:

  * **CPU scheduling**
  * **Printer spooling**
  * **Breadth-First Search (BFS)**
  * **Task scheduling**
  * **Message queues**


