bags = list()
capacity = [2, 3, 4, 5]
rocks = [1, 2, 4, 4]
additionalRocks = 2
for i in range(len(capacity)):
    bags.append(capacity[i]-rocks[i])
bags.sort()
count = 0
for i in bags:
    if i == 0:
        count += 1
    elif additionalRocks >= i:
        additionalRocks -= i
        count += 1

print(count)
