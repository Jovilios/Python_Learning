budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) * 0.25
loaves_price = flour_price + eggs_price + milk_price

loaves_counter = 0
eggs_counter = 0

while budget >= loaves_price:
    budget -= loaves_price
    loaves_counter += 1
    eggs_counter += 3
    if loaves_counter % 3 == 0:
        eggs_counter -= loaves_counter - 2
print(f"You made {loaves_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")
