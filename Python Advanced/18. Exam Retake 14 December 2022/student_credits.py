def students_credits(*args):
    courses = {}
    all_credits = 0

    for course in args:
        course_arg = course.split("-")
        credits = int(course_arg[1])
        max_points = int(course_arg[2])
        dido_points = int(course_arg[3])
        all_credits += dido_points * (credits / max_points)
        courses[course_arg[0]] = dido_points * (credits / max_points)

    result = ""

    if all_credits >= 240:
        result += f"Diyan gets a diploma with {all_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - all_credits:.1f} credits more for a diploma.\n"

    for key, value in sorted(courses.items(), key=lambda x: -x[1]):
        result += f"{key} - {value:.1f}\n"

    return result


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)




