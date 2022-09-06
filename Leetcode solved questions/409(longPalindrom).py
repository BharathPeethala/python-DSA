from collections import Counter


s = "abccccdd"
count = sum([(x//2) * 2 for x in Counter(s).values()])
print(count if count == len(s) else (count + 1))
