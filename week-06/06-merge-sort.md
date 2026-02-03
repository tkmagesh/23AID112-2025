
## 3. Merge Sort

![image](./images/merge-sort.png)

### Idea

Merge Sort also uses **divide and conquer**, but guarantees good performance.

* Divide the array into halves
* Sort each half
* Merge sorted halves

### How it works

1. Split array into two halves
2. Recursively sort each half
3. Merge the two sorted halves

### Python Implementation

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Example

```python
arr = [38, 27, 43, 3, 9]
print(merge_sort(arr))
# Output: [3, 9, 27, 38, 43]
```

### Time & Space Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n log n) |
| Space   | O(n)       |
| Stable  |  Yes      |
