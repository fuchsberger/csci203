# O(n)
def doThis1(n):
    for i in range(n):
        print(i)

# O(n^2)
def doThis2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


# T(10) => 1 + 10 + 10 * 10
# O(n^2)
def doThis3(n):
    x = 0

    for i in range(n):
        print(i)

    for i in range(n):
        for j in range(n):
            print(i, j)

# O(n*m)
def doThis4(n, m):
    for i in n:
        for j in m:
            print(i, j)

# T(10) -> 10 * 10
# O(n)
def doThis5(n):
    for i in n:
        for j in range(10):
            print(i, j)



# O(1)
def doThis6(n):
    print(n)
