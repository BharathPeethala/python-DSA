nums = [1, 7, 3, 6, 5, 6]
leftSum = 0
rightSum = sum(nums)
mid = 0
while mid < len(nums):
    leftSum += nums[mid]
    if leftSum == rightSum:
        print(mid)
        break
    rightSum -= nums[mid]
    mid += 1
print(-1)
