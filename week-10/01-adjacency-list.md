# Adjacency List

An **adjacency list** is a fundamental way to represent a graph in data structures, especially when dealing with **sparse graphs** (graphs with fewer edges).

---

##  Definition

An **adjacency list** represents a graph as an array (or list) of lists.
Each index (or node) stores a list of all the vertices directly connected to it.

In simple terms:

> For every vertex, we keep a list of its neighbors.

---

##  Structure

If a graph has **V vertices**, the adjacency list is an array of size **V**, where:

* Each element contains a list of adjacent vertices.
* It can be implemented using:

  * Arrays of linked lists
  * Arrays of dynamic lists (like Python lists)

---

##  Example

Consider this graph:

```
Vertices: 0, 1, 2, 3

Edges:
0 — 1
0 — 2
1 — 2
2 — 3
```

### Adjacency List Representation:

```
0 → 1 → 2
1 → 0 → 2
2 → 0 → 1 → 3
3 → 2
```

Or in table form:

| Vertex | Adjacent Nodes |
| ------ | -------------- |
| 0      | 1, 2           |
| 1      | 0, 2           |
| 2      | 0, 1, 3        |
| 3      | 2              |

---

##  For Directed Graph

If edges are **directed**, only store outgoing edges:

Example:

```
0 → 1
0 → 2
1 → 2
```

Adjacency list:

```
0 → 1 → 2
1 → 2
2 → (empty)
```

---

##  Python Implementation

```python
# Number of vertices
V = 4

# Create adjacency list
graph = [[] for _ in range(V)]

# Add edges
def add_edge(u, v):
    graph[u].append(v)
    graph[v].append(u)  # remove this line for directed graph

add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 2)
add_edge(2, 3)

# Print adjacency list
for i in range(V):
    print(f"{i} -> {graph[i]}")
```

---

##  Time and Space Complexity

| Operation       | Complexity          |
| --------------- | ------------------- |
| Space           | O(V + E)            |
| Add edge        | O(1)                |
| Check adjacency | O(degree of vertex) |

---

##  Advantages

* Efficient for **sparse graphs**
* Saves memory compared to adjacency matrix
* Easy to iterate through neighbors

---

##  Disadvantages

* Checking if an edge exists is slower than matrix
* Slightly complex structure compared to matrix

---

##  Adjacency List vs Adjacency Matrix

| Feature     | Adjacency List | Adjacency Matrix |
| ----------- | -------------- | ---------------- |
| Space       | O(V + E)       | O(V²)            |
| Best for    | Sparse graphs  | Dense graphs     |
| Edge lookup | Slower         | Faster (O(1))    |

---

##  Key Points

Adjacency list is part of **Graph representation** in Unit 4  and is widely used in algorithms like:

* BFS (Breadth-First Search)
* DFS (Depth-First Search)
* Dijkstra’s Algorithm

