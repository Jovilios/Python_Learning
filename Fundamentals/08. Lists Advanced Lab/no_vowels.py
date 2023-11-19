words = input()

vowels = ['a', 'o', 'u', 'e', 'i']
result = [x for x in words if x.lower() not in vowels]
print("".join(result))
