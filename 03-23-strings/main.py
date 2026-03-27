

def find_word_indexes(text, word):
    indexes = []
    word_length = len(word)
    
    for idx in range(0,len(text) - len(word) + 1):
        # if word[0] == text[idx] and word[1] == text[idx+1]:
        if word == text[idx:idx + word_length]:
            indexes.append(idx)

    return indexes
        

def test_find_word_indexes():
    text = "ABAABCDEAEDA"
    assert find_word_indexes(text, "AB") == [0, 3]
    assert find_word_indexes(text, "B") == [1, 4]

if __name__ == "__main__":
    test_find_word_indexes()
