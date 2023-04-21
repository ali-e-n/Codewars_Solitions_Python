def open_or_senior(data):
    result = []
    for member in data:
        if member[0] >= 55 and member[1] > 7:
            result.append('Senior')
        else:
            result.append('Open')
    return result     