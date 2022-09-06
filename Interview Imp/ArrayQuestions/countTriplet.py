# brute force
def findTriplets(arr):
    n = len(arr)
    count = 0
    arr.sort()
    print(arr)
    for i in range(len(arr)):
        for j in range(i+1, n):
            if bs(arr[i]+arr[j], arr):
                print(arr[i], arr[j])
                count += 1
    return count


def bs(search, arr):
    i, j = 0, len(arr)-1
    while(i <= j):
        mid = (i+j)//2
        if arr[mid] < search:
            i = mid+1
        elif arr[mid] > search:
            j = mid-1
        else:
            return True
    return False

# efficient


def countTriplet(arr, n):
    n = len(arr)
    count = 0
    arr.sort()
    for i in range(len(arr)-1, -1, -1):
        j, k = 0, i-1
        while(j < k):
            if arr[i] == arr[j]+arr[k]:
                count += 1
                j += 1
                k -= 1
            elif arr[i] > arr[j]+arr[k]:
                j += 1
            else:
                k -= 1
    return count


print(findTriplets([1, 5, 3, 2]))
