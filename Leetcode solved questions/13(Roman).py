s = "MCMXCIV"
hashmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
num = 0
n = len(s)
for i in range(n):
    if i+1 < n and hashmap[s[i]] < hashmap[s[i+1]]:
        num -= hashmap[s[i]]
    else:
        num += hashmap[s[i]]
print(num)
