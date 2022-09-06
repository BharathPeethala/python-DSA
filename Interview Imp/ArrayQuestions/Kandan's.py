def maxSubArraySum(arr, N):
    max_end, max_sofar = 0, -999999999999999999999999999999999999999999
    for i in arr:
        max_end += i
        if i > max_end:
            max_end = i
        if max_sofar < max_end:
            max_sofar = max_end
    return max_sofar
