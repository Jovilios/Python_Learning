country = input().split(", ")
capital = input().split(", ")

dictionary = {country[idx]: capital[idx] for idx in range(len(country))}
# dic1 = dict(zip(country, capital))


for key, value in dictionary.items():
    print(f"{key} -> {dictionary[key]}")

