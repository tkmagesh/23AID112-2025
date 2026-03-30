
#  **Graphs – Directed and Undirected**

## **1. What is a Graph?**

A **graph** is a non-linear data structure consisting of:

* **Vertices (nodes)**
* **Edges (connections between nodes)**

Represented as:

```
G = (V, E)
```

* V → set of vertices
* E → set of edges

---

#  **2. Undirected Graph**

## **Definition**

An **undirected graph** is a graph where:

* Edges have **no direction**
* Connection is **bidirectional**

---

## **Structure**

![Image](https://study.com/cimages/multimages/16/simple_graph4744763281979443882.png)

![Image](https://www.researchgate.net/publication/343090040/figure/fig1/AS%3A917194661703682%401595687656539/Representation-of-an-undirected-graph-with-its-adjacency-matrix.ppm)

![Image](https://www.researchgate.net/publication/281783677/figure/fig2/AS%3A667643879116815%401536190113966/A-graph-with-five-nodes-and-six-non-directional-edges.ppm)

![Image](https://cdn.prod.website-files.com/65d609edcc331dd0e4eb519b/693c611e4105fe0c1e32f427_graphs.png)

---

## **Example**

```
A ----- B
|       |
C ----- D
```

👉 Edge (A, B) = (B, A)

---

## **Properties**

* Degree = number of edges connected to a node
* No concept of incoming/outgoing edges
* Edges are unordered pairs

---

## **Applications**

* Social networks (friendship)
* Road networks (two-way roads)
* Network topology

---

# **3. Directed Graph (Digraph)**

## **Definition**

A **directed graph** is a graph where:

* Each edge has a **direction**
* Represented using arrows

---

## **Structure**

![Image](https://upload.wikimedia.org/wikipedia/commons/2/23/Directed_graph_no_background.svg)

![Image](https://study.com/cimages/multimages/16/adjacency_matrix7866713320554367537.png)

![Image](https://mathinsight.org/media/image/image/small_directed_network_labeled.png)

![Image](https://cdn.prod.website-files.com/65d609edcc331dd0e4eb519b/693c611e4105fe0c1e32f427_graphs.png)

---

## **Example**

```id="gtwsf6"
A → B → C
↑       ↓
D ←------
```

👉 Edge (A → B) ≠ (B → A)

---

## **Properties**

* Each node has:

  * **In-degree** (incoming edges)
  * **Out-degree** (outgoing edges)
* Edges are ordered pairs

---

## **Applications**

* Web links (page → page)
* One-way roads
* Task scheduling (dependency graphs)

---

# ⚖️ **Directed vs Undirected Graph**

| Feature        | Undirected Graph | Directed Graph         |
| -------------- | ---------------- | ---------------------- |
| Edge direction | No direction     | Has direction          |
| Edge type      | (A, B) = (B, A)  | (A, B) ≠ (B, A)        |
| Degree         | Only degree      | In-degree & Out-degree |
| Representation | Symmetric        | Asymmetric             |
| Example        | Friendship       | Twitter follow         |

---

# 🔑 **Important Concepts**

## **Degree of Vertex**

* Undirected:

  ```
  Degree = number of edges
  ```

* Directed:

  ```
  In-degree = incoming edges  
  Out-degree = outgoing edges
  ```

---

## **Path**

* A sequence of vertices connected by edges

---

## **Cycle**

* A path that starts and ends at the same vertex

---


## **Note**

*An undirected graph has bidirectional edges, while a directed graph has edges with a specific direction.*

