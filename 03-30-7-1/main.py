import requests

lincoln = "https://gutenberg.org/cache/epub/9/pg9.txt"
response = requests.get(lincoln)

txt = response.text

indexStart = txt.index("Fellow")
indexEnd = txt.index("*** END")

speech = txt[indexStart:indexEnd]

print(speech)
