to_do_list = [0] * 10

while True:
    notes = input().split("-")
    if notes[0] == "End":
        break
    idx, note = int(notes[0]) -1, notes[1]
    to_do_list.pop(idx)
    to_do_list.insert(idx, note)

result = [x for x in to_do_list if x != 0]

print(result)
