'''
Problem 7 - 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def isPrime(n):
    if n % 2 == 0 and n != 2:
        return False

    for i in range (3, n // 2, 2):
        if n % i == 0:
            return False

    return True


count = 0
i = 1

while count < 10001:
    i += 1
    if isPrime(i):
        count += 1

print (i)
