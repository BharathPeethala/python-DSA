hashmap = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
res = 0
prev = 0
S = 'MMMCMXCIX'
# S = S[::-1]
for i in S:
    print(prev)
    if hashmap[i] < prev:
        res += hashmap[i]
    else:
        res -= hashmap[i]
    prev = hashmap[i]

print(res)
