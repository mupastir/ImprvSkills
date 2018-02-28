'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

num_mul = int(20)
i = bool()
in_num = bool()

while i is False:
    in_num = False
    num_mul += 20
    for j in range(1, 21):
        if num_mul % j != 0:
            in_num = True
    if in_num is False:
        i = True
    print(num_mul)
print(num_mul)
