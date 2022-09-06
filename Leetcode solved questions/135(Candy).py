ratings = [1, 2, 87, 87, 87, 2, 1]
n = len(ratings)
candies = [1]*n
for i in range(n-1):
    print(ratings[i], end=' ')
    if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
        candies[i] = candies[i+1]+1
    elif ratings[i+1] > ratings[i] and candies[i+1] <= candies[i]:
        candies[i+1] = candies[i]+1
print()
for i in range(n-1, 0, -1):
    print(ratings[i], end=' ')
    if ratings[i-1] < ratings[i] and candies[i-1] >= candies[i]:
        candies[i] = candies[i-1]+1
    elif ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
        candies[i-1] = candies[i]+1
print()
print(sum(candies))
