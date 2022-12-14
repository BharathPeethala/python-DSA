import bisect


def countPairs(X, Y, M, n):
    def count(x, Y, n, NoOfY):
        if x == 0:
            return 0
        if x == 1:
            return NoOfY[0]
        idx = bisect.bisect_right(Y, x)
        ans = n - idx
        ans += NoOfY[0]+NoOfY[1]
        if x == 2:
            ans -= NoOfY[3]+NoOfY[4]
        if x == 3:
            ans += NoOfY[2]

        return ans
    NoOfY = [0]*5
    for i in range(n):
        if Y[i] < 5:
            NoOfY[Y[i]] += 1
    Y.sort()
    total_pairs = 0
    for x in X:
        total_pairs += count(x, Y, n, NoOfY)

    return total_pairs


print(countPairs([2, 3, 4, 5], [1, 2, 3], 4, 3))
