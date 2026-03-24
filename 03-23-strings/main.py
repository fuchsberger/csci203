def encrypt(text):
    encrypted = ""

    for c in text:
        encrypted += chr(ord(c) + 1)

    return encrypted

def decrypt(encrypted_text):
    text = ""

    for c in encrypted_text:
        text += chr(ord(c) - 1)

    return text
    

def test_ceasar():

    assert "BCD" == encrypt("ABC")
    assert "ABC" == decrypt("BCD")

if __name__ == "__main__":
  test_ceasar()


print("Hello World"[:4])
