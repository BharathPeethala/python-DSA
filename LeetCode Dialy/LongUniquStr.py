S = "aaaaaaaa"

N = len(S)
subSet = set()
if N < 2:
    print(S)
    exit()
last_index = {}
start_index = 0
length = 0
for j, i in enumerate(S):
    if i in last_index:
        start_index = max(start_index, last_index[i]+1)
    length = max(length, j-start_index+1)
    last_index[i] = j
print(length)
