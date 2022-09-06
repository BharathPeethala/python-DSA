arr = [4, 3, 5, 7]
n = len(arr)
big = arr[0]
small = arr[n-1]
minArray = list()
maxArray = list()
ele = -1
for i in arr:
    if i > big:
        big = i
    maxArray.append(big)
arr.reverse()
for i in arr:
    if i < small:
        small = i
    minArray.append(small)
minArray.reverse()
for i in range(n):
    if i != 0 and i != n-1 and minArray[i] == maxArray[i]:
        ele = (minArray[i])
        break

print(ele)
