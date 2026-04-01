# Text Analysis

Lecture taught by visiting Candidate **Dr. Buffum**.

We covered an example analyzing average sentence length in presidential speeches using the request library (to pull data from a web source).

Final program:

```python
import requests

import matplotlib.pyplot as pyplot


def main():
    lincoln = "https://gutenberg.org/cache/epub/9/pg9.txt"
    response = requests.get(lincoln)

    txt = response.text

    indexStart = txt.index("Fellow")
    indexEnd = txt.index("*** END")

    speech = txt[indexStart:indexEnd]

    sentenceList = speech.split(".")


    avg_words_per_sentence = mean(sentenceList)
    print(avg_words_per_sentence)

    senLen = []
    for s in sentenceList:
        wordList = s.split()
        senLen.append(len(wordList))

    print(senLen)

    pyplot.plot(range(1, len(senLen) + 1), senLen, label="Original")
    pyplot.legend()
    pyplot.xlabel("Sentence Number")
    pyplot.ylabel("Word Count")
    pyplot.show()

def mean(data: list[str]) -> float:
    if len(data) == 0:
        raise ValueError("Empty List")

    total = 0
    for item in data:
        wordList = item.split()
        total += len(wordList)

    return total / len(data)

main()
```
