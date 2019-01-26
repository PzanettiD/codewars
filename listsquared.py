# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python
# Given two integers m, n (1 <= m <= n) 
# find all integers between m and n
# whose sum of squared divisors is itself a square.
from math import sqrt
nums = [None] * 10000
results = [None] * 10000
def list_squared(m, n):
    result = []
    k = 0
    if m == nums[m]:
        while m + k != n and m + k == nums[m]:
            result.append(results[m + k])
            k += 1 
    for i in range(m + k, n):
        sum = 0
        for j in range(1, i+1):
            if i % j == 0:
                sum += pow(j, 2)
        if sqrt(sum).is_integer():
            result.append([i, sum])
            nums[i] = i
            results[i] = [i, sum]
    return result

print(list_squared(296, 2909))
print(list_squared(500, 7000))
        