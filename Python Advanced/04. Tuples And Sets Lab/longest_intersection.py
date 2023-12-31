longest_intersection = set()

for _ in range(int(input())):
    first_data, second_data = [el.split(",") for el in input().split("-")]

    first = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second = set(range(int(second_data[0]), int(second_data[1]) + 1))

    intersection = first.intersection(second)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(
    f"Longest intersection is "
    f"[{', '.join(str(x) for x in longest_intersection)}] "
    f"with length {len(longest_intersection)}"
)


# Input
#
# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10
#
# Longest intersection is [6, 7, 8, 9, 10] with length 5