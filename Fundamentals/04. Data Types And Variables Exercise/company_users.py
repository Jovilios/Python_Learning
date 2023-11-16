line = input()

company = {}


while True:
    if line == "End":
        break

    company_name, employee = line.split(" -> ")
    if company_name not in company:
        company[company_name] = []
    if employee in company[company_name]:
        line = input()
        continue
    company[company_name].append(employee)

    line = input()

for key, value in company.items():
    print(f"{key}")
    for i in value:
        print(f"-- {i}")
