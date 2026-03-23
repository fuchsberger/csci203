def training_cost(start_level, end_level):
  """Returns the total gold cost to train a skill from start_level` to `end_level`.

  Parameters:
    - `start_level` integer >= 1
    - `end_level` integer >= `start_level`

  Return value:
    - integer >= 0 representing the gold cost
  """
  gold = 0

  for level in range(start_level, end_level):
      if level <= 50:
          gold = gold + 10 * level + 50
      elif level <= 75:
          gold = gold + 30 * level + 50
      else:
          gold += 50 * level + 50

  return gold

print(training_cost(15, 100))
