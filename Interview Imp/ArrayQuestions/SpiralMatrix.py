matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
n = len(matrix)
m = len(matrix[n-1])
direction = 0
j = 0
left, right, top, bottom = 0, m-1, 0, n-1

while(top <= bottom and left <= right):
    if direction == 0:
        for i in range(left, right+1):
            print(matrix[top][i], end=' ')
        top += 1
    elif direction == 1:
        for i in range(top, bottom+1):
            print(matrix[i][right], end=' ')
        right -= 1
    elif direction == 2:
        for i in range(right, left-1, -1):
            print(matrix[bottom][i], end=' ')
        bottom -= 1
    elif direction == 3:
        for i in range(bottom, top-1, -1):
            print(matrix[i][left], end=' ')
        left += 1
    direction = (direction+1) % 4
