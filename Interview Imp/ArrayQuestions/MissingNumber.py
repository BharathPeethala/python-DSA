n = 5
array = {1, 2, 3, 5}
array = set(array)
for i in range(1, n+1):
    if i not in array:
        print(i)
    break
