message = input(">")
words = message.split(" ")

emojis = {
    ":)": "๐",
    ":D": "๐",
    ";)": "๐",
    "-_-": "๐",
    "XD": "๐",
    ":*": "๐",
    "<3": "โค",
    "8)": "๐",
    ":(": "โน",
    ":'(": "๐ฅ",
    "O:)": "๐ผ",
    ":O": "๐ฒ",
    ">:(": "๐ก",
    ":/": "๐",
    ">:)": "๐",
    "o.O": "๐คจ"
}

output = ""
for word in words:
    emojis.get(word, word)
    output += emojis.get(word, word) + " "
print(output)
