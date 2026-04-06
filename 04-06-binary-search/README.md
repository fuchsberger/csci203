# Exam 3 Prep List

- linear & binary search (completely understanding it, time complexity)

- time complexity
  - 7 levels of efficiency
  - determining any functions time complexity in Big O notation (information on the time complexity of library functions will be provided, if needed)
  - best/worst/average case time complexity
  - compare two algorithms

- lists and strings
  - indexing
  - slicing
  - in operator, range
  - searching for an item

- aliasing vs referencing
  - mutability / immutability
  - id() function to determine memory address

- smoothing data

- modulo operator (remainder) and integer division

- nested loops
  - continue statement
  - break statement

- files
  - open, close, read, write
  - open mods (r, w, a)

- writing unittests

## Linear Search

```python
def linear_search(items, item):
    for i in range(len(items)):
        if items[i] == item:
            return i

    return -1


def test():
    items = ["A", "B", "C"]

    assert linear_search(items, "A") == 0
    assert linear_search(items, "C") == 2
    assert linear_search(items, "D") == -1

test()
```

### Time Complexity

- Best case: `O(1)` _(first item in list matches)_
- Worst case: `O(n)` _item not in list or last item_

#### What about the average case?

On average we need to go through half the list assuming the item can be found in a random location in the list.
`n/2` is still `O(n)`, because we remove numbers from the `equation`.

## Binary Search

```python
def binary_search(items, item):
    left = 0
    right = len(items)

    while left <= right:
        mid = (right - left) // 2

        if  item < items[mid]:
          right = mid - 1

        elif item > items[mid]:
          left = mid + 1

        else:
          return mid

    return -1


def test():
    items = ["A", "B", "C"]

    assert binary_search(items, "A") == 0
    assert binary_search(items, "C") == 2
    assert binary_search(items, "D") == -1

test()
```

### Time Complexity

- Best case: `O(1)` _first item in list matches_
- Average case: `O(log(n))` _item not in list_
- Worst case: `O(log(n))` _item not in list_
