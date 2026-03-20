# Agenda

- try/except
- Learn about organizing project in multiple files
- Create a helper module
- Use unit testing framework (required for final project)
- Do some text analysis

# Try Except
```python
x = 1
y = "sdfsd"
z = None

try:
    z = x / y
except ZeroDivisionError:
    print("y cannot be 0")

except:
    print("A Problem occured")

print("Result", z)
```


