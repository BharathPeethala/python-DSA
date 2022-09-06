class Solution:
    def solve(self, A):
        dp = [0, 0, 0]
        for i in range(len(A)):
            dp0 = A[i][0] + min(dp[1], dp[2])
            dp1 = A[i][1] + min(dp[2], dp[0])
            dp2 = A[i][2] + min(dp[1], dp[0])
            dp = [dp0, dp1, dp2]
        return min(dp)
