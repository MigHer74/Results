# This function converts a string into a list
def convertion(values):
    l1 = []

    values = values.split(",")

    for i in values:
        l1.append(int(i))

    return l1