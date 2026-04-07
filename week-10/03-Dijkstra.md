### Shortest Path Algorithms – Dijkstra’s Algorithm 

Dijkstra’s Algorithm is one of the most important **greedy algorithms** used in graph theory to find the **shortest path from a single source vertex to all other vertices** in a graph.


---

# 1. What is Dijkstra’s Algorithm?

Dijkstra’s Algorithm computes the **minimum distance (shortest path)** from a **source node** to all other nodes in a **weighted graph**.

### ✔️ Key Characteristics:

* Works on **weighted graphs**
* Handles **non-negative edge weights only**
* Can be used on **directed or undirected graphs**

---

# 2. Core Idea (Greedy Approach)

At every step:

* Select the vertex with the **smallest known distance**
* Update (relax) its neighbors

👉 It always chooses the **locally optimal solution**, hoping it leads to a **globally optimal solution**

---

# 3. Terminology

* **Distance array (`dist[]`)** → stores shortest distance from source
* **Visited set** → nodes already finalized
* **Relaxation** → updating shorter paths:

[
\text{if } dist[u] + weight(u,v) < dist[v] \Rightarrow dist[v] = dist[u] + weight(u,v)
]

---

# 4. Step-by-Step Algorithm

### Input:

* Graph ( G(V, E) )
* Source vertex ( S )

### Steps:

1. Initialize:

   * `dist[S] = 0`
   * All other vertices = ∞
   * Mark all vertices unvisited

2. Repeat:

   * Pick the **unvisited vertex with smallest distance**
   * Mark it as **visited**
   * Update distances of its neighbors

3. Stop when all vertices are visited

---

# 5. Example

Consider the graph:

```
      (A)
     /   \
   1/     \4
   /       \
 (B)---2---(C)
   \       /
   5\     /1
     \   /
      (D)
```

### Source = A

| Step  | Node Picked | Updated Distances  |
| ----- | ----------- | ------------------ |
| Start | A           | A=0, B=∞, C=∞, D=∞ |
| 1     | A           | B=1, C=4           |
| 2     | B           | C=3, D=6           |
| 3     | C           | D=4                |
| 4     | D           | Final              |

### ✅ Final shortest distances:

* A → B = 1
* A → C = 3
* A → D = 4

---

# 6. Pseudocode

```text
Dijkstra(G, source):
    for each vertex v:
        dist[v] = ∞
        visited[v] = false

    dist[source] = 0

    repeat V times:
        u = vertex with minimum dist not visited
        mark u as visited

        for each neighbor v of u:
            if not visited[v] and dist[u] + weight(u,v) < dist[v]:
                dist[v] = dist[u] + weight(u,v)
```

---

# 7. Python Implementation

```python
import heapq

def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0
    
    pq = [(0, source)]  # (distance, node)

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist


# Example graph (adjacency list)
graph = {
    0: [(1,1), (2,4)],
    1: [(2,2), (3,5)],
    2: [(3,1)],
    3: []
}

print(dijkstra(graph, 0))
```

---

# 8. Time Complexity

| Implementation            | Complexity         |
| ------------------------- | ------------------ |
| Array-based               | (O(V^2))           |
| Min Heap (Priority Queue) | (O((V + E)\log V)) |

👉 Most efficient version uses a **priority queue (heap)**

---

# 9. Advantages

✔️ Efficient for large graphs
✔️ Guarantees optimal shortest path
✔️ Widely used in real-world systems

---

# 10. Limitations

❌ Does **not work with negative weights**
❌ Cannot detect negative cycles

👉 For negative weights → use **Bellman-Ford Algorithm**

---

# 11. Real-Life Applications

* Google Maps / GPS navigation
* Network routing (Internet packets)
* Flight route optimization
* Robotics path planning

---

# 12. Comparison with Other Shortest Path Algorithms

| Algorithm      | Handles Negative Weights | Complexity |
| -------------- | ------------------------ | ---------- |
| Dijkstra       | ❌ No                     | Fast       |
| Bellman-Ford   | ✔️ Yes                   | Slower     |
| Floyd-Warshall | ✔️ Yes                   | All-pairs  |

---

# Summary

Dijkstra’s Algorithm is a **greedy shortest path algorithm** that:

* Works on **non-negative weighted graphs**
* Uses **relaxation and priority queue**
* Finds **optimal shortest paths efficiently**

