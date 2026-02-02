

# Selection Sort

* Repeatedly finds the **smallest element** in the unsorted part of the list
* Swaps it with the first unsorted position
* Grows the sorted part one step at a time

---

### Python implementation

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # find the smallest element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap the found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
```

### Example usage

```python
nums = [64, 25, 12, 22, 11]
print(selection_sort(nums))
```

**Output**

```
[11, 12, 22, 25, 64]
```

---

### Key characteristics

* **Time complexity:**

  * Best / Average / Worst → `O(n²)`
* **Space complexity:** `O(1)` (in-place)
* **Stable?**  No
* **Good for:** learning sorting basics, small datasets
* **Bad for:** large datasets (slow)

