
# Circular Queue Implementation 

A **Circular Queue** connects the last position of the queue back to the first position to efficiently reuse space.

### Key Operations

* `enqueue()` – insert element
* `dequeue()` – remove element
* `display()` – show elements

### Full Python Program

```python
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(data, "inserted")

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
            return

        removed = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(removed, "removed")

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# Example
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

cq.display()

cq.dequeue()
cq.display()
```

---

# 2. Double Ended Queue (Deque) Implementation 

A **Deque** allows insertion and deletion from **both ends**.

### Operations

* `insert_front()`
* `insert_rear()`
* `delete_front()`
* `delete_rear()`

---

### Full Python Program

```python
class Deque:
    def __init__(self, size):
        self.size = size
        self.deque = [None] * size
        self.front = -1
        self.rear = -1

    def insert_front(self, data):
        if (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1):
            print("Deque Overflow")
            return

        if self.front == -1:
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1

        self.deque[self.front] = data
        print(data, "inserted at front")

    def insert_rear(self, data):
        if (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1):
            print("Deque Overflow")
            return

        if self.front == -1:
            self.front = self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1

        self.deque[self.rear] = data
        print(data, "inserted at rear")

    def delete_front(self):
        if self.front == -1:
            print("Deque Underflow")
            return

        removed = self.deque[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1

        print(removed, "removed from front")

    def delete_rear(self):
        if self.front == -1:
            print("Deque Underflow")
            return

        removed = self.deque[self.rear]

        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1

        print(removed, "removed from rear")

    def display(self):
        if self.front == -1:
            print("Deque empty")
            return

        i = self.front
        while True:
            print(self.deque[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# Example
dq = Deque(5)

dq.insert_rear(10)
dq.insert_rear(20)
dq.insert_front(5)

dq.display()

dq.delete_front()
dq.delete_rear()

dq.display()
```

---

# Circular Queue vs Deque

| Feature   | Circular Queue          | Deque                           |
| --------- | ----------------------- | ------------------------------- |
| Insert    | Rear only               | Front & Rear                    |
| Delete    | Front only              | Front & Rear                    |
| Structure | Circular                | Circular                        |
| Use Case  | CPU scheduling, buffers | Sliding window, task scheduling |

