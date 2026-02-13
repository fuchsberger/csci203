# What Is an Accumulator?

An accumulator is a variable that:
- Starts with an initial value
- Changes repeatedly inside a loop
- “Accumulates” (builds up) a result over time

Think of it like a running total.

```python
total = 0

for number in range(1, 6):
    total = total + number

print(total)

# What happens?
# we add 1 + 2 + 3 + 4 + 5 for a total of 15
```
Potential Exam question: Create a tracetable for the algorithm above.

# Why are accumulators important?
Accumulators allow us to simulate:

- Game scoring
- Utility cost prediciton
- Tax/Interest/Revenue accumulation
- Points in competitions
- Population growth (we won’t use this today 😉)
- Distance traveled
- Resource collection
- Spread of ideas
- future state of variables via predictive simulations

**They let us model change over time.**

Lets solve a real problem for [Skyrim Players](https://en.uesp.net/wiki/Skyrim:Trainers#Notes). The wiki states:

- For advancement of skills less than or equal to `50`:

  `n(10b + 5n + 45)`

- For advancement of skills greater than `5`0`:

  `n(30b + 15n + 35)`

- For advancement of skills greater than `75`:

  `n(50b + 25n + 25)`

Where `n` is the number of times you wish to train and `b` is the current level of the skill.

E.g.: If you wish to train a particular skill from level `20` to `50` (`b = 20` and `n = 50-20 = 30`) the combined cost (`250+260+270+...+540`) would be `30(10*20 + 5*30 + 45) = 11850`.

Lets design the following function and test it:
```python
def training_cost(start_level, end_level):
  """Returns the total gold cost to train a skill from start_level` to `end_level`.

  Parameters:
    - `start_level` integer >= 1
    - `end_level` integer >= `start_level`

  Return value:
    - integer >= 0 representing the gold cost
  """
```
