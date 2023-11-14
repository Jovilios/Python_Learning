n = input()


def largest_number(n):
    # Convert the number to a string
    num_str = str(n)
    # Sort the string in descending order
    num_str = ''.join(sorted(num_str, reverse=True))
    # Convert the string back to an int and return it
    return int(num_str)


# Test the function with a sample number
print(largest_number(n))
