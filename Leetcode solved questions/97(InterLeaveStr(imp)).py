from functools import cache


s1 = "abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb"
s2 = "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc"
s3 = "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"
if len(s1) + len(s2) != len(s3):
    print(False)


@cache
def dfs(i, j):
    if i == len(s1) and j == len(s2):
        return True
    choose_s1, choose_s2 = False, False
    if i < len(s1) and s1[i] == s3[i + j]:
        choose_s1 = dfs(i + 1, j)
    if j < len(s2) and s2[j] == s3[i + j]:
        choose_s2 = dfs(i, j + 1)

    return choose_s1 or choose_s2


print(dfs(0, 0))

# Tabulation


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                choose_s1, choose_s2 = False, False
                if s1[i - 1] == s3[i + j - 1]:
                    choose_s1 = dp[i - 1][j]
                if s2[j - 1] == s3[i + j - 1]:
                    choose_s2 = dp[i][j - 1]
                dp[i][j] = choose_s1 or choose_s2

        return dp[m][n]


# Tabulation - Space Optimized
class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if n > m:
            m, n = n, m
            s1, s2 = s2, s1
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                choose_s1, choose_s2 = False, False
                if s1[i - 1] == s3[i + j - 1]:
                    choose_s1 = dp[j]
                if s2[j - 1] == s3[i + j - 1]:
                    choose_s2 = dp[j - 1]
                dp[j] = choose_s1 or choose_s2

        return dp[-1]
