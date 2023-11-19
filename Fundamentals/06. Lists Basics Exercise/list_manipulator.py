data = [int(i) for i in input().split()]

even_indices = []
odd_indices = []


while True:
    command = input().split()
    if command == "end":
        quit()
# Check for exchange command
    if command[0] == "exchange":
        idx = int(command[1])
        if 0 <= idx < len(data):
            result = (data[idx:] + data[:idx])
            data = result
        else:
            print("Invalid index")
# Check for even/odd min/max index

    # for i in range(len(data)):
    #     if data[i] % 2 == 0:
    #         even_indices.append(i)
    #     elif data[i] % 2 != 0:
    #         odd_indices.append(i)
    #
    # if command[1] == "even" and even_indices:
    #     if command[0] == "min":
    #         result = min(even_indices)
    #     else:
    #         result = max(even_indices)
    # elif command[1] == "odd" and odd_indices:
    #     if command[0] == "min":
    #         result = min(odd_indices)
    #     else:
    #         result = max(odd_indices)
    # else:
    #     odd_indices = []
    #     even_indices = []
    #     result = "No matches"
    # print(result)


# # Get Indices of the Max Value from a List using enumerate()
# a_list = [10, 11, 35, 14, 23, 9, 3, 35, 22]
# indices = [index for index, item in enumerate(a_list) if item == max(a_list)]
#
# print(indices)
# # Returns: [2, 7]