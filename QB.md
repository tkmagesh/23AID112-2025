

### **Question 1: Dynamic Array vs Linked List Decision (Real-World System Design)**

You are designing a **student registration system** where:

* Students register at the beginning of the semester.
* Occasional drop/add operations happen during the first two weeks.
* The system frequently needs:

  * Random access to student records by index.
  * Iteration over all students to generate reports.
  * Sorting students by CGPA.

**Tasks:**

1. Would you choose an **array (dynamic array)** or a **singly linked list** to store student records? Justify your decision with time complexity comparisons.
2. Compare insertion, deletion, and random access complexities for both.
3. If the number of students doubles every year, explain the resizing implications.



---

### **Question 2: Circular Linked List – Round Robin Scheduler**

You are implementing a **Round Robin CPU scheduler**.

* Each process gets 5 ms CPU time.
* After its time slice, it goes to the end of the queue.
* The scheduling continues until all processes complete.

**Tasks:**

1. Why is a **circular linked list** suitable here?
2. Write pseudocode for one scheduling cycle.
3. What happens if you implement this using an array instead?
4. Compare the time complexity of:

   * Moving to the next process
   * Removing a completed process
5. What is the space complexity of your design?

---

### **Question 3: Undo/Redo Feature in a Text Editor**

You are implementing an **Undo/Redo system** for a text editor.

Requirements:

* Undo moves backward through actions.
* Redo moves forward.
* Deleting a middle action must be efficient.

**Tasks:**

1. Which data structure is most appropriate: singly linked list, doubly linked list, or array? Justify.
2. Explain how forward and backward traversal works.
3. What is the time complexity of:

   * Undo
   * Redo
   * Insert new action after undo
4. Why is a singly linked list less suitable?
5. Compare memory overhead of your chosen structure vs an array.

---

### **Question 4: Search and Sort in E-Commerce Inventory**

An e-commerce system stores **1 million products**.

Operations required:

* Search product by ID frequently.
* Occasionally sort products by price.
* Data rarely changes after initial load.

**Tasks:**

1. Which search algorithm would you use if data is:

   * Unsorted?
   * Sorted?
2. Compare **linear search vs binary search** in terms of time complexity.
3. Which sorting algorithm is best if:

   * Data is almost sorted?
   * Worst-case performance must be avoided?
4. Compare time complexity of:

   * Bubble Sort
   * Insertion Sort
   * Merge Sort
   * Quick Sort (average and worst case)
5. For 1 million products, justify which sorting algorithm is practically efficient and why.

---

### **Question 5: Complexity Analysis and Optimization**

A developer writes the following logic for processing an array of size `n`:

```
for i in range(n):
    for j in range(n):
        print(arr[i] + arr[j])
```

Later, the developer modifies it to:

```
for i in range(n):
    print(arr[i])
```

And then to:

```
for i in range(n):
    for j in range(i, n):
        print(arr[i] + arr[j])
```

**Tasks:**

1. Determine the time complexity of each version using Big-O notation.
2. Explain the difference between worst-case and average-case complexity.
3. If `n` becomes 10 times larger, how does runtime change for each case?
4. What is the space complexity in each case?
5. Explain why reducing nested loops significantly impacts scalability.



## **Question 6: Real-Time Stock Price Tracker**

You are building a real-time stock dashboard that:

* Continuously receives stock prices.
* Frequently appends new prices.
* Occasionally needs to remove incorrect entries.
* Often computes the maximum price in the last `k` entries.

**Tasks:**

1. Would you use an **array**, **singly linked list**, or **circular linked list**? Justify.
2. What is the time complexity of:

   * Appending a new price?
   * Removing a price at position `i`?
   * Accessing the 500th price?
3. If prices must be kept sorted at all times, which sorting strategy would you use?
4. Compare maintaining sorted order via:

   * Insertion into sorted array
   * Insertion into sorted linked list
5. Analyze the trade-off between time complexity and memory locality.

---

## **Question 7: Music Playlist Navigation System**

You are designing a music player where:

* Songs can be played forward and backward.
* The playlist loops infinitely.
* Songs can be inserted or removed while playing.

**Tasks:**

1. Which data structure best fits this scenario? Justify.
2. Explain how you would implement:

   * Next song
   * Previous song
   * Delete currently playing song
3. What is the time complexity of each operation?
4. If implemented using an array, what operations become inefficient?
5. What is the additional memory overhead of your chosen structure?

---

## **Question 8: Log Analysis Tool**

A server generates log entries continuously. At the end of the day:

* Logs are searched for specific error codes.
* Logs are sorted by timestamp.
* Duplicate logs must be detected.

**Tasks:**

1. If logs are stored in an array, what is the complexity of:

   * Linear search?
   * Binary search (after sorting)?
