message = input(">")
words = message.split(" ")

emojis = {
    ":)": "😊",
    ":D": "😀",
    ";)": "😉",
    "-_-": "😑",
    "XD": "😆",
    ":*": "😗",
    "<3": "❤",
    "8)": "😎",
    ":(": "☹",
    ":'(": "😥",
    "O:)": "👼",
    ":O": "😲",
    ">:(": "😡",
    ":/": "😕",
    ">:)": "😈",
    "o.O": "🤨"
}

output = ""
for word in words:
    emojis.get(word, word)
    output += emojis.get(word, word) + " "
print(output)
