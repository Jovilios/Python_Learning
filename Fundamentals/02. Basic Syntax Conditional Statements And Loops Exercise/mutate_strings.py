first_word = input()
second_word = input()

mixed_word = first_word
for idx in range(len(first_word)):
    if first_word[idx] == second_word[idx]:
        continue
    mixed_word = second_word[:idx + 1] + first_word[idx + 1:]
    print(mixed_word)
