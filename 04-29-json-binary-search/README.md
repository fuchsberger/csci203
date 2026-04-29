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
