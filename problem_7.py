'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

prime = int(0)
num_ig = int(0)


def miller(n):
    '''
    Check n and return True if n is simple.
    '''
    if n <= 1:
        return False
    elif n < 4:
        return True  # 2 and 3 are prime
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True  # we have already excluded 4, 6 and 8.
    elif n % 3 == 0:
        return False
    else:
        r = round(n ** 0.5)  # n ** 0.5 rounded to the greatest integer r so that r * r <= n
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
    return True


while num_ig != 10001:
    prime += 1
    if miller(prime) is True:
        num_ig += 1
print(prime)
