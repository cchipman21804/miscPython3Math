# The average of four numbers is 9
# If three of those numbers are 5, 9, & 12
# What is the fourth number?
#
def sumList(numList):
    listSum = 0
    for i in range(len(numList)):
        listSum += numList[i]
    return listSum
#
#a = 9
#n = 4
#w = 5
#y = 9
#z = 12
#x = a*n-(w+y+z)
#print(x)
#exit(0)
#
validInput = False
while not validInput:
    a = input("Enter Average: ")
    try:
        a = float(a)
    except ValueError:
        print("Enter a numeric value\n")
        validInput = False
    else:
        validInput = True
#
validInput = False
while not validInput:
    n = input("Enter length of list: ")
    try:
        n = int(n)
    except ValueError:
        print("Enter a whole number\n")
        validInput = False
    else:
        validInput = True
#
numbers = []
for i in range(n-1):
    validInput = False
    while not validInput:
        x = input(f"Enter numeric value #{i+1}: ")
        try:
            x = float(x)
        except ValueError:
            print("\n")
            validInput = False
        else:
            numbers.append(x)
            validInput = True
#
x = a*n-sumList(numbers)
print(f"The missing value is: {x}")
#
