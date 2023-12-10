def check_positive(a, b, c):
    result = a * b * c
    if result == 0:
        return "zero"
    elif result < 0:
        return "negative"
    elif result > 0:
        return "positive"


first = int(input())
second = int(input())
third = int(input())

print(check_positive(first, second, third))
