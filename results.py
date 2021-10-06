import minis as fm

# Main Menu - The user select the type of game
sel = input("Please select the game you want to analyse (N - Normal | L - Long | X - Salir): ")

if sel == "N":
    numbers = fm.enter_data(1)
    numbers = fm.review_file("N",numbers,0,0)
    numbers = fm.convertion(numbers)
elif sel == "L":
    a = fm.enter_data(1)
    b = fm.enter_data(2)
    c = fm.enter_data(3)

    d = fm.review_file("L",a,b,c)
    numbers = fm.convertion(d)
    print(numbers)
else:
    quit()

# Create and sort a variable concatenating the 6 lists plus the "a1" special list.
numbers.sort()

# Initializing the variables "number", "count" and the result lists; "number" and "count" are the variables who controls the number of repetitions.
number = 0
count = 1

n2 = []
n3 = []
n4 = []
n5 = []
n6 = []

# The core of the program; here makes the comparison, count the numbers and divide in repetitions.
for selection in range(len(numbers)):    
    if number == numbers[selection]:
        count += 1
    else:
        if count == 2:
            n2.append(number)
            count = 1
        elif count == 3:
            n3.append(number)
            count = 1
        elif count == 4:
            n4.append(number)
            count = 1
        elif count >= 5:
            n5.append(number)
            count = 1            
        else:
            count = 1

    number = numbers[selection]

# Shows the numbers divide it in 4 groups.
print("Numbers with 5 or more repetitions:", n5)
print("Numbers with 4 repetitions........:", n4)
print("Numbers with 3 repetitions........:", n3)
print("Numbers with 2 repetitions........:", n2)
