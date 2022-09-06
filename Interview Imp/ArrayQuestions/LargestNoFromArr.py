from functools import cmp_to_key


arr = [3, 30, 34, 9, 5]
arr = [str(i) for i in arr]
n = len(arr)-1
i = 0
while(i <= n):
    j = i+1
    while(j <= n):
        num1 = arr[i]+arr[j]
        num2 = arr[j]+arr[i]
        if num2 > num1:
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    i += 1
res = ""
for i in arr:
    res += i
print(res)


def LongestNumber(arr):
    arr = [str(i) for i in arr]
    n = len(arr)-1
    i = 0

    def compare(n1, n2):
        if n1+n2 > n2+n1:
            return -1
        else:
            return 1
    arr.sort(key=cmp_to_key(compare))
    return str(int("".join(arr)))
