from math import factorial
n = 5


def rightAngle(n):
    for i in range(n):
        for j in range(0, i+1):
            print('*', end=' ')
        print("\r")


def angel180(n):
    k = 2*n-2

    for i in range(n):
        for j in range(0, k):
            print(end=' ')
        k = k-2
        for j in range(0, i+1):
            print('*', end=' ')
        print("\r")


def triangle(n):
    k = n-1
    for i in range(n):
        for j in range(0, k):
            print(end=' ')
        k = k-1
        for j in range(0, i+1):
            print('*', end=' ')
        print("\r")


angel180(10)
rightAngle(10)
triangle(n=10)


def charTree(n):
    num = 1
    k = n-1
    for i in range(n):
        for j in range(0, k):
            print(end='  ')
        k = k-1
        for j in range(0, i+1):
            print(num, end=' ')
            num = num+1
        print('\r')


def fib(n):
    a = 0
    b = 1
    k = n-1
    for i in range(n):
        for j in range(0, k):
            print(end=' ')
        k = k-1
        for j in range(0, i+1):
            c = a+b
            a = b
            b = c
            print(c, end=' ')
        print('\r')


fib(4)


n = 5
k = n-1
for i in range(n):
    for j in range(k):
        print(end=' ')
    k = k-1
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=' ')
    print('\r')
