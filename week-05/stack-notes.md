

# Stack (Linked List Implementation)

## 1. What is a Stack?

A **stack** is a linear data structure that follows the **LIFO** principle:

> **Last In, First Out**

Elements are:

* **Inserted (push)** at the **top**
* **Removed (pop)** from the **top**

```
Top -> [data]
        [data]
        [data]
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

## 3. Stack Implementation (Using Linked List)

```python
class Stack:
    def __init__(self):
        self.top = None
```

---

## 4. Push (Insert Element)

```python
def push(self, data):
    new_node = Node(data)
    new_node.next = self.top
    self.top = new_node
```

---

## 5. Pop (Remove Element)

```python
def pop(self):
    if self.top is None:
        print("Stack is empty")
        return

    temp = self.top
    self.top = temp.next
    return temp.data
```

---

## 6. Peek (Top Element)

```python
def peek(self):
    if self.top is None:
        print("Stack is empty")
        return None
    return self.top.data
```

---

## 7. Display the Stack

```python
def display(self):
    temp = self.top
    while temp:
        print(temp.data)
        temp = temp.next
```

---

## 8. Search in Stack

```python
def search(self, key):
    temp = self.top
    while temp:
        if temp.data == key:
            return True
        temp = temp.next
    return False
```

---

## 9. Full Usage Example

```python
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
# Output:
# 30
# 20
# 10

print(s.peek())   # 30

s.pop()
s.display()
# Output:
# 20
# 10

print(s.search(20))   # True
print(s.search(100))  # False
```

---

## 10. Time Complexity

| Operation | Time |
| --------- | ---- |
| Push      | O(1) |
| Pop       | O(1) |
| Peek      | O(1) |
| Search    | O(n) |

---

## 11. Why use Stacks?

Compared to queues or lists:

* Simple **LIFO** ordering
* Very fast insert & delete (**O(1)**)
* Used in:

  * **Function calls / recursion**
  * **Undo / redo operations**
  * **Expression evaluation**
  * **Backtracking**
  * **Syntax parsing**

