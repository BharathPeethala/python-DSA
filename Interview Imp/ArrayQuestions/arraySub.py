# brutforce
# from jmespath import search
from functools import cmp_to_key


def mycmp(a, b):
    return a - b


def subArray(arr, sum):
    curr_sum = 0
    n = len(arr)
    for i in range(n):
        curr_sum = arr[i]
        for j in range(i+1, n+1):
            print(f'current_sum of arr[{i}:{j}]:{curr_sum}')
            if curr_sum == sum:
                return [i+1, j]
            if curr_sum > sum or j >= n:
                break
            curr_sum += arr[j]
    return -1

# efficient approach


def subArraySum(arr, n, sum):
    curr_sum = arr[0]
    start = 0
    end = 1
    while(end <= n):
        while(curr_sum > sum and start < end-1):
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum:
            return [start+1, end]
        if end < n:
            curr_sum += arr[end]
        end += 1
    return [-1]


str_in = "135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134"
arr_in = [int(i) for i in str_in.split()]

print(subArraySum(arr_in, 468))
