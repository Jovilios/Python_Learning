list_of_chars = input().split(", ")

characters = {key: ord(key) for key in list_of_chars}

print(characters)