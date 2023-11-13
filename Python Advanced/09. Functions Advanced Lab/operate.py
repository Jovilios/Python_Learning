from functools import reduce


def operate(oper, *args):
    # def sum_nums():
    #     return sum(args)
    #
    # def subtract():
    #     res = 0
    #     for num in args:
    #         res -= num
    #     return res
    #
    # def multiply():
    #     res = 1
    #     for num in args:
    #         res *= num
    #     return res
    #
    # def divide():
    #     res = 1
    #     for num in args:
    #         res /= num
    #     return res

    if oper == "+":
        return reduce(lambda a, b: a+b, args)
    elif oper == "-":
        return reduce(lambda a, b: a-b, args)
    elif oper == "*":
        return reduce(lambda a, b: a*b, args)
    elif oper == "/":
        return reduce(lambda a, b: a/b, args)



print(operate("+", 1, 2, 3))
