# Random

## Creating a game - Black Jack

- using an infinite while loop (game loop) with an input is a simple mechanism to maintain a game and only exit on specific conditions (e.g. win or loose).
- A list may have different data types
-

```python
# 1 choose whether to pick a new card

# if so, add score to current score

# we win if final score is between 18-21
# we get our money back if score is 16 or 17
# we loose otherwise

import random

CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

def main():

    score = 0

    while True:

        choice = input("New card? (y, n): ")

        if choice == "y":
            card = random.choice(CARDS)
            print("Next card:", card)

            if type(card) == int:
                score += card
            elif card == "A" and score <= 10:
                score += 11
            elif card == "A" and score > 10:
                score += 1
            elif type(card) == str:
                score += 10

            if score > 21:
                print("You lost. Score: ", score)
                return


            elif score >= 18:
                print("You win. Score: ", score)
                return


            print("Current Score:", score)

        elif choice == "n":
            print("no more cards")
            return
        else:
            print("invalid choice. try again.")

main()
```

### Monte Carlo

Determine probabily by repeating an experiment many times.
Probability = number of times it pans out / number of total attemps.

For example: What is the probability for drawing an ace:

```python
import random

CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


# probability of drawing an ace:
count = 0

for i in range(1000000):
    if random.choice(CARDS) == "A":
        count += 1

print("Probability: ", count/1000000)
print(1/13)

```

### Exercise

Use a Monte Carlo simulation to determine the probability of drawing the same face card twice in a row.
