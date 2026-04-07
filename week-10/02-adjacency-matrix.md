# Adjacency Matrix

An **adjacency matrix** is another standard way to represent a graph, using a **2D matrix (array)**.

---

##  Definition

An **adjacency matrix** is a **V × V matrix** (where V = number of vertices) such that:

* Each row and column represent a vertex.
* The value at position **(i, j)** indicates whether there is an edge from vertex **i → j**.

---

##  Structure

For a graph with **V vertices**, we create a matrix:

[
\text{Adj}[V][V]
]

* **Adj[i][j] = 1** → edge exists
* **Adj[i][j] = 0** → no edge

For weighted graphs:

* Store weight instead of 1

---

##  Example (Undirected Graph)

Graph:

```
Vertices: 0, 1, 2, 3

Edges:
0 — 1
0 — 2
1 — 2
2 — 3
```

### Adjacency Matrix:

|   | 0 | 1 | 2 | 3 |
| - | - | - | - | - |
| 0 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 |
| 2 | 1 | 1 | 0 | 1 |
| 3 | 0 | 0 | 1 | 0 |

✔ Symmetric matrix (because graph is undirected)

---

##  Directed Graph Example

Edges:

```
0 → 1
0 → 2
1 → 2
```

### Matrix:

|   | 0 | 1 | 2 |
| - | - | - | - |
| 0 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 2 | 0 | 0 | 0 |

✔ Not symmetric

---

##  Python Implementation

```python
V = 4

# Initialize matrix with 0
graph = [[0 for _ in range(V)] for _ in range(V)]

def add_edge(u, v):
    graph[u][v] = 1
    graph[v][u] = 1  # remove for directed graph

# Add edges
add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 2)
add_edge(2, 3)

# Print matrix
for row in graph:
    print(row)
```

---

##  Time and Space Complexity

| Operation            | Complexity |
| -------------------- | ---------- |
| Space                | O(V²)      |
| Add edge             | O(1)       |
| Check edge existence | O(1)       |
| Traverse neighbors   | O(V)       |

---

##  Advantages

* Very simple representation
* Fast edge lookup → **O(1)**
* Useful for **dense graphs**
* Works well with matrix-based algorithms

---

##  Disadvantages

* Requires **O(V²)** space (wasteful for sparse graphs)
* Iterating neighbors is slower than adjacency list

---

##  Adjacency Matrix vs Adjacency List

| Feature        | Adjacency Matrix | Adjacency List   |
| -------------- | ---------------- | ---------------- |
| Space          | O(V²)            | O(V + E)         |
| Edge lookup    | O(1)             | O(degree)        |
| Best for       | Dense graphs     | Sparse graphs    |
| Implementation | Simple           | Slightly complex |

---

##  Key Point

Adjacency matrix is part of **graph representation techniques** in Unit 4  and is commonly used in:

* Floyd-Warshall Algorithm
* Graph connectivity problems
* Dense graph computations

---

##  Quick Summary

Adjacency Matrix = **2D table showing connections between all vertex pairs**

