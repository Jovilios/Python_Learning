num = int(input())

for n in range(1, num + 1):
    n1_first = n % 10
    n1_second = (n // 10) % 10
    numb = n1_first + n1_second
    if numb == 5 or numb == 7:
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")
