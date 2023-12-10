def repeat(input_word, multiply):
    return input_word * multiply


word = input()
counter = int(input())

print(repeat(word, counter))


# repeat = lambda input_word, multiply: input_word * multiply
# result = repeat((word, counter))

print(repeat(word, counter))
