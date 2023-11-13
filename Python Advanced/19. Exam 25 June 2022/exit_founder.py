names = [{"name": x, "rest": False} for x in input().split(", ")]

SIZE = 6

matrix = [[x for x in input().split()] for _ in range(SIZE)]


while True:
    player = names.pop(0)
    coordinates = input()
    row, col = int(coordinates[1]), int(coordinates[-2])

    if player["rest"]:
        player["rest"] = False
        names.append(player)
        continue

    if matrix[row][col] == "E":
        print(f"{player['name']} found the Exit and wins the game!")
        break

    elif matrix[row][col] == "T":
        print(f"{player['name']} is out of the game! The winner is {names[0]['name']}.")
        break

    elif matrix[row][col] == "W":
        player['rest'] = True
        print(f"{player['name']} hits a wall and needs to rest.")

    names.append(player)
