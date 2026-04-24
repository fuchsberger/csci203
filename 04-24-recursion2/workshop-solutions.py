def count(string, character):
    return countHelper(0, string, character)

def countHelper(count, string, character):
    if string == "":
        return count

    elif string[0] == character:
        return 
    else:
        return countHelper(count, string[1:], character)
        
# tests
assert count("ABBA", "A") == 2
assert count("ABBA", "B") == 2
assert count("ABBA", "C") == 0
