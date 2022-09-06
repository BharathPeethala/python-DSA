import functools
# Python3 program to arrange the
# given array of numbers
# to form the largest number

# A comparison function which
# is used by sort() in
# printLargest()


def myCompare(x, y):

    xy = x
    yx = y

    # Count length of x and y
    countx = 0
    county = 0

    # Count length of X
    while (x > 0):
        countx += 1
        x //= 10

    # Count length of Y
    while (y > 0):
        county += 1
        y //= 10

    x = xy
    y = yx

    while (countx):
        countx -= 1
        yx *= 10

    while (county):
        county -= 1
        xy *= 10

    # Append x to y
    yx += x

    # Append y to x
    xy += y

    return 1 if xy > yx else -1

# The main function that prints
# the arrangement with the
# largest value. The function
# accepts a vector of strings


def printLargest(arr):

    # Sort the numbers using
    # library sort function. The
    # function uses our comparison
    # function myCompare() to
    # compare two strings. See

    arr.sort(key=functools.cmp_to_key(myCompare))
    arr.reverse()

    print("".join(map(str, arr)))


# Driver code
arr = [54, 546, 548, 60]

# Function Hall
printLargest(arr)

# This code is contributed by phasing17
