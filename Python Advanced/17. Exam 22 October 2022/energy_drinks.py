from collections import deque

milligrams_of_coffeine = deque(input().split(", "))
energy_drinks = deque(input().split(", "))

stamat_coffeine = 0
MAX_COFFEINE = 300

while milligrams_of_coffeine and energy_drinks:

    coffeine = milligrams_of_coffeine.pop()
    drink = energy_drinks.popleft()

    current_drink = int(coffeine) * int(drink)

    if current_drink > MAX_COFFEINE - stamat_coffeine:
        if stamat_coffeine <= 30:
            stamat_coffeine = 0
        else:
            stamat_coffeine -= 30
        energy_drinks.append(drink)
    else:
        stamat_coffeine += current_drink


if energy_drinks:
    print(f"Drinks left: {', '.join(energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_coffeine} mg caffeine.")

