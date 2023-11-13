from string import punctuation

with open("temp/text.txt", "r") as f:
    text = f.readlines()

output = open("temp/output.txt", "w")

for idx in range(len(text)):
    letters_counter = 0
    punctuation_counter = 0

    for symbol in text[idx]:
        if symbol.isalpha():
            letters_counter += 1
        elif symbol in punctuation:
            punctuation_counter += 1

    output.write(f"Line {idx+1}: {''.join(text[idx][:-1])} ({letters_counter})({punctuation_counter})\n")

output.close()