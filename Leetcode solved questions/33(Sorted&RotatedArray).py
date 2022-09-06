def search(nums, target):
    k = 0
    n = len(nums)
    if n == 0:
        return -1
    if n == 1 and target == nums[0]:
        return 0
    i = 0
    j = 1
    while(j < n):
        if nums[i] < nums[j]:
            k += 1
            i += 1
            j += 1
        else:
            break
    if k == n-1:
        k = 0
    nums2 = [1 for _ in range(n)]
    for i in range(n):
        nums2[(i+k) % n] = nums[i]
    print(nums2)

    def bs(nums, target):
        low, high = 0, len(nums)-1
        while(low <= high):
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1
    n1 = bs(nums2, target)
    return (n1+k) % n if n1 != -1 else -1


print(search([3, 2, 1], 1))
