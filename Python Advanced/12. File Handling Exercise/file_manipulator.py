import os

while True:
    commands = input().split("-")

    if commands[0] == "Create":
        with open(f"temp/{commands[1]}", "w"):
            pass

    elif commands[0] == "Add":
        with open(f"temp/{commands[1]}", "a") as file:
            file.write(f"{commands[2]}\n")

    elif commands[0] == "Replace":
        try:
            with open(f"temp/{commands[1]}", "r+") as file:
                text = file.read()
                text = text.replace(commands[2], commands[3])
                file.seek(0)
                file.write(text)

        except FileNotFoundError:
            print(f"An error occurred")

    elif commands[0] == "Delete":
        try:
            os.remove(f"temp/{commands[1]}")

        except FileNotFoundError:
            print(f"An error occurred")

    elif commands[0] == "End":
        break
