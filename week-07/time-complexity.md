Big-O notation is just a **way to describe how an algorithm’s runtime grows as the input size grows**. It ignores machine speed and small constants and focuses on the *trend*.

Think of it as answering:

> “If my input doubles, how much slower does this get?”

---

## The idea (in plain terms)

* **n** = size of the input
* **O(f(n))** = how the runtime scales with *n* in the worst case
* We care about:

  * growth rate
  * worst-case behavior
* We **ignore**:

  * constants (2n → O(n))
  * lower-order terms (n² + n → O(n²))

---

## Common Big-O time complexities (from fastest to slowest)

| Big-O      | Name         | Example                        |
| ---------- | ------------ | ------------------------------ |
| O(1)       | Constant     | Access array element           |
| O(log n)   | Logarithmic  | Binary search                  |
| O(n)       | Linear       | Loop through list              |
| O(n log n) | Linearithmic | Merge sort                     |
| O(n²)      | Quadratic    | Nested loops                   |
| O(2ⁿ)      | Exponential  | Recursive subsets              |
| O(n!)      | Factorial    | Traveling salesman brute force |

---

## O(1) — Constant Time

Runtime does **not** change with input size.

```python
def get_first(arr):
    return arr[0]
```

* Whether `arr` has 10 items or 10 million → same time
* **O(1)**

---

## O(n) — Linear Time

Runtime grows **proportionally** with input size.

```python
def find_max(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val
```

* One loop over `n` elements
* **O(n)**

---

## O(n²) — Quadratic Time

Usually caused by **nested loops**.

```python
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
```

* n × n operations
* If `n = 1000`, ~1,000,000 operations
* **O(n²)**

---

## O(log n) — Logarithmic Time

Input is cut in half each step.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

* Each step removes half the search space
* Very fast for large data
* **O(log n)**

---

## O(n log n) — Linearithmic Time

Common in **efficient sorting algorithms**.

```python
def sort_numbers(arr):
    return sorted(arr)  # Timsort → O(n log n)
```

* Better than O(n²)
* Used by merge sort, quicksort (average case)

---

## O(2ⁿ) — Exponential Time

Grows **very fast** — usually recursion with branching.

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

* Each call spawns two more
* Becomes unusable quickly
* **O(2ⁿ)**

---

## Dropping constants & lower terms

```python
def example(arr):
    for x in arr:        # O(n)
        print(x)

    for y in arr:        # O(n)
        print(y)
```

* O(n + n) → **O(n)**

```python
def example(arr):
    for x in arr:        # O(n)
        for y in arr:    # O(n)
            print(x, y)
    for z in arr:        # O(n)
        print(z)
```

* O(n² + n) → **O(n²)**

---

## Rule of thumb when analyzing code

1. Loops → O(n)
2. Nested loops → O(n²), O(n³), …
3. Halving the problem → O(log n)
4. Recursion? Count how many calls are made
5. Keep the **largest term only**

---

## Why Big-O matters

* Helps choose the **right algorithm**
* Predicts performance at scale
* Explains why “working code” can still be **slow**

------



## The Big-O calculation checklist

When you see code, do this **in order**:

### 1️. Identify what *n* is

Ask:

> “What grows?”

Usually:

* length of a list
* size of input
* number of nodes / elements

```python
n = len(arr)
```

---

### 2️. Count operations relative to *n*

You don’t count exact steps — just how they **scale**.

* One loop over n → **O(n)**
* Two loops one after another → **O(n + n)**
* Nested loops → **O(n × n)**

---

### 3️. Handle loops

#### Single loop

```python
for x in arr:
    print(x)
```

* Runs n times → **O(n)**

---

#### Nested loops

```python
for i in arr:
    for j in arr:
        print(i, j)
```

* n × n → **O(n²)**

---

#### Loop that halves input

```python
while n > 1:
    n = n // 2
```

* n → n/2 → n/4 → ...
* **O(log n)**

---

### 4️. Handle sequential code (add)

```python
for x in arr:      # O(n)
    print(x)

for y in arr:      # O(n)
    print(y)
```

* O(n + n) → **O(n)**

Always **add first**, simplify later.

---

### 5️. Handle nested code (multiply)

```python
for i in arr:          # n
    for j in arr:      # n
        print(i, j)
```

* O(n × n) → **O(n²)**

---

### 6️. Drop constants and lower terms

```python
O(3n + 10) → O(n)
O(n² + n) → O(n²)
O(100) → O(1)
```

Big-O only cares about **dominant growth**.

---

## Step-by-step examples

---

## Example 1: Simple loop

```python
def example(arr):
    total = 0
    for x in arr:
        total += x
    return total
```

**Step-by-step**

1. n = length of `arr`
2. Loop runs n times
3. Each iteration is O(1)
4. Total → **O(n)**

---

## Example 2: Two loops, not nested

```python
def example(arr):
    for x in arr:
        print(x)

    for y in arr:
        print(y)
```

**Steps**

1. n = len(arr)
2. First loop → O(n)
3. Second loop → O(n)
4. O(n + n) → **O(n)**

---

## Example 3: Nested loops

```python
def example(arr):
    for i in arr:
        for j in arr:
            print(i, j)
```

**Steps**

1. n = len(arr)
2. Outer loop → n
3. Inner loop → n
4. n × n → **O(n²)**

---

## Example 4: Mixed nested + sequential

```python
def example(arr):
    for i in arr:           # O(n)
        for j in arr:       # O(n)
            print(i, j)

    for k in arr:           # O(n)
        print(k)
```

**Steps**

1. Nested part → O(n²)
2. Sequential loop → O(n)
3. O(n² + n) → **O(n²)**

---

## Example 5: Logarithmic loop

```python
def example(n):
    while n > 1:
        n = n // 2
```

**Steps**

1. Each iteration halves n
2. Number of steps = how many times you divide by 2
3. That’s log₂(n)
4. **O(log n)**

---

## Example 6: Binary search (full breakdown)

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
```

**Steps**

1. n = len(arr)
2. Each loop cuts search space in half
3. Max number of iterations = log₂(n)
4. Work inside loop = O(1)
5. Total → **O(log n)**

---

## Example 7: Recursive function

```python
def sum_recursive(arr, i):
    if i == len(arr):
        return 0
    return arr[i] + sum_recursive(arr, i + 1)
```

**Steps**

1. One recursive call per element
2. Depth of recursion = n
3. Work per call = O(1)
4. **O(n)**

---

## Example 8: Exponential recursion

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

**Steps**

1. Each call spawns 2 more
2. Tree of calls doubles each level
3. Growth ≈ 2ⁿ
4. **O(2ⁿ)**

---

## Mental shortcuts (very useful)

* One loop → **O(n)**
* Loop inside loop → **O(n²)**
* Halving input → **O(log n)**
* Loop + halving → **O(n log n)**
* Recursive branching → usually exponential

---

## Final sanity check

Ask:

> “If input size becomes **10× bigger**, what happens to runtime?”

* ~10× slower → O(n)
* ~100× slower → O(n²)
* barely changes → O(log n)
* explodes → exponential 

