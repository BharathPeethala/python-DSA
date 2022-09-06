nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
i, j = m-1, n-1
placing = m+n-1
while(j >= 0 and i >= 0):
    if nums1[i] > nums2[j]:
        nums1[placing] = nums1[i]
        i -= 1
    else:
        nums1[placing] = nums2[j]
        j -= 1
    placing -= 1
while(j >= 0):
    nums1[placing] = nums2[j]
    j, placing = j-1, placing-1
