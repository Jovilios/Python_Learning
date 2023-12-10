def calculator(a,b,operation_name):
    if operation_name == "multiply":
        return a * b
    elif operation_name == "divide":
        return a // b
    elif operation_name == "add":
        return a + b
    elif operation_name == "subtract":
        return a - b


mat_operator = input()
first_num = int(input())
second_num = int(input())

print(calculator(first_num, second_num, mat_operator))
