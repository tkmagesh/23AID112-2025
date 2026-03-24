
#  **Binary Trees**

## **1. What is a Binary Tree?**

A **binary tree** is a hierarchical data structure where:

* Each node has **at most 2 children**

  * Left child
  * Right child

 Formally:

* Each node contains:

  * Data
  * Pointer/reference to left child
  * Pointer/reference to right child

---

## **2. Types of Binary Trees**

### **(a) Full Binary Tree**

* Every node has either **0 or 2 children**

### **(b) Complete Binary Tree**

* All levels are filled except possibly the last
* Last level is filled from **left to right**

### **(c) Perfect Binary Tree**

* All internal nodes have 2 children
* All leaves are at the same level

### **(d) Skewed Binary Tree**

* All nodes are on one side (left or right)

---

## **3. Representation of Binary Tree**

### **(A) Array Representation**

Used mostly for **complete binary trees**

If node is at index `i`:

* Left child → `2i + 1`
* Right child → `2i + 2`
* Parent → `(i - 1) // 2`

#### Example:

```
Tree:
      A
     / \
    B   C
   / \
  D   E

Array:
[A, B, C, D, E]
```

---

### **(B) Linked List Representation**

Each node contains:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

---

## **4. Binary Tree Traversals**

Consider this tree:

```
        A
       / \
      B   C
     / \
    D   E
```

---

### **(1) Preorder Traversal (Root → Left → Right)**

**Steps:**

1. Visit root
2. Traverse left subtree
3. Traverse right subtree

**Output:**

```
A B D E C
```

**Code:**

```python
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
```

---

### **(2) Inorder Traversal (Left → Root → Right)**

**Output:**

```
D B E A C
```

**Code:**

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
```

---

### **(3) Postorder Traversal (Left → Right → Root)**

**Output:**

```
D E B C A
```

**Code:**

```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
```

---

### **(4) Level Order Traversal (BFS)**

**Output:**

```
A B C D E
```

**Code:**

```python
from collections import deque

def level_order(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

---

## **5. Example: Creating a Binary Tree in Python**

```python
# Creating nodes
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')

# Traversals
print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)

print("\nLevel Order:")
level_order(root)
```

---

## **6. Key Properties (Important for Exams)**

* Maximum nodes at level `l`:

  ```
  2^l
  ```

* Maximum nodes in tree of height `h`:

  ```
  2^(h+1) - 1
  ```

* Minimum height for `n` nodes:

  ```
  log2(n+1) - 1
  ```

---

## **7. Common Viva Questions**

* Difference between **full, complete, and perfect tree**
* Why array representation is inefficient for skewed trees
* Difference between **DFS (pre/in/post)** and **BFS (level order)**
* Applications:

  * Expression trees
  * Binary Search Trees
  * Heaps

---

## **Quick Summary**

* Binary tree = max 2 children per node
* Two representations: **array & linked list**
* 4 main traversals: **pre, in, post, level**
* Widely used in searching, sorting, parsing


Here are **domain-specific use cases of Binary Trees**—structured the way examiners expect (application + explanation + example):

---

#  **Domain-Specific Use Cases of Binary Trees**

## **1. Compiler Design (Expression Trees)**

### **Use Case**

Binary trees represent **arithmetic and logical expressions**.

### **How it works**

* Internal nodes → operators (`+, -, *, /`)
* Leaf nodes → operands

### **Example**

Expression: `(A + B) * C`

```
        *
       / \
      +   C
     / \
    A   B
```

 Used in:

* Expression evaluation
* Syntax parsing
* Code optimization

---

## **2. Database Systems (Indexing using B-Trees / BST concepts)**

### **Use Case**

Efficient **search, insert, delete operations** in databases.

### **How it works**

* Data stored in sorted structure
* Searching reduces from **O(n) → O(log n)**

 Used in:

* Database indexing
* File systems

 Note: Real systems use **B-Trees**, but concept originates from binary search trees.

---

## **3. Operating Systems (Scheduling & Memory Management)**

### **Use Case**

Binary trees help in:

* Process scheduling
* Memory allocation

### **Example**

* **Binary Heap (complete binary tree)** used in:

  * Priority scheduling
  * CPU task management

 Ensures:

* Fast access to highest priority task

---

## **4. Networking (Routing Algorithms)**

### **Use Case**

Binary trees support **decision-making and routing logic**.

### **Example**

* Routing tables can use tree-like structures
* Decision trees for packet forwarding

 Helps in:

* Fast lookup
* Efficient path decisions

---

## **5. Artificial Intelligence & Machine Learning**

### **Use Case**

**Decision Trees** (a type of binary tree)

### **How it works**

* Each node → decision condition
* Left/Right → outcomes

### **Example**

```
        Age > 18?
        /      \
      Yes       No
     /            \
  Adult         Minor
```

 Used in:

* Classification problems
* Regression models

---

## **6. Data Compression (Huffman Coding)**

### **Use Case**

Binary trees are used to **compress data efficiently**.

### **How it works**

* Characters stored as leaves
* Path from root → binary code

### **Example**

* Left edge → `0`
* Right edge → `1`

 Used in:

* ZIP files
* Image/audio compression

---

## **7. Computer Graphics (Scene Graphs / Rendering)**

### **Use Case**

Binary trees organize objects in a scene.

### **Example**

* **Binary Space Partitioning (BSP Trees)**

 Used in:

* Game engines
* Rendering pipelines

---

## **8. Searching Algorithms (Binary Search Tree - BST)**

### **Use Case**

Efficient searching and sorting.

### **How it works**

* Left subtree < root
* Right subtree > root

 Operations:

* Search → O(log n) (balanced)
* Insert/Delete → efficient

---

## **9. Expression Evaluation in Calculators**

### **Use Case**

Used internally in:

* Compilers
* Calculators

Converts:

* Infix → Tree → Evaluate

---

## **10. Hierarchical Data Representation**

### **Use Case**

Represents hierarchical relationships.

### **Example**

* File systems (simplified)
* Organization structures

---

#  **Quick Summary (Exam Ready)**

| Domain          | Use                    |
| --------------- | ---------------------- |
| Compiler Design | Expression trees       |
| Databases       | Indexing (BST/B-Trees) |
| OS              | Scheduling (heap)      |
| AI/ML           | Decision trees         |
| Compression     | Huffman coding         |
| Networking      | Routing decisions      |
| Graphics        | BSP trees              |
| Searching       | BST                    |

---



