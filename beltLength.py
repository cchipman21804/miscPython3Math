# Calculate pulley distance & belt length
import math
#
def dataEntry(promptText):
    validInput = False
    while not validInput:
        data = input(promptText)
        try:
            data = float(data)
        except:
            validInput = False
        validInput = True
        return data
#
pulley1Diameter = dataEntry("Enter diameter of pulley #1: ")
pulley2Diameter = dataEntry("Enter diameter of pulley #2: ")
pulleyDistance = dataEntry("Enter center-to-center distance between the pulleys: ")

beltLength = math.pi * (pulley1Diameter + pulley2Diameter) * 0.5 + (pulleyDistance * 2) + (pow((pulley2Diameter - pulley1Diameter),2) / (pulleyDistance * 4))

print(beltLength)
