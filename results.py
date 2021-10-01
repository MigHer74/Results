# The results of each draw are divided into lists. The list "a1" is only a greater number that is placed at the end of the concatenation of the lists.
r1 = [3,4,12,19,23,37]
r2 = [7,14,21,24,34,36]
r3 = [13,17,25,28,38,39]
r4 = [1,8,21,22,34,37]
r5 = [11,18,25,27,31,39]
r6 = [1,4,7,10,28,29]
a1 = [100]

# Create and sort a variable concatenating the 6 lists plus the "a1" special list.
numbers = r1 + r2 + r3 + r4 + r5 + r6 + a1
numbers.sort()

# Initializing the variables "number", "count" and the result lists; "number" and "count" are the variables who controls the number of repetitions.
number = 0
count = 1

n2 = []
n3 = []
n4 = []
n5 = []

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
