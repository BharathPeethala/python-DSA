boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4
boxTypes.sort(key=lambda x: x[1], reverse=True)
res = 0
for noOfBoxes, unitsPerBox in boxTypes:
    numBoxes = min(truckSize, noOfBoxes)
    res += (numBoxes*unitsPerBox)
    truckSize -= numBoxes

print(res)
