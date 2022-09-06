arr
i = 0
minJump = 0
while(i < n-1):
    minJump += 1
    if arr[i] == 0:
        return -1
    i += arr[i]
