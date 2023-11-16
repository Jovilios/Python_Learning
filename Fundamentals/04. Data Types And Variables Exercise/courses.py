line = input()

courses = {}

while True:
    if line == "end":
        break
    course_name, student_name = line.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    line = input()

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for i in value:
        print(f"-- {i}")


