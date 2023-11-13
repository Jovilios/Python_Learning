def forecast(*args):
    result = {}

    for i in args:
        if i[0] not in result:
            result[i[0]] = i[1]

    sorted_result = {k: v for k,v in sorted(result.items(), key=lambda x: (x[1], x[0]))}

    sunny = ''
    cloudy = ''
    rainy = ''

    for key, value in sorted_result.items():
        if value == 'Sunny':
            sunny += f'{key} - {value}\n'
        elif value == 'Cloudy':
            cloudy += f'{key} - {value}\n'
        elif value == 'Rainy':
            rainy += f'{key} - {value}\n'

    return sunny + cloudy + rainy





print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

