from collections import deque

nums = [1, -1, -2, 4, -7, 3]
k = 2
n = len(nums)
deq = deque([n-1])
for i in range(n-2, -1, -1):
    if deq[0] - i > k:
        deq.popleft()
    nums[i] += nums[deq[0]]
    while len(deq) and nums[deq[-1]] <= nums[i]:
        deq.pop()
    deq.append(i)
print(nums[0])
