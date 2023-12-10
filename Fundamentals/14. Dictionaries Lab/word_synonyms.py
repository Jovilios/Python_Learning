count = int(input())
synonyms = {}


for i in range(count):
    key = input()
    value = input()
    if key not in synonyms:
        synonyms[key] = []
    synonyms[key].append(value)

for key, value in synonyms.items():
    print(f"{key} - {', '.join(synonyms[key])}")