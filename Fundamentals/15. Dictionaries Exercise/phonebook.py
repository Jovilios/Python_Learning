people = input().split("-")

phonebook = {}

while len(people) > 1:
    contact_name = people[0]
    phone_number = people[1]
    phonebook[contact_name] = phone_number
    people = input().split("-")

for i in range(int(people[0])):
    searched = input()
    if searched in phonebook:
        print(f"{searched} -> {phonebook[searched]}")
    else:
        print(f"Contact {searched} does not exist.")
