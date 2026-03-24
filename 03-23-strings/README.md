## Checksum

```python
def checksum(text):
    checksum = 0

    for c in text:
        checksum = (checksum + ord(c)) % 256
        #print(c, ord(c))


    return checksum

def test_checksum():
    print(checksum("Hello Class AÄÆ♥"))
    print(checksum("Hellp Class AÄÆ♥"))

test_checksum()
```

## Activity: Ceasar's Cipher

- Create your own encryption algorithm (encrypt)
- Create your own decryption algorithm (decrypt)

Example:

```python
encrypt("Hello") # "aeUUs"
decrypt("aeUUs") # "Hello"
```

You will want to use `ord(c)` and `chr(o)` to convert a character into an ordial value and back:

```python
ord(c) --> ord
chr(ord) --> c
```

Starting code:
```python
def encrypt(text):
    pass

def decrypt(text):
    pass

def test_ceasar():
    pass

if __name__ == "__main__":
  test_ceasar()
```


# string/list slicing
"Hello World"
