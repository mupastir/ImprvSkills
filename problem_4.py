'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

num_pol = int(0)  # number polindrom

for i in range(100, 1000):
    for j in range(100, 1000):
        num_st = str(i * j)  # число в уме
        if num_st[:3] == num_st[:2:-1] and num_pol <= (i * j):
            num_pol = i * j
print(num_pol)
