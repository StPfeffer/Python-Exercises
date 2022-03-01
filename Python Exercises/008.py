word = input("Enter some words in a comma-separated sequence: ")
words = [x for x in word.split(",")]
print(", ".join(sorted(words)))


items = [x for x in input("Enter some words in a comma-separated sequence: ").split(",")]
items.sort()
print(", ".join(items))