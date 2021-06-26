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
beltLength = dataEntry("Enter belt length: ")
pulley1Diameter = dataEntry("Enter diameter of pulley #1: ")
pulley2Diameter = dataEntry("Enter diameter of pulley #2: ")

pulleyDiameterSum = pulley1Diameter + pulley2Diameter
pulleyDiameterDiff = pulley2Diameter - pulley1Diameter
x = 4 * beltLength - (2 * math.pi) * pulleyDiameterSum
numerator = x + math.sqrt(pow(x,2) - 32 * pow(pulleyDiameterDiff,2))
pulleyDistance = numerator/16

print(pulleyDistance)
