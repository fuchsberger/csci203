# Dictionaries

# Lists vs Dictionaries

**Lists**
  - optimized for traversal (do something with each item)
  - ordered
  - implemented as an array of references (thus `O(1)` for indexing)
  - suitable for storing collections of items
  - (usually) not suitable for storing attributes of an item


```python
# Not a good use case for a list
person_list = ["Sam", "Adams", 34]

# good use case
people = ["Sam", "Amelia", "George"]
```

**Dictionaries**
  - key/value storage
  - optimized for lookup (find the value given the key)
  - order not guaranteed
  - implemented as a hash map (thus `O(1)` for indexing)
  - suitable for storing attributes of an item
  - (usually) not suitable for storing multipe items


```python
# good use case
person_dict = {
  "first_name": "Sam",
  "last_name": "Adams",
  "age": 34
}

# Bad use case
people = {
  "person1": "Sam",
  "person2": "Amelia",
  "person3": "George"
}
```

### Indexing Lists / Dictionaries
Indexing in dictionaries works exactly like in lists except in
  - lists one finds value by numeric (ordered) index
  - dictionaries one finds value by key index, which should be a string`*`

```python
last_name = person_list[1] # Adams
last_name = person_dict["last_name"] # Adams
```

`*` You are technically allowed to use any primary datatypes as keys but anything other than a string is usually a bad idea because the dictionary can no longer be converted into JSON and back. This becomes important in your final projects if you plan to use JSON storage/API stuff.

### Add/Modify entry in dictionary

Simply assign a new value to the dictionary for both adding/modifying:

```python
person_dict["age"] = 33
person_dict["height"] = "5'4"
```
In comparison you use `append()` to add to a list and the same reassignment pattern as in dictionaries for lists:
```python
person_list[2] = 33
person_list.append("5'4")
```

*Attention:* `append()` wont work on dictonaries. This method is exclusively for lists.

### Removing items from lists and dictionaries

Let's remove `age` from `dict_list`. There are 2 variants:
```python
# no return (not a function)
del person_list[2]

# returns removed item value (33)
new_lists = person_list.pop(2)
```

In both cases person_list is now `["Sam", "Adams", "5'4"]`.

Lets remove age from dictionary:
```python
del  person_list["age"]
```

### Looping through dictionaries
Remember, order of key/value pairs is not guaranteed.

**Correction:** As of Python 3.7 Python dictionaries now maintained the order of insertion of key-value pairs.

```python
# loop through keys (variant 1)
for something in person2:
    print(something)

# loop through keys (variant 2)
for key in person2.keys():
    print(key)

# loop through values
for value in person2.values():
    print(value)

# loop through both
for key, value in person2.items():
    print(key, value)
```
