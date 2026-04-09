
# **Tree & Graph Scenarios**

---

## **Question 1: File System Organization (Tree)**

An operating system manages files using a hierarchical structure:

* Each folder can contain files or subfolders.
* Files are accessed via paths.
* Searching for a file is frequent.

**Tasks:**

1. Why is a **tree structure** suitable for file systems?
2. What type of tree is used (general tree, binary tree)? Justify.
3. What is the time complexity of searching for a file?
4. How would traversal be used to list all files?
5. Compare tree vs graph representation for this system.

---

## **Question 2: Binary Search Tree for Student Records**

A university stores student records sorted by roll number.

Operations:

* Insert new student
* Search student
* Delete student

**Tasks:**

1. Why is a **Binary Search Tree (BST)** appropriate?
2. What is the time complexity of:

   * Insert
   * Search
   * Delete (average vs worst case)
3. What happens when the BST becomes skewed?
4. How can performance be improved?
5. Compare BST vs sorted array.

---

## **Question 3: Expression Tree Evaluation**

A compiler evaluates arithmetic expressions using trees.

Example: `(A + B) * C`

**Tasks:**

1. What is an **expression tree**?
2. How is it constructed from postfix expression?
3. Which traversal is used for evaluation?
4. What is the time complexity of evaluation?
5. Compare tree-based evaluation vs stack-based evaluation.

---

## **Question 4: Organization Hierarchy (Tree Traversals)**

A company hierarchy:

* CEO → Managers → Employees
* Need to:

  * Print hierarchy
  * Count employees
  * Find reporting chain

**Tasks:**

1. Which traversal is suitable for:

   * Listing all employees?
   * Printing hierarchy level-wise?
2. Compare:

   * Preorder
   * Inorder
   * Postorder
   * Level-order traversal
3. What is the time complexity of each traversal?
4. How would you find depth of hierarchy?
5. Analyze space complexity.

---

## **Question 5: Network Routing (Graph)**

A computer network consists of routers connected via links.

* Each link has a cost (latency).
* Need to find shortest path between two routers.

**Tasks:**

1. Why is a **graph** suitable here?
2. Which algorithm would you use for shortest path?
3. What is the time complexity of the algorithm?
4. Difference between weighted and unweighted graphs.
5. Compare adjacency list vs adjacency matrix representation.

---

## **Question 6: Social Media Connections (Graph)**

A social media platform:

* Users are nodes.
* Friendships are edges.
* Need to:

  * Find mutual friends
  * Suggest new friends

**Tasks:**

1. Is the graph directed or undirected? Justify.
2. How would you find mutual friends?
3. Which traversal is suitable for friend suggestions?
4. What is the time complexity of traversal?
5. Compare graph vs tree representation.

---

## **Question 7: Web Crawling System (Graph Traversal)**

A search engine crawls web pages:

* Pages are nodes
* Links are edges

**Tasks:**

1. Why is graph traversal required?
2. Compare BFS vs DFS for crawling.
3. Which traversal ensures level-wise exploration?
4. What is the time complexity?
5. How do you avoid visiting the same page twice?

---

## **Question 8: Minimum Spanning Tree in City Planning**

A city plans to connect all buildings with minimum cable cost.

**Tasks:**

1. What is a **Minimum Spanning Tree (MST)**?
2. Which algorithms can be used?
3. Compare Prim’s vs Kruskal’s algorithm.
4. What is the time complexity?
5. Why is MST optimal for this problem?

---

## **Question 9: Cycle Detection in Graph**

A system checks for deadlocks:

* Processes are nodes
* Dependencies are edges

**Tasks:**

1. Why is cycle detection important?
2. How can cycles be detected in:

   * Directed graph?
   * Undirected graph?
3. Which traversal is used?
4. What is the time complexity?
5. What happens if a cycle exists?

---

## **Question 10: Shortest Path in Navigation System**

A GPS system:

* Maps roads as graph
* Finds shortest route

**Tasks:**

1. Which algorithm is most suitable?
2. What if negative weights exist?
3. Compare:

   * Dijkstra’s Algorithm
   * Bellman-Ford Algorithm
4. What is the time complexity?
5. Analyze real-world constraints.

---

## **Question 11: Binary Tree vs Binary Search Tree**

A developer must choose between binary tree and BST.

**Tasks:**

1. Define binary tree and BST.
2. What are key differences?
3. When is BST preferred?
4. Compare search complexity.
5. Give real-world use cases.

---

## **Question 12: Graph Representation Choice**

A system stores a sparse graph with millions of nodes.

**Tasks:**

1. Which representation is better:

   * Adjacency list
   * Adjacency matrix
2. Compare space complexity.
3. Compare traversal performance.
4. When is adjacency matrix preferred?
5. Analyze scalability.

---

## **Question 13: DFS vs BFS in Maze Solving**

A robot navigates a maze.

**Tasks:**

1. Compare DFS and BFS approaches.
2. Which guarantees shortest path?
3. What is time complexity?
4. What is space complexity?
5. When is DFS preferable?

---

## **Question 14: Topological Sorting (Graph)**

A project has tasks with dependencies.

**Tasks:**

1. What is topological sorting?
2. When is it applicable?
3. Which algorithms can be used?
4. What is time complexity?
5. What happens if a cycle exists?

---

## **Question 15: Tree Height and Balance**

A database uses tree structures for indexing.

**Tasks:**

1. What is tree height?
2. How does height affect performance?
3. What is a balanced tree?
4. Compare balanced vs skewed tree.
5. Why are balanced trees preferred?

---
