def hanoi(n, left, middle, right):
    if n > 0:
        hanoi(n - 1, left, right, middle)
        print(left, right)
        hanoi(n - 1, middle, right, left)
        

hanoi(4, "A", "B", "C")
# AB
# AC
# BC
# AB
# CA
# ...
