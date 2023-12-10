command = input().split(":")

students = {}

while len(command) > 1:
    name, student_id, course = command[0], command[1], command[2]
    if course not in students.keys():
        students[course] = []
    students[course].append(f"{name} - {student_id}")
    command = input().split(":")

searched_course = command[0].replace("_", " ")

for student in students[searched_course]:
    print(student)

