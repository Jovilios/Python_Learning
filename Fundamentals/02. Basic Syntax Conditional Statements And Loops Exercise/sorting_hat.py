name_length = 0
while True:
    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if name == "Voldemort":
        print("You must not speak of that name!")
        quit()
    for ch in range(1, len(name) + 1):
        name_length = ch
    if name_length < 5:
        print(f"{name} goes to Gryffindor.")
    if name_length == 5:
        print(f"{name} goes to Slytherin.")
    if name_length == 6:
        print(f"{name} goes to Ravenclaw.")
    if name_length > 6:
        print(f"{name} goes to Hufflepuff.")

