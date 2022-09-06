h, w = 5, 4
horizontalCuts = [1, 2, 4]
verticalCuts = [1, 3]
l, b = 0, 0
horizontalCuts.append(0)
horizontalCuts.append(h)
verticalCuts.append(0)
verticalCuts.append(w)
horizontalCuts.sort()
verticalCuts.sort()

for i in range(1, len(horizontalCuts)):
    l = max(l, horizontalCuts[i]-horizontalCuts[i-1])
for i in range(1, len(verticalCuts)):
    b = max(b, verticalCuts[i]-verticalCuts[i-1])

print((l*b) % (10**9+7))
