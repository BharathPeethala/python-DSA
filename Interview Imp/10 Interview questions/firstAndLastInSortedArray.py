def find_start(arr, target):
    left, right = 0, len(arr)-1
    start, end = -1, -1
    while(left <= right):
        mid = (left+right)//2
        if arr[mid] == target and arr[mid-1] != target:
            start = mid
            j = mid+1
            while j < len(arr) and arr[j] == target:
                j += 1
            end = j-1
            return start, end
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1


print(find_start([1, 2, 3, 5, 5, 5, 7, 8, 9], 5))
