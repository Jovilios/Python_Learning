budget = int(input())

current_sum = input()
while current_sum != "End":
    product = int(current_sum)
    budget -= product
    if budget < 0:
        print("You went in overdraft!")
        exit()
    current_sum = input()
print("You bought everything needed.")