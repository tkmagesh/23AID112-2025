

# **Queue & Stack Scenarios**

---

## **Question 1: Call Center Management System (Queue)**

A customer support center handles incoming calls:

* Calls arrive continuously.
* The first caller should be served first.
* Calls may be dropped if waiting time exceeds a threshold.

**Tasks:**

1. Which data structure is most appropriate: simple queue, circular queue, or priority queue? Justify.
2. What is the time complexity of:

   * Enqueue (new call)?
   * Dequeue (serving a call)?
3. How would you handle high call volume efficiently?
4. What happens if implemented using an array with fixed size?
5. Compare linear queue vs circular queue in this scenario.

---

## **Question 2: Print Job Scheduling (Queue)**

A printer receives multiple print requests:

* Jobs are processed in order of arrival.
* Urgent jobs may need priority.

**Tasks:**

1. Which data structure would you use:

   * Simple queue
   * Priority queue
     Justify your answer.
2. What is the complexity of inserting a job in a priority queue?
3. How does job reordering affect performance?
4. Compare FIFO vs priority-based scheduling.
5. What is the space complexity of your system?

---

## **Question 3: Web Server Request Handling (Queue)**

A web server handles incoming HTTP requests:

* Requests arrive unpredictably.
* They are processed in arrival order.
* The system must scale under heavy load.

**Tasks:**

1. Why is a queue suitable here?
2. What type of queue implementation would you use for scalability?
3. What happens when the queue becomes full?
4. Compare array-based vs linked list queue implementation.
5. Analyze time and space complexity.

---

## **Question 4: Undo Feature in Application (Stack)**

A graphics editor supports undo functionality:

* Each action is stored.
* Undo removes the last action.

**Tasks:**

1. Why is a stack ideal for this feature?
2. What is the complexity of:

   * Push (new action)?
   * Pop (undo)?
3. How would you extend this to support redo?
4. What happens if implemented using a queue?
5. Compare stack vs doubly linked list for this system.

---

## **Question 5: Expression Evaluation System (Stack)**

A calculator evaluates expressions like:

* `(A + B) * C`
* `A + (B * C)`

**Tasks:**

1. Why is a stack used for expression evaluation?
2. Explain infix → postfix conversion using stack.
3. What is the time complexity of evaluation?
4. What happens if recursion is used instead of stack?
5. Compare stack-based vs recursive approach.

---

## **Question 6: Ticket Counter System (Queue)**

At a railway station:

* Passengers stand in line.
* First person gets ticket first.
* VIP passengers may bypass the queue.

**Tasks:**

1. Which data structure would you use to handle VIP priority?
2. Compare normal queue vs priority queue.
3. What is the time complexity of insertion and deletion?
4. How would starvation be avoided?
5. Analyze fairness vs efficiency trade-offs.

---

## **Question 7: Browser Back Button (Stack)**

A browser tracks visited pages:

* Back button goes to the previous page.
* Forward button moves ahead.

**Tasks:**

1. Why are stacks used for this feature?
2. How many stacks are required? Explain.
3. What is the complexity of:

   * Visiting a new page?
   * Going back?
4. What happens to forward history when a new page is visited?
5. Compare stack vs linked list implementation.

---

## **Question 8: CPU Task Scheduling (Queue vs Stack)**

An operating system schedules tasks:

* Tasks arrive dynamically.
* Some tasks must be executed immediately (LIFO behavior).

**Tasks:**

1. Compare queue-based vs stack-based scheduling.
2. In what scenario is stack preferable?
3. What is the time complexity of task insertion/removal?
4. How does scheduling affect system performance?
5. Compare real-world use cases of both.

---

## **Question 9: Balanced Parentheses Checker (Stack)**

A compiler checks syntax:

* Every opening bracket must have a matching closing bracket.

**Tasks:**

1. Why is a stack suitable for this problem?
2. Write algorithm logic using stack.
3. What is the time complexity?
4. What happens if queue is used instead?
5. Analyze space complexity.

---

## **Question 10: Circular Buffer in Streaming (Circular Queue)**

A video streaming system:

* Stores last `N` frames.
* New frames overwrite old ones.

**Tasks:**

1. Why is a circular queue ideal here?
2. What is the time complexity of:

   * Insert frame?
   * Remove frame?
3. What happens when buffer is full?
4. Compare circular queue vs linear queue.
5. Analyze memory efficiency.

---

## **Question 11: Task History Tracking (Stack)**

A software tracks user actions:

* Users perform multiple operations.
* They may revert multiple steps.

**Tasks:**

1. Why is stack suitable?
2. What is complexity of storing history?
3. What happens when stack overflows?
4. Compare fixed-size vs dynamic stack.
5. Analyze memory usage.

---

## **Question 12: Multi-User Printer Queue (Queue)**

Multiple users send print jobs:

* Jobs must be processed fairly.
* Some departments have priority.

**Tasks:**

1. Which data structure would you choose?
2. Compare multiple queues vs single priority queue.
3. What is complexity of scheduling?
4. How would you prevent starvation?
5. Analyze scalability.

---

## **Question 13: Recursion vs Stack (Stack)**

A program calculates factorial using recursion.

**Tasks:**

1. Explain how recursion internally uses stack.
2. Compare recursive vs iterative (stack-based) approach.
3. What is time and space complexity?
4. What is stack overflow?
5. When is recursion not preferred?

---

## **Question 14: Breadth-First Search (Queue)**

A graph traversal system:

* Visits nodes level by level.

**Tasks:**

1. Why is queue used in BFS?
2. What is time complexity?
3. Compare BFS vs DFS (stack-based).
4. What happens if stack is used instead?
5. Analyze space complexity.

---

## **Question 15: Depth-First Search (Stack)**

A maze-solving robot:

* Explores as deep as possible before backtracking.

**Tasks:**

1. Why is stack suitable?
2. Compare DFS using stack vs recursion.
3. What is time complexity?
4. When does DFS fail to find optimal path?
5. Compare DFS vs BFS in real-world scenarios.

