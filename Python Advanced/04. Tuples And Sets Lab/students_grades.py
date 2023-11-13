
students = {}

for _ in range(int(input())):
    name, grade = tuple(input().split())
    grade = float(grade)

    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{name} -> {' '.join(str(f'{x:.2f}') for x in grades)} (avg: {avg:.2f})")