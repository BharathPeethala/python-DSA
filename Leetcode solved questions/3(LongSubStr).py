s = "abcabcbb"
maps = dict()
i = 0
res = 0
for j in range(len(s)):
    if s[j] in maps:
        i = max(maps[s[j]], i)
    res = max(res, j-i+1)
    maps[s[j]] = j+1

print(res)
