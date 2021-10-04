# This function selects the type of group of numbers according to the type of game
def enter_data(sel):
    if sel == 1:
        label = "FIRST"
    elif sel == 2:
        label = "SECOND"
    else:
        label = "THIRD"
    
    print("Enter the", label, "group of numbers.\n")

    n1 = input("Enter the first number...: ")
    n2 = input("Enter the second number..: ")
    n3 = input("Enter the third number...: ")
    n4 = input("Enter the fourth number..: ")
    n5 = input("Enter the fifth number...: ")
    n6 = input("Enter the sixth number...: ")

    new_numbers = ("{},{},{},{},{},{},{}\n".format(sel,n1,n2,n3,n4,n5,n6))

    return new_numbers


# This function converts a string into a list
def convertion(tolist):
    ls = []

    for i1 in range(len(tolist)):
        values = tolist[i1]
        values = values.split(",")
        
        for i2 in values:
            ls.append(int(i2))

    return ls