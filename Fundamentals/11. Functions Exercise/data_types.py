def data_type(command, data):
    if command == "int":
        num = int(data)
        result = num * 2
        return result
    elif command == "real":
        num = float(data)
        result = num * 1.5
        return f"{result:.2f}"
    elif command == "string":
        return "$" + data + "$"


commands = input()
string = input()

print(data_type(commands, string))