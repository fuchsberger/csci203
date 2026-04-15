"""
Text Helper Functions
"""

def slug(text):
  """
  slug("Hello World!")
  "hello_world"
  """

  text = text.lower()

  text = text.replace("!", "")

  # replace special characters and space
  new_text = ""
  for c in text:
    if c == " ":
      new_text += "_"
    elif c in "!.?;<>,":
      pass
    else:
      new_text += c

  
  return new_text


def test_slug():
  assert slug("Hello World!") == "hello_world"
  print("All tests are good.")

if __name__ == "__main__":
  test_slug()

