def numbers(args):

    neg_sum = 0
    pos_sum = 0

    for el in args:
        if el < 0:
            neg_sum += el
        else:
            pos_sum += el

    print(neg_sum)
    print(pos_sum)
    if abs(neg_sum) > pos_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


line = [int(x) for x in input().split()]

numbers(line)

