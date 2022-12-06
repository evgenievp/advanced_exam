def forecast(*param):
    time = {}
    for location, wheater in param:
        if location not in time:
            time[location] = wheater
    res = sorted(time.items(), key=lambda x: x[0])

    sunny, rainy, cloudy = '', '', ''
    for it in res:
        if it[1] == "Sunny":
            sunny += f"{it[0]} - {it[1]}\n"
        elif it[1] == "Cloudy":
            cloudy += f"{it[0]} - {it[1]}\n"
        elif it[1] == "Rainy":
            rainy += f"{it[0]} - {it[1]}\n"

    output = sunny + cloudy + rainy
    return output