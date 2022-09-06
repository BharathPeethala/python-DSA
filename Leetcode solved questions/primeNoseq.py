

def isPrime(n):
    i = 2
    while(i*i <= n):
        if n % i == 0:
            return False
        i += 1
    return True


n1 = 3
n2 = 10000

for i in range(n1, n2+1):
    if isPrime(i):
        print(i, end=' ')
