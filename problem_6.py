'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

num_sum_sq = int(0)
num_sq_sum = int(0)

for i in range(1, 101):
    num_sq_sum += i * i
    num_sum_sq += i
print(num_sum_sq * num_sum_sq - num_sq_sum)
