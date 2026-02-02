
## Bubble Sort vs Selection Sort (Python)

###  Bubble Sort

* Compares **adjacent elements**
* Swaps them if they are in the wrong order
* Larger elements move (“bubble”) to the end

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

**Pros**

* Very easy to understand
* Can stop early if optimized

**Cons**

* Inefficient for large datasets

---

###  Selection Sort

* Finds the **minimum element**
* Places it at the correct position

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```

**Pros**

* Fewer swaps than bubble sort
* Simple, predictable behavior

**Cons**

* Always runs in `O(n²)`
* Not stable

---

## Quick comparison table

| Algorithm      | Best Case | Average | Worst | Stable | In-Place |
| -------------- | --------- | ------- | ----- | ------ | -------- |
| Bubble Sort    | O(n)      | O(n²)   | O(n²) | ✅ Yes  | ✅ Yes    |
| Selection Sort | O(n²)     | O(n²)   | O(n²) | ❌ No   | ✅ Yes    |

---

### Bottom line

* **Bubble Sort:** best for understanding basic swapping logic
* **Selection Sort:** useful when swap operations are expensive
* **Real-world use:** prefer Python’s built-in `sorted()`

