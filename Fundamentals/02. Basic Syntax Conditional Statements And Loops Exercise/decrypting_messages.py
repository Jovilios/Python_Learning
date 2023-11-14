key = int(input())
lines = int(input())

for n in range(1, lines + 1):
    leather = input()
    decrypt = ord(leather) + key
    print(chr(decrypt), end="")
