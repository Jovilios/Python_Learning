num = int(input())
magic_word = input()

words = []
magic_list = []

for _ in range(num):
    word = input()
    words.append(word)
    if magic_word in word:
        magic_list.append(word)

print(words)
print(magic_list)
