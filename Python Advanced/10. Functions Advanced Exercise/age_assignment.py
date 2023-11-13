def age_assignment(*args, **kwargs):
    result = []

    for key, age in kwargs.items():
        for name in args:
            if name.startswith(key):
                result.append(f"{name} is {age} years old.")
                break

    return '\n'.join(sorted(result))




print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))