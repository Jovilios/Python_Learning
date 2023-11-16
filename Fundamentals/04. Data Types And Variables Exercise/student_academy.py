count = int(input())

students_academy = {}

for i in range(count):
    student = input()
    grade = float(input())

    if student not in students_academy:
        students_academy[student] = []
    students_academy[student].append(grade)

for key, value in students_academy.items():
    result = 0
    for i in value:
        result += i
    final_result = result / len(value)
    if final_result < 4.50:
        continue
    print(f"{key} -> {final_result:.2f}")

