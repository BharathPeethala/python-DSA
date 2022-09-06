prices = [7, 6, 4, 3, 1]
if len(prices) <= 1:
    print(0)
    exit()
profit = 0
start = 0
end = 1
while(end < len(prices)):
    if prices[start] < prices[end]:
        profit = max(profit, prices[end]-prices[start])
    else:
        start = end
    end += 1
print(profit)
