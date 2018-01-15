'''
Project Euler Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def fib(a, b, t): # where a and b are the last two values, and t is the total
    if a > 4000000:
        return t
    elif (a + b) % 2 == 0:
        return fib(a + b, a, t + a + b)
    else:
        return fib (a + b, a, t)

if __name__ == "__main__":
    print (fib(1, 1, 0))
