

data = [[1, 2, 3], [{1: "A"}, 3, 4]]

##data[1]         # [2, 3, 4]
##data[1][2]      # 4

import json

def save(filename):
    f = open(filename, "w")
    f.write(json.dumps(data))

## save("data.json")

def load(filename):
    f = open(filename)
    data = json.loads(f.read())
    #print(data)
    #print(data[1][0])

    return data

load("data.json")

# project

# 1. when starting app --> load
# 2. in main menu option: save contact

# looping

data = load("data.json")
for item in data:
    for subitem in item:
        print(subitem)
