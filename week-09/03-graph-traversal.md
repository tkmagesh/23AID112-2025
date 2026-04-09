#  **Graph Traversals**

Traversal means **visiting all vertices of a graph systematically**.

Two main methods:

* **Breadth-First Search (BFS)**
* **Depth-First Search (DFS)**

---

##  **Example Graph**

![Image](https://rkpandey.com/AlgorithmHelper/assets/dijkstra1.png)

![Image](https://deen3evddmddt.cloudfront.net/uploads/content-images/bfs.webp)

![Image](https://www.researchgate.net/publication/320163720/figure/fig2/AS%3A667648333447178%401536191175516/a-a-tree-with-a-depth-first-search-traversal-a-b-c-b-d-b-a-e-f-e-g-e-a.png)

![Image](https://deen3evddmddt.cloudfront.net/uploads/content-images/dfs.webp)

We’ll use:

```
    A
   / \
  B   C
 / \
D   E
```

---

#  **1. Breadth-First Search (BFS)**

## **Concept**

* Visits nodes **level by level**
* Uses a **queue (FIFO)**

---

## **Algorithm Steps**

1. Start from a node (e.g., A)
2. Mark it visited and enqueue it
3. While queue is not empty:

   * Dequeue node
   * Visit all unvisited neighbors
   * Enqueue them

---

## **Traversal Example**

```
BFS from A: A B C D E
```

- Level-wise:

* Level 1 → A
* Level 2 → B, C
* Level 3 → D, E

---

## **Python Code**

```python 
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

## **Applications**

* Shortest path (unweighted graphs)
* Level order traversal
* Network broadcasting

---

# **2. Depth-First Search (DFS)**

## **Concept**

* Visits nodes **as deep as possible first**
* Uses **recursion or stack (LIFO)**

---

## **Algorithm Steps**

1. Start from a node
2. Mark as visited
3. Recursively visit unvisited neighbors

---

## **Traversal Example**

```
DFS from A: A B D E C
```

---

## **Python Code (Recursive)**

```python
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
```

---

## **Applications**

* Cycle detection
* Topological sorting
* Path finding

---

#  **BFS vs DFS Comparison**

| Feature        | BFS              | DFS               |
| -------------- | ---------------- | ----------------- |
| Data structure | Queue            | Stack / Recursion |
| Traversal      | Level-wise       | Depth-wise        |
| Shortest path  | Yes (unweighted) | No guarantee      |
| Memory         | More             | Less              |
| Implementation | Iterative        | Recursive         |

---

#  **Easy Trick**

* **BFS** → Breadth → “Wide” → Level-by-level
* **DFS** → Depth → “Deep” → Go deep first

---

#  **Key Exam Points**

* BFS uses **queue**, DFS uses **stack/recursion**
* BFS finds **shortest path (unweighted graph)**
* DFS is used in **cycle detection & backtracking**
* Both have time complexity:

  ```
  O(V + E)
  ```

---

## **Quick Summary**

- BFS → level order traversal
- DFS → deep traversal

