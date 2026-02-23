words = ["apple", "bat", "banana", "cat"]

sorted_words = sorted(words, key=lambda x: (len(x), x))

print(sorted_words)
