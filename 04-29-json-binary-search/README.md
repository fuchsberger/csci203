# Binary Search (Iterative)

```python
def binary_search(items, item):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (right - left) // 2

        if  item < items[mid]:
          right = mid - 1

        elif item > items[mid]:
          left = mid + 1

        else:
          return mid

    return None
```

# Binary Search (Recursive)

```python
def binary_rec(items, item):
    left = 0
    right = len(items) - 1
    bin_rec_helper(items, item, left, right)

def bin_rec_helper(items, item, left, right):
    if left > right:
        return None

    mid = (right - left) // 2

    if item < items[mid]:
        bin_rec_helper(items, item, left, mid - 1)
    elif item > items[mid]:
        bin_rec_helper(items, item, mid+1, right)
    else:
        return mid
```

# Efficieny

- both iterative and rec are `O(log n)` time complexity
- iterative has `O(1)` space complexity
- recursive has `O(log n)` space complexity because additional recursive function calls generate more memory footprint.
