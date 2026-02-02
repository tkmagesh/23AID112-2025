

# Bubble Sort

* Repeatedly compares **adjacent elements**
* Swaps them if they’re in the wrong order
* Larger elements “bubble up” to the end

---

### Basic bubble sort

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
```

### Example usage

```python
nums = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(nums))
```

**Output**

```
[11, 12, 22, 25, 34, 64, 90]
```

---

### Optimized bubble sort (early exit 🚀)

Stops early if the list is already sorted.

```python
def bubble_sort_optimized(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr
```

---

### Key characteristics

* **Time complexity**

  * Best: `O(n)` (optimized version, already sorted)
  * Average / Worst: `O(n²)`
* **Space complexity:** `O(1)`
* **Stable?**  Yes
* **Good for:** learning, tiny datasets
* **Bad for:** performance on large lists 

