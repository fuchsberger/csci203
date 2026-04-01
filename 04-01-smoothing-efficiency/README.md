# Smoothing

Continuing the example from last lecture lets have a look of how we could smooth the volatile graph we aquired previously:

![Graph](./graph.png)

Lets discuss the smooth function given in the book:

```python
def smooth(data: list[float], width: int) -> list[float]:
    """Return a new list of data, smoothed over windows of the given width.
    Parameters:
    data: a list of numbers
    width: the width of each window
    Return value: a list of smoothed data values
    """
    total = 0                              # get sum for the first window

    for index in range(width):
        total = total + data[index]

    smoothed_data = [total / width]

    for index in range(1, len(data)):               # start at index 1
        total = total - data[index - 1]             # subtract left value

        if index + width - 1 < len(data):           # and, if possible,
            total = total + data[index + width - 1] # add right value
        width = min(width, len(data) - index)       # adjust width at end
        smoothed_data.append(total / width)         # append the mean

    return smoothed_data
```

We can now use it in our existing program from last lecture:

```python
def main()
    # ...

    senLen = []
    for s in sentenceList:
        wordList = s.split()
        senLen.append(len(wordList))

    # Insert the following:

    smoothed3 = smooth(senLen, 3)
    smoothed5 = smooth(senLen, 5)

    # Comment out the plots that you don't need
    pyplot.plot(range(1, len(senLen) + 1), senLen, label="Original")
    pyplot.plot(range(1, len(senLen) + 1), smoothed3, label="Smoothed 3")
    pyplot.plot(range(1, len(senLen) + 1), smoothed5, label="Smoothed 5")

    # ...
```

And we can see the following smoothed graphs:

![Graph](./graph-smoothed.png)
