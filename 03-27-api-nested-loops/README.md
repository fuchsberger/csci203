## Nested For Loops

![Tic Tac Toe](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJd6tIrqyz0C3Quc9ohvlqK6DhvTXO2gJKQA&s)

Lets start by representing a game state of Tic Tac Toe in a format that the computer can read more easily. Since we always have `3` rows and `3` columns we can use a string or list, where

- `0` indicates an empty slot
- `1` indicates slot occupied by player 1 (x)
- `2` indicates slot occupied by player 2 (o)

```python
"010221100"
[0, 1, 0, 2, 2, 1, 1, 0, 0]
```

Because this game always has `3` rows and `3` columns the `index` in that list/string identifies the actual game field precicely. For example index `2` always refers to the top-right corner field.

While a string is fine we could also choose a nested list for storage:

```python
[
  [0, 1, 0],
  [2, 2, 1],
  [1, 0, 0]
]
```

A nested list is a list that contains other lists.
This is more human readable and comes with advantages and disadvantages.

We are going to write two functions now

- to convert a list in the format above into a nested list
- convert a nested list back into a singular list

## Nested List indexing and looping

`TODO`

## API data

In order to make the starting code work on your computer we will need to install a python module that doesn't come preinstalled:

**Windows:** Search for `cmd` or `PowerShell`. Open the program and type:

```bash
py -3.14 -m pip install requests
```

**Mac OS:** Search for `Terminal`. Open the program and type:

```bash
python3.14 -m pip install requests
```

This should install a module that allows us to send API requests to other servers!

You can then run `starting_code.py` in IDLE. You should see an output like this:

```
[38.8316650390625, -122.817169189453, 0.77]
[57.379, -156.282, 2.2]
[51.853, -172.407, 3.4]
```

_This is a very long list containing all the earthquakes measured since yesterday including their magnitude on the richter scale!_

## Scatter Plot

Lets see if we can plot them in a scatter plot:

```python
import matplotlib.pyplot as pyplot

def plot(quakes: list) -> None:
    """Display a scatterplot of earthquakes.
    Parameters:
        quakes - a list of lists: [latitude, longitude, magnitude]

    Return value: None
    """
    x = []
    y = []
    for index in range(len(quakes)):
        # TODO
        pass
    pyplot.scatter(x, y) # scatter plot
    pyplot.xlabel("Latitude")
    pyplot.ylabel("Longitude")
    pyplot.show()
```
