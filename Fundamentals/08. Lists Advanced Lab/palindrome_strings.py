words = input().split()
searched_palindrome = input()

palindrome = []
counter = 0

for word in words:
    if word == word[::-1]:
        palindrome.append(word)
    if word == searched_palindrome:
        counter += 1

print(palindrome)
print(f"Found palindrome {palindrome.count(searched_palindrome)} times")
