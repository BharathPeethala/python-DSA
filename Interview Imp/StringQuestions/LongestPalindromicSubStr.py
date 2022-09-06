str_in = input().strip()
n = len(str_in)
start = 0
dp = [[0 for i in range(n)] for j in range(n)]
maxLength = 0
ans = ""
for k in range(n):
    i = 0
    j = i+k
    while(j < n):
        if i == j:
            dp[i][j] = True
        elif k == 1:
            dp[i][j] = str_in[i] == str_in[j]
        elif str_in[i] == str_in[j] and dp[i+1][j-1]:
            dp[i][j] = True
        j += 1
        i += 1
    if dp[i][j] and j-i+1 > maxLength:
        maxLength = j-i+1
        ans = str_in[i:maxLength]
print(ans)


def longestPalindrome(s):
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    maxlength = 1
    start_index = 0
    end_index = 0

    for i in range(len(s)):
        dp[i][i] = True

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            maxlength = 2
            start_index = i
            end_index = i+1
    for gap in range(2, len(s)):
        for j in range(0, len(s) - gap):
            if s[j] == s[gap+j] and dp[j+1][gap+j-1]:
                dp[j][gap+j] = True
                start_index = j
                end_index = gap + j
            else:
                dp[j][gap+j] = False
    return s[start_index:end_index+1]


s = 'aaaabbaa'
n = len(s)
if n < 2:
    print(s)
    exit()
start = 0
maxLength = 1
for i in range(n):
    low = i-1
    high = i+1
    while(high < n and s[high] == s[i]):
        high += 1
    while(low >= 0 and s[low] == s[i]):
        low -= 1
    while(low >= 0 and high < n and s[low] == s[high]):
        low -= 1
        high += 1
    length = high-low-1
    if (maxLength < length):
        maxLength = length
        start = low+1

print(s[start:maxLength+start])
