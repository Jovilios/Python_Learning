coffee_count = 0
while True:
    word = input()
    if word == "END":
        break
    if word == "coding" or word == "dog" or word == "cat" or word == "movie":
        coffee_count += 1
    elif word == "CODING" or word == "DOG" or word == "CAT" or word == "MOVIE":
        coffee_count += 2
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
