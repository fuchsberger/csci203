# Final Project

[Final Project Instructions & Grading rubric](https://docs.google.com/spreadsheets/d/1e6pTpGP58kv9knUV6GHU1ibA9mT7kVpu-F3mV9KHpco/edit?gid=1973983522#gid=1973983522)

## Steps for creating a markdown file

1.  Open Notepad / Textedit
2.  Save empty file as `README.md` in your project folder
3.  Make changes and open it with Notepad/TextEdit in the future

## Sample structure of the proposal

- Must contain a summary of your intended project.
- Must contain some example descriptions of anticipated helper functions.
- Must contain a bullet point list with all planned core features (main menu entries).
- If Innovative Components by Student (see below) are used, they need to be clarified for instructor approval here.

```markdown
# CSCI 203 Proposal

Short Description that (optionally) contains [source links](https://google.com) and/or images.

## Core Features

- Feature 1
- Feature 2
- Feature 3

## Innovative Component Clarification

(optional section) If Innovative Components by Student (see below) are used, clarify here how it will satisfy the conditions layed out in the rubric.

## Sample helper functions
```

## Find Word Indexes

The idea is to write a function that returns the indexs of all occurences of `word` in text.

We can start this in [test-driven development style](https://en.wikipedia.org/wiki/Test-driven_development):

> Test-driven development (TDD) is a way of writing code that involves writing an automated unit-level test case that fails, then writing just enough code to make the test pass, then refactoring both the test code and the production code, then repeating with another new test case.



```python
def find_word_indexes(text, word):
    # TODO
    pass


def test_find_word_indexes():
    text = "ABAABCDEAEDA"
    assert find_word_indexes(text, "A") == [0, 2, 3, 8, 11]
    assert find_word_indexes(text, "B") == [1, 4]

if __name__ == "__main__":
    test_find_word_indexes()

```

In our first iteration we keep it simple and only account for single letters as words. The solution we arrived in class was this:
```python
def find_word_indexes(text, word):
    indexes = []

    for idx in range(len(text)):
        if text[idx] == word:
            indexes.append(idx)

    return indexes
```

Now we revise the test function to account for all words:
```python
def test_find_word_indexes():
    text = "ABAABCDEAEDA"
    assert find_word_indexes(text, "AB") == [0, 3]
    assert find_word_indexes(text, "B") == [1, 4]
```

And finally we revise the function:
```python
def find_word_indexes(text, word):
    indexes = []

    for i in range(0, len(text) - len(word) + 1):
        # if word[0] == text[idx] and word[1] == text[idx+1]:
        if word == text[i:i + len(word)]:
            indexes.append(i)

    return indexes
```

### Conclusion
- used `indexing` and `slicing`
- reduced the range by the word length to avoid index out of bounds errors.
- caveat: if the word is longer than the text we still get an index out of bound error.

**Fix:** add this before your for loop:
```python
if len(word) > len(text):
    return indexes
```
