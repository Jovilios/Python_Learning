line = input()

exam = {}
exam_counter = {}

while True:
    if line == "exam finished":
        break
    elif "banned" in line:
        name, ban = line.split("-")
        for key, value in exam.items():
            if name in value:
                value.pop(name)
    else:
        name, lang, points = line.split("-")
        points = int(points)
        if lang not in exam:
            exam[lang] = {}
            exam_counter[lang] = 0
        exam_counter[lang] += 1
        if name in exam[lang] and points <= exam[lang][name]:
            line = input()
            continue

        exam[lang][name] = points

    line = input()


print("Results: ")
for key, value in exam.items():
    for k, v in value.items():
        print(f"{k} | {v}")

print("Submissions: ")
for key, value in exam_counter.items():
    if key in exam:
        print(f"{key} - {value}")
