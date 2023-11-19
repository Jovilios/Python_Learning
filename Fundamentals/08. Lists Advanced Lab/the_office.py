def happy_employees(employee_happiness, factor):
    happiness_list = [int(x) * factor for x in employee_happiness.split()]
    total_count = len(happiness_list)
    average = sum(happiness_list) / total_count
    happy_count = len([x for x in happiness_list if x >= average])
    if happy_count >= total_count / 2:
        return f"Score: {happy_count}/{total_count}. Employees are happy!"
    else:
        return f"Score: {happy_count}/{total_count}. Employees are not happy!"


employee_happiness = input()
factor = int(input())

print(happy_employees(employee_happiness, factor))
