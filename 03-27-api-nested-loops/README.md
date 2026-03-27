## Nested For Loops

```python
# TODO in class
```

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
