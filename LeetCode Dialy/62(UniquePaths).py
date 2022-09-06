def fun(m, n):
    row = [1] * n
    for i in range(m-1):
        newRow = [1]*n
        for j in range(n-2, -1, -1):
            newRow[j] = newRow[j+1]+row[j]
        print(newRow)
        row = newRow
    return row[0]


print(fun(5, 4))
