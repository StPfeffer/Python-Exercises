words = input("Enter a sequence of whitespace separated words: ")
# set não aceita valores duplicados
words_list = set([x for x in words.split(" ")])

for i in sorted(words_list):
    print(i, end = " ")

print()

s = input("Enter a sequence of whitespace separated words: ")
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
