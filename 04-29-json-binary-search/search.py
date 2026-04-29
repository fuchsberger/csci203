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
def binary_rec(items, item):
    # TODO
    pass


def test_search():
    numbers = [ 2, 5, 7, 9, 11 ]
    assert binary_search(numbers, 9) == 3
    assert binary_search(numbers, 6) == None

    assert binary_rec(numbers, 9) == 3
    assert binary_rec(numbers, 6) == None

if __name__ == "__main__":
    test_search()
