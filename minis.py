# This function converts a string into a list
def convertion(tolist):
    ls = []

    for i1 in range(len(tolist)):
        values = tolist[i1]
        values = values.split(",")
        
        for i2 in values:
            ls.append(int(i2))

    return ls