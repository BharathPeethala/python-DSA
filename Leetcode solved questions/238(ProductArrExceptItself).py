nums = [1, 2, 3, 4]


def product(nums):
    n = len(nums)
    res = [1 for _ in range(n)]
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    postFix = 1
    for i in range(n-1, -1, -1):
        res[i] *= postFix
        postFix *= nums[i]
    return res


print(product(nums))
