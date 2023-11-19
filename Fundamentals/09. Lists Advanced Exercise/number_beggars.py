coins = input().split(", ")
coins_as_int = []

for coin in coins:
    coins_as_int.append(int(coin))

number_of_beggars = int(input())

final_sum = []

starting_index = 0

while starting_index < number_of_beggars:
    sum_for_beggar = 0
    for current_index in range(starting_index, len(coins_as_int), number_of_beggars):
        sum_for_beggar += coins_as_int[current_index]

    final_sum.append(sum_for_beggar)
    starting_index += 1

print(final_sum)
