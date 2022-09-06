from itertools import permutations
permu = permutations('ABC')
res = list()
for i in permu:
    i = "".join(list(i))
    res.append(i)
print(res)