2. Which sorting algorithm would you prefer for large log datasets and why?
3. If duplicate detection must be efficient, would sorting first help? Explain.
4. Compare the time complexity of:

   * Sorting first + binary search
   * Repeated linear searches
5. Discuss space complexity implications of Merge Sort vs Quick Sort.

---

## **Question 9: Memory-Constrained Embedded System**

You are building firmware for a small embedded device with:

* Very limited RAM.
* Small dataset (maximum 500 elements).
* Frequent insertions and deletions in the middle.

**Tasks:**

1. Would you choose arrays or linked lists? Justify in terms of memory overhead.
2. What is the per-node memory overhead in a singly linked list?
3. If memory fragmentation is a concern, which structure is safer?
4. For small `n`, does Big-O complexity dominate practical performance? Explain.
5. Would Bubble Sort ever be acceptable in this scenario? Why or why not?

---

## **Question 10: Social Media Feed Ranking**

A social media platform:

* Loads 10,000 posts into memory.
* Ranks posts by engagement score.
* Frequently updates engagement scores.
* Needs to display top 20 posts quickly.

**Tasks:**

1. Would you repeatedly sort the entire array or use a different strategy?
2. Compare:

   * Full array sorting (Quick/Merge Sort)
   * Partial sorting
   * Maintaining a sorted structure
3. What is the time complexity of retrieving top 20 posts after:

   * Full sort?
   * Using a selection approach?
4. If scores change frequently, what is the cost of maintaining sorted order?
5. Analyze the time complexity trade-off between preprocessing and query efficiency.

---

Below are **five more scenario-based questions (11–15)** that require deeper reasoning across arrays, linked lists (singly/doubly/circular), searching, sorting, and time complexity analysis.

---

## **Question 11: Exam Result Processing System**

A university processes marks for 75,000 students.

Operations required:

* Store marks subject-wise.
* Frequently compute average, highest, and lowest marks.
* Occasionally insert late entries.
* Generate a merit list sorted by total score.

**Tasks:**

1. Would you use:

   * 1D array
   * 2D array
   * Linked list
     Justify your choice.
2. What is the time complexity of computing:

   * Class average?
   * Highest mark?
3. If merit list generation is required multiple times, which sorting algorithm is preferable and why?
4. If marks are almost sorted, which sorting algorithm performs best?
5. Analyze total complexity of:

   * Data entry
   * Sorting
   * Report generation

---

## **Question 12: Ticket Booking Waitlist Management**

A railway booking system maintains:

* Confirmed tickets
* Waitlisted passengers
* Cancellations move waitlisted passengers up

System characteristics:

* Frequent insertions at end
* Frequent deletions from middle
* Sequential traversal required

**Tasks:**

1. Which data structure is most suitable? Justify.
2. Compare complexity of:

   * Adding a new waitlisted passenger
   * Cancelling a passenger in position `k`
3. Would a circular linked list improve performance? Explain.
4. If implemented using an array, what is the worst-case cost of deletion?
5. Discuss space complexity differences between array and linked list implementations.

---

## **Question 13: Duplicate Detection in Large Dataset**

You are given an unsorted array of `n` integers (where `n` can be up to 2 million).
You must determine whether duplicates exist.

**Tasks:**

1. What is the time complexity of checking duplicates using:

   * Nested loops?
   * Sorting + single pass?
2. Compare:

   * Merge Sort
   * Quick Sort (average & worst case)
3. After sorting, what is the complexity of detecting duplicates?
4. If memory is limited, which sorting algorithm is preferable?
5. What is the overall complexity of the optimal approach?

---

## **Question 14: Browser History Implementation**

You are implementing browser navigation:

* Visit new page
* Back
* Forward
* Clear forward history when a new page is visited after going back

**Tasks:**

1. Which data structure best models this behavior?
2. Why is a doubly linked list preferable over singly linked list?
3. What is the time complexity of:

   * Visit new page?
   * Back?
   * Forward?
4. If implemented using an array, what operation becomes inefficient?
5. Compare memory overhead of pointer-based structure vs array-based implementation.

---

## **Question 15: Performance Scaling Analysis**

Consider the following sorting times observed:

| n       | Algorithm A | Algorithm B |
| ------- | ----------- | ----------- |
| 1,000   | 0.01 sec    | 0.05 sec    |
| 10,000  | 0.2 sec     | 0.4 sec     |
| 100,000 | 5 sec       | 3 sec       |

**Tasks:**

1. Based on growth rate, which algorithm is likely O(n²) and which is O(n log n)? Justify mathematically.
2. If `n` becomes 1,000,000, estimate relative performance.
3. Explain why small input sizes may not reflect asymptotic complexity.
4. Discuss cache effects and constant factors.
5. Explain difference between:

   * Big-O
   * Big-Theta
   * Big-Omega

