def palindrome(word, i):
    if i == len(word) // 2:
        return f"{word} is a palindrome"

    if word[i] != word[-i-1]:
        return f"{word} is not a palindrome"

    return palindrome(word, i + 1)




print(palindrome("peter", 0))

