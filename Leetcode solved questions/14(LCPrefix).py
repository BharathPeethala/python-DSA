import math


def longestCommonPrefix(strs):
    mini = min(strs, key=lambda x: len(x))
    m = math.inf
    for string in strs:
        s = 0
        for i in range(len(mini)):
            if mini[i] != string[i]:
                break
            s += 1
        m = min(s, m)
    return mini[:m]


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
print(math.inf)
