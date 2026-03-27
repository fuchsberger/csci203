#  [0, 1, 0, 2, 2, 1, 1, 0, 0]

#  [
#    [0, 1, 0],
#    [2, 2, 1],
#    [1, 0, 0]
#  ]

def index_to_coordinates(index:int):
    x = index % 3
    y = index // 3

    return (x, y)

def coordinates_to_index(coords:tuple):
    x, y = coords
    # x = 2, y = 0 --> 2 (top right)
    # x = 0, y = 2 --> 6 (bottom left)
    return x + 3 * y


def tests():

    assert index_to_coordinates(2) == (2, 0)
    assert coordinates_to_index((2, 0)) == 2

if __name__ == "__main__":
    tests()
