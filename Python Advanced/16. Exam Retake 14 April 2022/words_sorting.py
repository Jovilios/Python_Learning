def words_sorting(*args):
    words = {}

    for word in args:
        if word not in words:
            words[word] = 0
            for el in word:
                words[word] += ord(el)

    sum_values = sum(words.values())

    if sum_values % 2 == 0:
        sorted_dict = dict(sorted(words.items(), key=lambda x: x[0]))
    else:
        sorted_dict = dict(sorted(words.items(), key=lambda x: x[1], reverse=True))

    result = "\n".join([f"{key} - {value}" for key, value in sorted_dict.items()])

    return result




print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
