'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

a = int(0)
b = int(0)
c = int(0)
num_p = int(1000)

for j in range(1, num_p - 1):
    a = j
    for i in range(1, int((num_p - a) / 2)):
        c = i
        b = num_p - a - c
        if a * a == (c * c + b * b) or c * c == (a * a + b * b) or b * b == (a * a + c * c):
            print(a * b * c, a, b, c)
