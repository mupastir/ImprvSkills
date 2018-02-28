'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

num_sum_prm = int(0)


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


for i in range(2, 2000000):
    if miller(i) is True:
        num_sum_prm += i
print(num_sum_prm)
