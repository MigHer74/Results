import minis as fm

# Ask to the user to enter the 6 numbers of the last week
n1 = input("Enter the first number...: ")
n2 = input("Enter the second number..: ")
n3 = input("Enter the third number...: ")
n4 = input("Enter the fourth number..: ")
n5 = input("Enter the fifth number...: ")
n6 = input("Enter the sixth number...: ")

new_numbers = ("{},{},{},{},{},{}\n".format(n1,n2,n3,n4,n5,n6))

# Open the file to read the previous numbers and  insert the numbers of the last week
lr = []
ac_file = open("results.txt","r")

for i in ac_file:
    lr.append(i)

ac_file.close()

nl0 = new_numbers
nl1 = lr[0]
nl2 = lr[1]
nl3 = lr[2]
nl4 = lr[3]
nl5 = lr[4]

nw_file = open("results.txt","w")

nw_file.write(nl0)
nw_file.write(nl1)
nw_file.write(nl2)
nw_file.write(nl3)
nw_file.write(nl4)
nw_file.write(nl5)

nw_file.close()

r1 = convertion(nl0)
r2 = convertion(nl1)
r3 = convertion(nl2)
r4 = convertion(nl3)
r5 = convertion(nl4)
r6 = convertion(nl5)
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
