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


# This function opens the file, save the new numbers, get the numbers of the previous weeks and closes the file
def review_file(game,nw1,nw2,nw3):
    lr = []

    if game == "N":
        ac_file = open("res_n.txt","r")

        for i in ac_file:
            lr.append(i)

        ac_file.close()

        nl0  = nw1
        nl1  = lr[0]
        nl2  = lr[1]
        nl3  = lr[2]
        nl4  = lr[3]
        nl5  = lr[4]
    else:
        ac_file = open("res_l.txt","r")

        for i in ac_file:
            lr.append(i)

        ac_file.close()

        nl0  = nw1
        nl1  = nw2
        nl2  = nw3
        nl3  = lr[0]
        nl4  = lr[1]
        nl5  = lr[2]
        nl6  = lr[3]
        nl7  = lr[4]
        nl8  = lr[5]
        nl9  = lr[6]
        nl10 = lr[7]
        nl11 = lr[8]
        nl12 = lr[9]
        nl13 = lr[10]
        nl14 = lr[11]
        nl15 = lr[12]
        nl16 = lr[13]
        nl17 = lr[14]
    
    if game == "N":
        nw_file = open("res_n.txt","w")

        nw_file.write(nl0)
        nw_file.write(nl1)
        nw_file.write(nl2)
        nw_file.write(nl3)
        nw_file.write(nl4)
        nw_file.write(nl5)
    else:
        nw_file = open("res_l.txt","w")

        nw_file.write(nl0)
        nw_file.write(nl1)
        nw_file.write(nl2)
        nw_file.write(nl3)
        nw_file.write(nl4)
        nw_file.write(nl5)
        nw_file.write(nl6)
        nw_file.write(nl7)
        nw_file.write(nl8)
        nw_file.write(nl9)
        nw_file.write(nl10)
        nw_file.write(nl11)
        nw_file.write(nl12)
        nw_file.write(nl13)
        nw_file.write(nl14)
        nw_file.write(nl15)
        nw_file.write(nl16)
        nw_file.write(nl17)

    nw_file.close()

    if game == "N":
        return nl0[2:-1],nl1[2:-1],nl2[2:-1],nl3[2:-1],nl4[2:-1],nl5[2:-1]
    else:
        return nl0[2:-1],nl1[2:-1],nl2[2:-1],nl3[2:-1],nl4[2:-1],nl5[2:-1],nl6[2:-1],nl7[2:-1],nl8[2:-1],nl9[2:-1],nl10[2:-1],nl11[2:-1],nl12[2:-1],nl13[2:-1],nl14[2:-1],nl15[2:-1],nl16[2:-1],nl17[2:-1]


# This function converts a string into a list
def convertion(tolist):
    ls = []

    for i1 in range(len(tolist)):
        values = tolist[i1]
        values = values.split(",")
        
        for i2 in values:
            ls.append(int(i2))

    ls.append(100)

    return ls