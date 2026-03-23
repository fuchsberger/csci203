## Final Project Rubric & Info

[Final Project Rubric and Information](https://docs.google.com/spreadsheets/d/1e6pTpGP58kv9knUV6GHU1ibA9mT7kVpu-F3mV9KHpco/edit?gid=1973983522#gid=1973983522)

Submission via PrarieLearn

## Files

- You must open a file before you can read from or write to it.
- By default looks for files in the same folder
- By default opens a file in read mode (can't accidentaly write to it)

### Reading

```python
f = open("filename")

# read all content at once
text = f.read()

# read file line by line
line = f.readline()
while line:
    #  do stuff with line
    line = f.readline()
```

### Writing

Opening a file in `w` write mode will **replace** all content when `f.write()` is called:

```python
f = open("filename", "w")
text = f.write("new content\nline 2")

# new content
# line 2
```

Opening a file in `a` append mode will **add** content to the bottom of the file when `f.write()` is called:

```python
f = open("filename", "a")
text = f.write("new content\n")
text = f.write("line 2")

# new content
# line 2
```

### Writing

After you are done processing a file you should close it properly to free memory resources:

```python
def get_content(file):
    f = open("filename", "r")
    text = f.read()
    f.close()
    return text
```

### Main Menu FInal Project Wrapper Template

This is a suggested approach to organize your program into a format that supports multiple user-selected main features.

General Advise:

- Create lots of tiny functions instead of few big ones
- Move helper functions into their own module(s)
- Use docstrings for all functions instead of comments
- Use comments only if the meaning of a subsequent code block cann't easily be determined by looking at the code.
- create test functions immeadiatly as you complete helper functions instead of waiting till after you are done coding it
- wrap your test function in a `__name__ == "__main__"` conditional to only test if running the file directly (see below).

`main.y`

```python
from helpers import main

def main():

    while(True):
        menu()
        choice = input("Press a key: ")

        if choice == "1":
            handle_add()

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            print("Goodbye.")
            return

        else:
            print("Invalid Option. Try again.")

if __name__ == "__main__":
    main()
```

`helpers.py`

```python
def menu():
    print("(1) Add Contact")
    print("(2) List Contacts")
    print("(3) Exit")

def handle_add():
    name = input("Name: ")
    number = input("Phone number:")

    f = open("database.csv", "a")

    f.write(f"{name},{number}")
    f.close()

    print(name, " has been added to the contacts.")

def show_contacts():
    f = open("database.csv")
    print(f.read())
    f.close()

def test_helpers():
    test_menu():
        # Add your unit tests here
        # Generally testing print statements is very hard.
        # Testing what a function returns is very easy (do that).
        pass

if __name__ == "__main__":
    test_helpers()
```
